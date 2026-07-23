"""Motor de Totalizadores.

Recalcula automaticamente todos os totalizadores da ECF de modo idêntico
ao PVA da Receita:

  * ``X990`` (0990, C990, ... Y990): quantidade de registros do bloco X,
    incluindo a abertura (X001 / 0000) e o encerramento (X990).
  * Bloco 9:
      - ``9900|REG|QTD``: uma linha por tipo de registro existente no
        arquivo inteiro, com a quantidade de ocorrências.
      - ``9990``: total de registros do bloco 9.
      - ``9999``: total de linhas (registros) do arquivo inteiro.

Regra de ordenação do 9900 (verificada contra arquivos reais): ordem de
primeira aparição de todos os tipos, exceto o próprio 9900, que é
acrescentado por último — após 9990 e 9999.

O registro 9100 (mensagens de validação geradas pelo PVA) é *preservado*
como está: a ferramenta não altera nem recria essas ocorrências, apenas
as contabiliza nos totais.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from ..models import ArquivoECF, Registro

BLOCO9_CONTROLE = {"9001", "9900", "9990", "9999"}


@dataclass
class ResultadoContagem:
    totalizadores_atualizados: List[str]
    total_linhas: int


class Contador:
    def recalcular(
        self, arquivo: ArquivoECF, ordem_canonica: List[str] | None = None
    ) -> ResultadoContagem:
        """Recalcula todos os totalizadores.

        Args:
            arquivo: a ECF em memória (modificada in-place).
            ordem_canonica: ordem oficial dos registros no leiaute
                (``ordem_registros`` do JSON). Usada para ordenar as linhas
                9900 exatamente como o PVA. Se ausente, usa a ordem de
                primeira aparição.
        """
        atualizados: List[str] = []
        indice = {reg: i for i, reg in enumerate(ordem_canonica or [])}

        # 1) Separa registros de dados (blocos 0..Y) dos de controle do bloco 9.
        #    Preserva os campos 4/5 (VERSAO, ID_TAB_DIN) das linhas 9900 já
        #    existentes, para que a recontagem não perca marcadores do PVA.
        dados: List[Registro] = []
        r9100: List[Registro] = []
        extras_9900: Dict[str, tuple] = {}
        for r in arquivo.registros:
            if r.reg == "9100":
                r9100.append(r)
            elif r.reg == "9900":
                if len(r.campos) >= 3:
                    reg_blc = r.campos[1]
                    versao = r.campos[3] if len(r.campos) > 3 else ""
                    id_tab = r.campos[4] if len(r.campos) > 4 else ""
                    extras_9900[reg_blc] = (versao, id_tab)
                continue  # descartado; será reconstruído
            elif r.reg in BLOCO9_CONTROLE:
                continue  # descartados; serão reconstruídos
            else:
                dados.append(r)

        # 2) Recalcula os encerradores de bloco X990 (blocos 0..Y).
        contagem_bloco: Dict[str, int] = {}
        for r in dados:
            contagem_bloco[r.bloco] = contagem_bloco.get(r.bloco, 0) + 1
        for r in dados:
            if r.reg.endswith("990") and r.bloco != "9":
                r.set_campo(1, str(contagem_bloco[r.bloco]))
                atualizados.append(r.reg)

        # 3) Reconstrói o Bloco 9.
        #    base = dados (já com X990 corrigidos) + 9100 preservados
        base = dados + r9100

        # 3a) Ordem das linhas 9900:
        #     tipos de dados (blocos 0..Y) na ORDEM CANÔNICA do leiaute,
        #     seguidos pelo bloco 9 na ordem fixa: 9001, 9100, 9990, 9999, 9900.
        tipos_dados = []
        vistos = set()
        for r in dados:
            if r.reg not in vistos:
                vistos.add(r.reg)
                tipos_dados.append(r.reg)
        # ordenação estável pela posição canônica (desconhecidos ao fim)
        tipos_dados.sort(key=lambda reg: (indice.get(reg, 10**9),))

        ordem_tipos: List[str] = list(tipos_dados)
        ordem_tipos.append("9001")
        if r9100:
            ordem_tipos.append("9100")
        ordem_tipos += ["9990", "9999", "9900"]

        # 3b) Contagem de ocorrências de cada tipo no arquivo final.
        cont: Dict[str, int] = {}
        for r in base:
            cont[r.reg] = cont.get(r.reg, 0) + 1
        cont["9001"] = 1
        cont["9990"] = 1
        cont["9999"] = 1
        cont["9900"] = len(ordem_tipos)  # uma linha 9900 por tipo

        # 3c) Monta as linhas do bloco 9.
        r9001 = Registro(campos=["9001", "0"])
        linhas_9900 = [
            Registro(campos=["9900", reg, str(cont[reg]),
                             extras_9900.get(reg, ("", ""))[0],
                             extras_9900.get(reg, ("", ""))[1]])
            for reg in ordem_tipos
        ]
        # total do bloco 9 = 9001 + (9100...) + (9900...) + 9990 + 9999
        total_bloco9 = 1 + len(r9100) + len(linhas_9900) + 1 + 1
        r9990 = Registro(campos=["9990", str(total_bloco9)])

        # total do arquivo = registros de dados (0..Y) + total do bloco 9
        total_arquivo = len(dados) + total_bloco9
        r9999 = Registro(campos=["9999", str(total_arquivo)])

        bloco9 = [r9001, *r9100, *linhas_9900, r9990, r9999]
        atualizados += ["9001", "9900", "9990", "9999"]

        # 4) Recompõe a lista: blocos de dados (na ordem) + bloco 9 ao final.
        arquivo.registros = list(dados) + list(bloco9)

        return ResultadoContagem(
            totalizadores_atualizados=sorted(set(atualizados)),
            total_linhas=total_arquivo,
        )
