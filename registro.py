"""Assistente de comandos em português para edição da ECF.

Interpreta pedidos escritos em linguagem natural ("inserir M310 com COD_CTA
1.01.01.001", "alterar o campo NOME do 0000 para ...", "quantos M300 existem?")
e os traduz em operações **determinísticas** executadas pela engine, sempre
com base no leiaute (o manual da ECF carregado em ``/layouts``).

Princípios de segurança adotados:

* O assistente **nunca inventa valores**. Se o pedido não informa o valor de um
  campo obrigatório, ele pergunta em vez de preencher.
* Toda alteração passa por **pré-visualização** (linha antes → linha depois) e
  só é aplicada após confirmação explícita do usuário.
* O número de campos do registro criado vem **sempre do leiaute**, garantindo
  estrutura válida mesmo que o usuário informe só um ou dois campos.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from ..models import ArquivoECF, Registro
from .layout_loader import LayoutLoader

# --------------------------------------------------------------------------- #
# CONSTANTES
# --------------------------------------------------------------------------- #
RE_REGISTRO = re.compile(r"\b(\d{4}|[A-Z]\d{3})\b")
RE_PAR = re.compile(
    r"([A-Z][A-Z0-9_]{1,30})\s*(?:=|:|\bpara\b|\bcomo\b)\s*"
    r"(\"[^\"]*\"|'[^']*'|[^,;]+?)(?=\s*(?:,|;|\se\s|$))",
    re.IGNORECASE)
RE_INDICE = re.compile(r"#\s*(\d+)")
MAX_PREVIA = 12

# Palavras que indicam "trocar o que já existe" em vez de apenas acrescentar
GATILHOS_SUBSTITUIR = (
    "substituir", "substitua", "trocar", "troque", "apagar as anteriores",
    "apagar as informações anteriores", "apagar as informacoes anteriores",
    "apagar os anteriores", "apagar tudo", "excluir as anteriores",
    "remover as anteriores", "sobrescrever", "refazer", "zerar",
    "limpar e inserir", "bloco inteiro", "todo o bloco",
)

ACOES = {
    "inserir": ("inserir", "incluir", "adicionar", "criar", "acrescentar"),
    "alterar": ("alterar", "mudar", "trocar", "corrigir o campo", "atualizar",
                "editar", "substituir", "ajustar o campo"),
    "remover": ("remover", "excluir", "apagar", "deletar", "eliminar"),
    "reparar": ("reparar", "corrigir estrutura", "corrigir automaticamente",
                "arrumar", "sanear"),
    "recalcular": ("recalcular", "atualizar totalizadores", "recontar"),
    "consultar": ("o que é", "o que e", "quantos", "quantas", "campos do",
                  "campos de", "mostrar", "listar", "explique", "explicar",
                  "consultar", "detalhe", "detalhes"),
}

AJUDA = r"""**Como falar comigo**

| Intenção | Exemplo |
|---|---|
| Consultar o manual | `o que é o M300?` · `campos do 0020` · `quantos M350?` |
| Inserir registro | `inserir M310 com COD_CTA = 1.01.01.001` |
| Alterar campo | `no 0000, alterar NOME para EMPRESA X LTDA` |
| Alterar com filtro | `alterar VALOR para 100,00 no M300 onde COD_CTA = 1.01` |
| Alterar por posição | `alterar COD_CTA para 2.01 no M310 #2` |
| Remover registros | `remover M310 onde COD_CTA = 1.01.01.001` |
| Sanear estrutura | `corrigir estrutura` · `recalcular totalizadores` |
| **Inserir lote** | cole as linhas prontas: `\|Y570\|00083430000114\|...\|` |
| **Substituir bloco** | cole as linhas + a palavra `substituir` |

Nos lotes, aceito as linhas coladas de qualquer jeito — uma por linha,
grudadas ou todas numa só. Confiro cada registro contra o leiaute (número de
campos e obrigatórios) antes de aplicar.

Sempre mostro uma **pré-visualização** antes de aplicar qualquer mudança.
"""


# --------------------------------------------------------------------------- #
# Estruturas
# --------------------------------------------------------------------------- #
@dataclass
class Comando:
    acao: str = ""
    registro: str = ""
    campos: Dict[str, str] = field(default_factory=dict)
    filtro: Dict[str, str] = field(default_factory=dict)
    indice: Optional[int] = None
    texto: str = ""
    registros: List[Registro] = field(default_factory=list)   # lote colado


@dataclass
class Resposta:
    mensagem: str                                   # markdown para o chat
    comando: Optional[Comando] = None               # o que será aplicado
    previa: List[Tuple[str, str]] = field(default_factory=list)  # antes, depois
    aplicavel: bool = False                         # exige confirmação?
    alvos: int = 0                                  # nº de registros afetados


# --------------------------------------------------------------------------- #
# Assistente
# --------------------------------------------------------------------------- #
class Assistente:
    """Traduz linguagem natural em operações validadas pelo leiaute."""

    def __init__(self, layout: LayoutLoader, versao: str) -> None:
        self.layout = layout
        self.versao = versao

    # ------------------------------------------------------------------ #
    # Interpretação
    # ------------------------------------------------------------------ #
    def interpretar(self, texto: str) -> Comando:
        t = texto.strip()
        baixo = t.lower()

        acao = ""
        # a ordem importa: 'corrigir estrutura' antes de 'corrigir o campo'
        for nome in ("reparar", "recalcular", "inserir", "remover",
                     "alterar", "consultar"):
            if any(g in baixo for g in ACOES[nome]):
                acao = nome
                break

        cmd = Comando(acao=acao, texto=t)

        m = RE_REGISTRO.search(t.upper())
        if m:
            cmd.registro = m.group(1)

        mi = RE_INDICE.search(t)
        if mi:
            cmd.indice = int(mi.group(1))

        # Remove do texto as referências estruturais ("no M310", "#2") antes
        # de extrair os pares campo=valor, para que elas não sejam capturadas
        # como parte do VALOR (ex.: "para 9.99 no M310").
        limpo = RE_INDICE.sub(" ", t)
        if cmd.registro:
            limpo = re.sub(
                rf"(?:\b(?:n[oa]|d[oa]|em|para|no registro|do registro)\s+)?"
                rf"(?:registro\s+)?{re.escape(cmd.registro)}\b",
                " ", limpo, flags=re.IGNORECASE)

        # separa a parte de filtro ("onde ...") da parte de valores
        parte_valor, parte_filtro = limpo, ""
        mo = re.search(r"\bonde\b", limpo, re.IGNORECASE)
        if mo:
            parte_valor = limpo[:mo.start()]
            parte_filtro = limpo[mo.end():]

        cmd.campos = self._pares(parte_valor)
        cmd.filtro = self._pares(parte_filtro)

        # em consultas, "campos do M300" não é par campo=valor
        if acao == "consultar":
            cmd.campos, cmd.filtro = {}, {}
        return cmd

    @staticmethod
    def _pares(texto: str) -> Dict[str, str]:
        pares: Dict[str, str] = {}
        for m in RE_PAR.finditer(texto):
            nome = m.group(1).upper()
            valor = m.group(2).strip().strip("\"'")
            # evita capturar o próprio código do registro como campo
            if RE_REGISTRO.fullmatch(nome):
                continue
            pares[nome] = valor
        return pares

    # ------------------------------------------------------------------ #
    # Registros colados em bruto (|Y570|...|)
    # ------------------------------------------------------------------ #
    def extrair_brutos(self, texto: str) -> List[Registro]:
        """Extrai registros no formato ``|REG|campo|campo|`` de um texto livre.

        Tolera que as linhas venham coladas numa só (``...|0,00| |Y570|...``),
        separadas por quebras de linha, ou grudadas (``|0,00||Y570|``): o corte
        é feito sempre que aparece um código de registro **existente no
        leiaute** logo após um separador vazio.
        """
        if "|" not in texto:
            return []

        partes = texto.split("|")
        registros: List[Registro] = []
        atual: List[str] = []

        for i, bruto in enumerate(partes):
            tok = bruto.strip()
            anterior_vazio = (i == 0) or (partes[i - 1].strip() == "")
            # Um código válido inicia registro quando vem após um separador
            # vazio OU quando ainda não começamos nenhum registro (o texto
            # do pedido pode preceder a primeira linha colada).
            inicia = (self.layout.existe(self.versao, tok.upper())
                      and (anterior_vazio or not atual))
            if inicia:
                if atual:
                    registros.append(Registro(campos=list(atual)))
                atual = [tok.upper()]
            elif atual:
                if tok == "" and i == len(partes) - 1:
                    continue          # separador final da última linha
                atual.append(bruto.strip())

        if atual:
            registros.append(Registro(campos=list(atual)))

        # descarta o separador vazio que sobra ao final de cada registro
        limpos: List[Registro] = []
        for r in registros:
            campos = list(r.campos)
            while len(campos) > 1 and campos[-1] == "":
                lr = self.layout.registro(self.versao, campos[0])
                if lr and len(campos) <= lr.num_campos:
                    break
                campos.pop()
            limpos.append(Registro(campos=campos))
        return limpos

    def _prever_lote(self, texto: str, brutos: List[Registro],
                     arquivo: ArquivoECF) -> Resposta:
        tipos = sorted({r.reg for r in brutos})
        baixo = texto.lower()
        substituir = any(g in baixo for g in GATILHOS_SUBSTITUIR)

        # --- validação estrutural contra o leiaute --- #
        problemas: List[str] = []
        for i, r in enumerate(brutos, 1):
            lr = self.layout.registro(self.versao, r.reg)
            if not lr:
                problemas.append(f"linha {i}: registro {r.reg} não existe.")
                continue
            if r.num_campos != lr.num_campos:
                problemas.append(
                    f"linha {i} ({r.reg}): {r.num_campos} campos, "
                    f"o leiaute exige {lr.num_campos}.")
                continue
            for c in lr.campos:
                if c.obrigatorio == "Sim" and c.seq > 1 \
                        and r.campo(c.seq - 1).strip() == "":
                    problemas.append(
                        f"linha {i} ({r.reg}): campo obrigatório "
                        f"'{c.nome}' vazio.")

        if problemas:
            amostra = "\n".join(f"- {p}" for p in problemas[:10])
            resto = (f"\n\n…e mais {len(problemas) - 10} problema(s)."
                     if len(problemas) > 10 else "")
            return Resposta(
                f"Encontrei **{len(problemas)} problema(s)** nos registros "
                f"colados. Não vou inserir nada até que sejam corrigidos:\n\n"
                f"{amostra}{resto}")

        cmd = Comando(
            acao="lote_substituir" if substituir else "lote_inserir",
            texto=texto, registros=brutos)
        cmd.registro = tipos[0] if len(tipos) == 1 else ""

        existentes = {t: arquivo.contagem_por_tipo().get(t, 0) for t in tipos}
        resumo_tipos = ", ".join(
            f"**{t}** ({len(([r for r in brutos if r.reg == t]))} novo(s), "
            f"{existentes[t]} no arquivo)" for t in tipos)

        previa = [("(novo)", r.para_linha()) for r in brutos[:MAX_PREVIA]]

        if substituir:
            total_remover = sum(existentes.values())
            msg = (f"Entendi: **substituir o bloco**.\n\n"
                   f"Vou **remover os {total_remover} registro(s) existentes** "
                   f"de {', '.join(tipos)} e inserir **{len(brutos)} novo(s)** "
                   f"na posição correta, recalculando todos os totalizadores."
                   f"\n\nTipos: {resumo_tipos}"
                   f"\n\n⚠️ Os registros atuais serão apagados.")
        else:
            msg = (f"Vou **inserir {len(brutos)} registro(s)** na posição "
                   f"correta do bloco e recalcular os totalizadores.\n\n"
                   f"Tipos: {resumo_tipos}\n\n"
                   f"*Se a intenção era trocar os existentes, escreva "
                   f"\"substituir\" junto com os registros.*")

        if len(brutos) > MAX_PREVIA:
            msg += f"\n\nPrévia das {MAX_PREVIA} primeiras de {len(brutos)}."

        return Resposta(msg, comando=cmd, aplicavel=True,
                        alvos=len(brutos), previa=previa)

    # ------------------------------------------------------------------ #
    # Processamento (gera resposta + prévia, sem aplicar)
    # ------------------------------------------------------------------ #
    def processar(self, texto: str, arquivo: ArquivoECF) -> Resposta:
        baixo = texto.strip().lower()
        if baixo in ("ajuda", "help", "?", "o que você faz",
                     "o que voce faz", "comandos"):
            return Resposta(AJUDA)

        # Reclassificações → dirige o usuário para a aba com upload
        if any(g in baixo for g in ("reclassific", "reclassif", "de para",
                                    "de→para", "de-para")):
            return Resposta(
                "Para fazer as **reclassificações**, abra a aba "
                "**🔄 Reclassificar** e importe a planilha De→Para.\n\n"
                "O que eu espero na planilha (colunas ajustáveis na tela):\n\n"
                "| Coluna | Conteúdo |\n|---|---|\n"
                "| **Y** | código atual (o que vocês usam) |\n"
                "| **Z** | código pedido pela auditoria |\n"
                "| **F** | `PARTE B` **ou** o número da conta contábil |\n"
                "| **G** | conta da Parte B |\n\n"
                "Regra que vou seguir: se a coluna F disser **PARTE B**, "
                "reclassifico apenas o lançamento ligado àquela conta da "
                "Parte B (coluna G); se trouxer um **número de conta**, "
                "reclassifico apenas o lançamento ligado a essa conta. "
                "Altero o código em **M300** (IRPJ) e **M350** (CSLL), e "
                "mostro a prévia antes de aplicar.")

        # Registros colados em bruto têm prioridade sobre a análise textual
        brutos = self.extrair_brutos(texto)
        if brutos:
            return self._prever_lote(texto, brutos, arquivo)

        cmd = self.interpretar(texto)

        # "substituir o bloco do Y570" sem colar os dados → pedir os registros
        if any(g in baixo for g in GATILHOS_SUBSTITUIR) and cmd.registro:
            lr = self.layout.registro(self.versao, cmd.registro)
            if lr:
                exemplo = "|" + lr.registro + "|" + "|".join(
                    f"<{c.nome}>" for c in lr.campos[1:]) + "|"
                return Resposta(
                    f"Para substituir o bloco **{lr.registro}** inteiro, "
                    f"cole aqui as linhas novas (uma por registro) junto com "
                    f"a palavra *substituir*. Eu apago as atuais e insiro as "
                    f"novas na posição correta.\n\n"
                    f"Formato esperado ({lr.num_campos} campos):\n\n"
                    f"```\n{exemplo}\n```\n\n"
                    f"Para lotes grandes, use o campo **Colar lote de "
                    f"registros** logo acima do chat.")

        if not cmd.acao:
            return Resposta(
                "Não entendi o que você precisa. Diga, por exemplo, "
                "`inserir M310 com COD_CTA = 1.01.01.001` ou `o que é o M300?`."
                "\n\nDigite **ajuda** para ver todos os comandos.")

        if cmd.acao == "reparar":
            return Resposta(
                "Vou aplicar o **reparo seguro**: remover duplicatas de "
                "registros únicos e recalcular todos os totalizadores. "
                "Valores de campo não serão inventados.",
                comando=cmd, aplicavel=True)

        if cmd.acao == "recalcular":
            return Resposta(
                "Vou **recalcular todos os totalizadores** "
                "(`X990`, `9900`, `9990`, `9999`).",
                comando=cmd, aplicavel=True)

        if cmd.acao == "consultar":
            return self._consultar(cmd, arquivo)

        if not cmd.registro:
            return Resposta(
                "Preciso saber **qual registro**. Ex.: `inserir M310 com "
                "COD_CTA = 1.01.01.001`.")

        lr = self.layout.registro(self.versao, cmd.registro)
        if not lr:
            return Resposta(
                f"O registro **{cmd.registro}** não existe no leiaute "
                f"{self.versao}. Confira o código no manual.")

        if cmd.acao == "inserir":
            return self._prever_insercao(cmd, lr)
        if cmd.acao == "alterar":
            return self._prever_alteracao(cmd, lr, arquivo)
        if cmd.acao == "remover":
            return self._prever_remocao(cmd, lr, arquivo)
        return Resposta("Não consegui determinar a operação.")

    # ------------------------------------------------------------------ #
    # Consulta ao manual
    # ------------------------------------------------------------------ #
    def _consultar(self, cmd: Comando, arquivo: ArquivoECF) -> Resposta:
        if not cmd.registro:
            return Resposta("Informe o código do registro. Ex.: `o que é o M300?`")
        lr = self.layout.registro(self.versao, cmd.registro)
        if not lr:
            return Resposta(f"Registro **{cmd.registro}** não consta no leiaute.")

        qtd = arquivo.contagem_por_tipo().get(cmd.registro, 0) if arquivo else 0

        # "quantos M350?" merece resposta direta, não a ficha inteira
        if re.search(r"\bquant[oa]s?\b", cmd.texto, re.IGNORECASE):
            return Resposta(
                f"O arquivo tem **{qtd} ocorrência(s)** do registro "
                f"**{lr.registro}** — {lr.nome}.\n\n"
                f"Ocorrência prevista no leiaute: `{lr.ocorrencia or '—'}`.")

        linhas = [
            f"### {lr.registro} — {lr.nome}",
            f"- **Bloco:** {lr.bloco}  •  **Nível:** {lr.nivel}",
            f"- **Obrigatoriedade:** {lr.obrig_entrada or '—'}  •  "
            f"**Ocorrência:** {lr.ocorrencia or '—'}",
            f"- **Campos no leiaute:** {lr.num_campos}",
            f"- **Ocorrências neste arquivo:** {qtd}",
            "",
            "| Nº | Campo | Tipo | Obrigatório |",
            "|---|---|---|---|",
        ]
        for c in lr.campos:
            linhas.append(f"| {c.seq} | {c.nome} | {c.tipo or '—'} | "
                          f"{c.obrigatorio or '—'} |")
        return Resposta("\n".join(linhas))

    # ------------------------------------------------------------------ #
    # Inserção
    # ------------------------------------------------------------------ #
    def _prever_insercao(self, cmd: Comando, lr) -> Resposta:
        desconhecidos = [n for n in cmd.campos
                         if n not in {c.nome.upper() for c in lr.campos}]
        if desconhecidos:
            validos = ", ".join(c.nome for c in lr.campos[1:])
            return Resposta(
                f"O(s) campo(s) **{', '.join(desconhecidos)}** não existe(m) no "
                f"{lr.registro}.\n\nCampos válidos: {validos}")

        # monta o registro com o número de campos do leiaute (estrutura correta)
        novo = self._montar(lr, cmd.campos)

        faltando = [c.nome for c in lr.campos
                    if c.obrigatorio == "Sim" and c.seq > 1
                    and novo.campo(c.seq - 1).strip() == ""]
        if faltando:
            return Resposta(
                f"Para inserir o **{lr.registro}** faltam campos obrigatórios: "
                f"**{', '.join(faltando)}**.\n\nInforme assim: "
                f"`inserir {lr.registro} com "
                f"{faltando[0]} = <valor>`.\n\n*Não vou preenchê-los por conta "
                f"própria — em escrituração fiscal isso seria pior que o erro.*")

        return Resposta(
            f"Vou inserir **1 registro {lr.registro}** ({lr.nome}) com "
            f"{lr.num_campos} campos, na posição correta do bloco "
            f"**{lr.bloco}**, e recalcular os totalizadores.",
            comando=cmd, aplicavel=True, alvos=1,
            previa=[("(novo)", novo.para_linha())])

    def _montar(self, lr, valores: Dict[str, str]) -> Registro:
        campos = [""] * max(lr.num_campos, 1)
        campos[0] = lr.registro
        for c in lr.campos:
            v = valores.get(c.nome.upper())
            if v is not None and c.seq - 1 < len(campos):
                campos[c.seq - 1] = v
        return Registro(campos=campos)

    # ------------------------------------------------------------------ #
    # Alteração
    # ------------------------------------------------------------------ #
    def _prever_alteracao(self, cmd: Comando, lr,
                          arquivo: ArquivoECF) -> Resposta:
        if not cmd.campos:
            return Resposta(
                f"Diga qual campo alterar e o novo valor. Ex.: "
                f"`no {lr.registro}, alterar {lr.campos[1].nome if len(lr.campos)>1 else 'CAMPO'} "
                f"para <valor>`.")

        mapa = {c.nome.upper(): c for c in lr.campos}
        desconhecidos = [n for n in cmd.campos if n not in mapa]
        if desconhecidos:
            return Resposta(
                f"Campo(s) inexistente(s) no {lr.registro}: "
                f"**{', '.join(desconhecidos)}**.\n\nVálidos: "
                f"{', '.join(c.nome for c in lr.campos)}")

        alvos = self._selecionar(cmd, lr, arquivo)
        if not alvos:
            return Resposta(
                f"Nenhum registro **{lr.registro}** corresponde ao pedido"
                + (f" com filtro {cmd.filtro}." if cmd.filtro else " no arquivo."))

        previa = []
        for r in alvos[:MAX_PREVIA]:
            antes = r.para_linha()
            copia = Registro(campos=list(r.campos))
            for nome, valor in cmd.campos.items():
                copia.set_campo(mapa[nome].seq - 1, valor)
            previa.append((antes, copia.para_linha()))

        alvo_txt = (f"**{len(alvos)} registro(s) {lr.registro}**"
                    if len(alvos) > 1 else f"**1 registro {lr.registro}**")
        aviso = ("\n\n⚠️ São muitos registros — confira a prévia com atenção."
                 if len(alvos) > 1 else "")
        return Resposta(
            f"Vou alterar {alvo_txt}: "
            + ", ".join(f"`{k}` → `{v}`" for k, v in cmd.campos.items())
            + aviso,
            comando=cmd, aplicavel=True, alvos=len(alvos), previa=previa)

    # ------------------------------------------------------------------ #
    # Remoção
    # ------------------------------------------------------------------ #
    def _prever_remocao(self, cmd: Comando, lr,
                        arquivo: ArquivoECF) -> Resposta:
        if lr.abertura or lr.encerramento:
            return Resposta(
                f"**{lr.registro}** é registro de abertura/encerramento de "
                f"bloco. Removê-lo quebraria a estrutura — não farei isso.")

        alvos = self._selecionar(cmd, lr, arquivo)
        if not alvos:
            return Resposta(f"Nenhum registro **{lr.registro}** encontrado "
                            f"com esse critério.")

        previa = [(r.para_linha(), "(removido)") for r in alvos[:MAX_PREVIA]]
        return Resposta(
            f"Vou remover **{len(alvos)} registro(s) {lr.registro}** e "
            f"recalcular os totalizadores.\n\n⚠️ Esta ação apaga dados — "
            f"confira a prévia antes de confirmar.",
            comando=cmd, aplicavel=True, alvos=len(alvos), previa=previa)

    # ------------------------------------------------------------------ #
    # Seleção de alvos
    # ------------------------------------------------------------------ #
    def _selecionar(self, cmd: Comando, lr,
                    arquivo: ArquivoECF) -> List[Registro]:
        mapa = {c.nome.upper(): c for c in lr.campos}
        alvos = [r for r in arquivo.registros if r.reg == cmd.registro]

        for nome, valor in cmd.filtro.items():
            c = mapa.get(nome)
            if not c:
                continue
            i = c.seq - 1
            alvos = [r for r in alvos
                     if i < r.num_campos and r.campo(i).strip() == valor.strip()]

        if cmd.indice is not None:
            k = cmd.indice - 1
            alvos = [alvos[k]] if 0 <= k < len(alvos) else []
        return alvos

    # ------------------------------------------------------------------ #
    # Aplicação (só após confirmação do usuário)
    # ------------------------------------------------------------------ #
    def aplicar(self, cmd: Comando, arquivo: ArquivoECF) -> Tuple[str, bool]:
        """Executa o comando. Retorna (mensagem, precisa_recontar)."""
        lr = self.layout.registro(self.versao, cmd.registro) \
            if cmd.registro else None

        if cmd.acao == "alterar" and lr:
            mapa = {c.nome.upper(): c for c in lr.campos}
            alvos = self._selecionar(cmd, lr, arquivo)
            for r in alvos:
                for nome, valor in cmd.campos.items():
                    r.set_campo(mapa[nome].seq - 1, valor)
            return (f"{len(alvos)} registro(s) {cmd.registro} alterado(s).",
                    True)

        if cmd.acao == "remover" and lr:
            alvos = set(id(r) for r in self._selecionar(cmd, lr, arquivo))
            antes = len(arquivo.registros)
            arquivo.registros = [r for r in arquivo.registros
                                 if id(r) not in alvos]
            return (f"{antes - len(arquivo.registros)} registro(s) "
                    f"{cmd.registro} removido(s).", True)

        return ("Nada a aplicar.", False)

    def registro_para_inserir(self, cmd: Comando) -> Optional[Registro]:
        """Monta o registro da ação 'inserir' para a engine de inserção."""
        lr = self.layout.registro(self.versao, cmd.registro)
        return self._montar(lr, cmd.campos) if lr else None
