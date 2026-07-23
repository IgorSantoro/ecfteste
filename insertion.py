"""Controlador da aplicação (camada C do MVC).

Fachada de alto nível que orquestra parser, leiaute, validação, inserção,
totalizadores e exportação. A UI e a CLI conversam apenas com esta classe.
"""
from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass, field
from typing import Callable, List, Optional

from .core import (
    Assistente,
    Comando,
    Contador,
    Exportador,
    Hierarquia,
    InsercaoInteligente,
    LayoutLoader,
    LeitorReclass,
    Ocorrencia,
    ParserECF,
    Reclassificador,
    Reparador,
    Resposta,
    ResultadoReclass,
    ResultadoReparo,
    Validador,
)
from .models import ArquivoECF, Registro

log = logging.getLogger("editor_ecf")


@dataclass
class RelatorioOperacao:
    adicionados: List[str] = field(default_factory=list)
    ignorados: List[tuple] = field(default_factory=list)
    erros: List[Ocorrencia] = field(default_factory=list)
    totalizadores: List[str] = field(default_factory=list)
    tempo_seg: float = 0.0
    total_linhas: int = 0


class ControladorECF:
    def __init__(self, pasta_layouts: str, pasta_logs: str = "logs") -> None:
        self.layout = LayoutLoader(pasta_layouts)
        self.parser = ParserECF()
        self.exportador = Exportador()
        self.arquivo: Optional[ArquivoECF] = None
        self.versao: str = self.layout.versao_padrao()
        self._config_log(pasta_logs)

    # ------------------------------------------------------------------ #
    def _config_log(self, pasta_logs: str) -> None:
        os.makedirs(pasta_logs, exist_ok=True)
        if not log.handlers:
            log.setLevel(logging.INFO)
            fh = logging.FileHandler(os.path.join(pasta_logs, "editor_ecf.log"),
                                     encoding="utf-8")
            fh.setFormatter(logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"))
            log.addHandler(fh)

    # ------------------------------------------------------------------ #
    # Importação
    # ------------------------------------------------------------------ #
    def importar(self, caminho: str) -> ArquivoECF:
        t0 = time.perf_counter()
        self.arquivo = self.parser.ler(caminho)
        return self._pos_importar(caminho, t0)

    def importar_bytes(self, bruto: bytes, nome: str = "upload") -> ArquivoECF:
        t0 = time.perf_counter()
        self.arquivo = self.parser.ler_bytes(bruto, caminho_original=nome)
        return self._pos_importar(nome, t0)

    def _pos_importar(self, ref: str, t0: float) -> ArquivoECF:
        v = self.arquivo.metadados.versao_leiaute
        if v and v in self.layout.versoes:
            self.versao = v
        dt = time.perf_counter() - t0
        log.info("Importado %s | %d linhas | versão %s | %.3fs",
                 os.path.basename(ref), self.arquivo.total_linhas,
                 self.versao, dt)
        return self.arquivo

    # ------------------------------------------------------------------ #
    # Inserção + revalidação + recontagem
    # ------------------------------------------------------------------ #
    def inserir_texto(self, texto: str) -> RelatorioOperacao:
        novos = self.parser.ler_texto(texto)
        return self.inserir_registros(novos)

    def inserir_registros(self, novos: List[Registro]) -> RelatorioOperacao:
        assert self.arquivo is not None, "Nenhuma ECF importada."
        t0 = time.perf_counter()
        rel = RelatorioOperacao()

        validador = Validador(self.layout, self.versao)
        # 1) valida candidatos
        erros = [o for o in validador.validar_novos(novos, self.arquivo)
                 if o.nivel.value == "ERRO"]
        rel.erros = validador.validar_novos(novos, self.arquivo)
        if erros:
            log.warning("Inserção abortada: %d erro(s) de validação.", len(erros))
            rel.tempo_seg = time.perf_counter() - t0
            return rel

        # 2) insere de forma inteligente
        insercao = InsercaoInteligente(self.layout, self.versao)
        res = insercao.inserir(self.arquivo, novos)
        rel.adicionados = res.inseridos
        rel.ignorados = res.ignorados

        # 3) recalcula totalizadores
        cont = Contador().recalcular(self.arquivo,
                                     self.layout.ordem_registros(self.versao))
        rel.totalizadores = cont.totalizadores_atualizados
        rel.total_linhas = cont.total_linhas
        self.arquivo.atualizar_metadados_do_0000()

        rel.tempo_seg = time.perf_counter() - t0
        log.info("Inseridos %d | ignorados %d | totalizadores %s | %.3fs",
                 len(rel.adicionados), len(rel.ignorados),
                 ",".join(rel.totalizadores), rel.tempo_seg)
        return rel

    # ------------------------------------------------------------------ #
    # Recontagem avulsa
    # ------------------------------------------------------------------ #
    def recalcular_totalizadores(self) -> RelatorioOperacao:
        assert self.arquivo is not None
        t0 = time.perf_counter()
        cont = Contador().recalcular(self.arquivo,
                                     self.layout.ordem_registros(self.versao))
        rel = RelatorioOperacao(totalizadores=cont.totalizadores_atualizados,
                                total_linhas=cont.total_linhas)
        rel.tempo_seg = time.perf_counter() - t0
        return rel

    # ------------------------------------------------------------------ #
    # Assistente de comandos em linguagem natural
    # ------------------------------------------------------------------ #
    def assistente(self) -> Assistente:
        return Assistente(self.layout, self.versao)

    def chat_processar(self, texto: str) -> Resposta:
        """Interpreta o pedido e devolve a prévia — não aplica nada."""
        assert self.arquivo is not None
        return self.assistente().processar(texto, self.arquivo)

    def chat_aplicar(self, cmd: Comando) -> str:
        """Executa o comando já confirmado pelo usuário."""
        assert self.arquivo is not None
        if cmd is None or not cmd.acao:
            return "Nenhuma operação pendente para aplicar."
        ass = self.assistente()

        if cmd.acao == "reparar":
            res = self.reparar()
            return (f"Reparo aplicado: "
                    f"{len(res.duplicatas_removidas)} tipo(s) de duplicata "
                    f"removido(s), {len(res.totalizadores)} totalizadores "
                    f"atualizados, {res.total_linhas} linhas. "
                    f"{len(res.pendencias)} pendência(s) de conteúdo.")

        if cmd.acao == "recalcular":
            rel = self.recalcular_totalizadores()
            return (f"Totalizadores recalculados: "
                    f"{', '.join(rel.totalizadores)} — "
                    f"{rel.total_linhas} linhas.")

        if cmd.acao in ("lote_inserir", "lote_substituir"):
            return self._chat_lote(cmd)

        if cmd.acao == "inserir":
            novo = ass.registro_para_inserir(cmd)
            if novo is None:
                return "Não foi possível montar o registro."
            rel = self.inserir_registros([novo])
            if not rel.adicionados:
                motivos = "; ".join(m for _, m in rel.ignorados) or \
                    "; ".join(o.mensagem for o in rel.erros)
                return f"Inserção não realizada. {motivos}"
            return (f"Registro {cmd.registro} inserido na posição correta. "
                    f"Totalizadores atualizados; "
                    f"total de {rel.total_linhas} linhas.")

        msg, recontar = ass.aplicar(cmd, self.arquivo)
        if recontar:
            rel = self.recalcular_totalizadores()
            msg += f" Totalizadores atualizados ({rel.total_linhas} linhas)."
        log.info("Chat: %s | %s", cmd.acao, msg)
        return msg

    def _chat_lote(self, cmd: Comando) -> str:
        """Insere (ou substitui) um lote de registros colados."""
        assert self.arquivo is not None
        t0 = time.perf_counter()
        tipos = sorted({r.reg for r in cmd.registros})
        removidos = 0

        if cmd.acao == "lote_substituir":
            antes = len(self.arquivo.registros)
            self.arquivo.registros = [r for r in self.arquivo.registros
                                      if r.reg not in tipos]
            removidos = antes - len(self.arquivo.registros)

        rel = self.inserir_registros(cmd.registros)
        dt = time.perf_counter() - t0

        partes = []
        if removidos:
            partes.append(f"{removidos} registro(s) anterior(es) removido(s)")
        partes.append(f"{len(rel.adicionados)} inserido(s)")
        if rel.ignorados:
            partes.append(f"{len(rel.ignorados)} ignorado(s)")
        msg = (f"{'; '.join(partes)}. Totalizadores atualizados — "
               f"{rel.total_linhas} linhas. ({dt:.2f}s)")
        log.info("Chat lote: %s | %s", cmd.acao, msg)
        return msg

    # ------------------------------------------------------------------ #
    # Reclassificação de códigos (M300 / M350)
    # ------------------------------------------------------------------ #
    def reclass_ler_planilha(self, dados, colunas=None, aba=None):
        """Lê a planilha De→Para. Retorna (regras, avisos)."""
        return LeitorReclass(colunas).ler(dados, aba=aba)

    def reclass_previa(self, regras, alterar_descricao: bool = False
                       ) -> ResultadoReclass:
        assert self.arquivo is not None
        return Reclassificador(alterar_descricao).previa(self.arquivo, regras)

    def reclass_aplicar(self, res: ResultadoReclass,
                        alterar_descricao: bool = False) -> str:
        assert self.arquivo is not None
        t0 = time.perf_counter()
        n = Reclassificador(alterar_descricao).aplicar(self.arquivo, res)
        rel = self.recalcular_totalizadores()
        msg = (f"{n} lançamento(s) reclassificado(s) em M300/M350. "
               f"Totalizadores conferidos — {rel.total_linhas} linhas. "
               f"({time.perf_counter() - t0:.2f}s)")
        log.info("Reclassificação: %s", msg)
        return msg

    def reparar(self) -> "ResultadoReparo":
        assert self.arquivo is not None
        t0 = time.perf_counter()
        res = Reparador(self.layout, self.versao).reparar(self.arquivo)
        log.info("Reparo: %d tipo(s) de duplicata removidos | "
                 "totalizadores %s | %d pendência(s) | %.3fs",
                 len(res.duplicatas_removidas),
                 ",".join(res.totalizadores), len(res.pendencias),
                 time.perf_counter() - t0)
        return res

    # ------------------------------------------------------------------ #
    # Validação global
    # ------------------------------------------------------------------ #
    def validar(self) -> List[Ocorrencia]:
        assert self.arquivo is not None
        return Validador(self.layout, self.versao,
                         obrig_como_erro=False).validar(self.arquivo)

    # ------------------------------------------------------------------ #
    # Árvore de exibição
    # ------------------------------------------------------------------ #
    def montar_arvore(self) -> dict:
        assert self.arquivo is not None
        return Hierarquia(self.layout, self.versao).montar_arvore(self.arquivo)

    def info_registro(self, reg: str) -> dict:
        lr = self.layout.registro(self.versao, reg)
        qtd = self.arquivo.contagem_por_tipo().get(reg, 0) if self.arquivo else 0
        if not lr:
            return {"reg": reg, "nome": "", "qtd": qtd, "campos": [], "nivel": None,
                    "ocorrencia": "", "obrig": ""}
        return {
            "reg": reg, "nome": lr.nome, "qtd": qtd, "nivel": lr.nivel,
            "ocorrencia": lr.ocorrencia, "obrig": lr.obrig_entrada,
            "campos": [{"seq": c.seq, "nome": c.nome, "tipo": c.tipo,
                        "obrig": c.obrigatorio} for c in lr.campos],
        }

    # ------------------------------------------------------------------ #
    # Exportação
    # ------------------------------------------------------------------ #
    def exportar(self, caminho: str) -> int:
        assert self.arquivo is not None
        n = self.exportador.exportar(self.arquivo, caminho)
        log.info("Exportado %s | %d linhas", os.path.basename(caminho), n)
        return n

    def exportar_bytes(self) -> bytes:
        assert self.arquivo is not None
        return self.exportador.para_bytes(self.arquivo)

    # ------------------------------------------------------------------ #
    # Painel / dashboard
    # ------------------------------------------------------------------ #
    def dados_painel(self) -> dict:
        if not self.arquivo:
            return {}
        m = self.arquivo.metadados
        return {
            "empresa": m.razao_social,
            "cnpj": self._formatar_cnpj(m.cnpj),
            "periodo": f"{self._data(m.dt_inicial)} a {self._data(m.dt_final)}",
            "versao": m.versao_leiaute,
            "linhas": self.arquivo.total_linhas,
            "blocos": self.arquivo.blocos_presentes(),
            "tipos": len(self.arquivo.contagem_por_tipo()),
            "descricao_leiaute": self.layout.descricao(self.versao),
        }

    @staticmethod
    def _formatar_cnpj(c: str) -> str:
        c = (c or "").zfill(14)
        if len(c) != 14:
            return c
        return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}"

    @staticmethod
    def _data(d: str) -> str:
        return f"{d[:2]}/{d[2:4]}/{d[4:]}" if d and len(d) == 8 else d
