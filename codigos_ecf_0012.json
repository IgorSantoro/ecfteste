"""Reparo automático seguro da estrutura da ECF.

Filosofia: só corrigir automaticamente o que é **determinístico e não
destrutivo**. Nunca inventar valores de campo. As correções aplicadas são:

  1. Remoção de duplicatas de registros que o leiaute define como **únicos**
     (ocorrência ``[1;1]``) — mantém a primeira ocorrência e descarta as
     repetições idênticas.
  2. Remoção de linhas 100% idênticas (mesmo REG e mesmos campos) que sejam
     de registros únicos.
  3. Recálculo de **todos os totalizadores** (``X990``, ``9900``, ``9990``,
     ``9999``) — a correção mais comum e sempre segura.

O que **não** é corrigido automaticamente (exige decisão do usuário) é
listado em ``pendencias``: valores de campo obrigatório ausentes e quantidade
de campos divergente do leiaute — porque não há como adivinhar o valor certo
sem risco de corromper a escrituração.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

from ..models import ArquivoECF, Registro
from .counter import Contador
from .layout_loader import LayoutLoader
from .validator import Nivel, Validador


@dataclass
class ResultadoReparo:
    duplicatas_removidas: List[Tuple[str, int]] = field(default_factory=list)
    totalizadores: List[str] = field(default_factory=list)
    total_linhas: int = 0
    pendencias: List[str] = field(default_factory=list)  # não auto-corrigíveis


class Reparador:
    """Aplica correções seguras e devolve um relatório do que foi feito."""

    def __init__(self, layout: LayoutLoader, versao: str) -> None:
        self.layout = layout
        self.versao = versao

    # ------------------------------------------------------------------ #
    def reparar(self, arquivo: ArquivoECF) -> ResultadoReparo:
        res = ResultadoReparo()

        # 1) Remove duplicatas de registros ÚNICOS (mantém a 1ª ocorrência).
        res.duplicatas_removidas = self._remover_duplicatas_unicas(arquivo)

        # 2) Recalcula todos os totalizadores.
        cont = Contador().recalcular(
            arquivo, self.layout.ordem_registros(self.versao))
        res.totalizadores = cont.totalizadores_atualizados
        res.total_linhas = cont.total_linhas
        arquivo.atualizar_metadados_do_0000()

        # 3) Lista pendências que NÃO podem ser corrigidas sem inventar dados.
        res.pendencias = self._pendencias_nao_corrigiveis(arquivo)
        return res

    # ------------------------------------------------------------------ #
    def _remover_duplicatas_unicas(
        self, arquivo: ArquivoECF
    ) -> List[Tuple[str, int]]:
        """Remove repetições de registros de ocorrência única [1;1].

        Só remove quando a repetição é **idêntica** à primeira (mesmo
        conteúdo), evitando descartar dados diferentes por engano.
        """
        vistos: dict[str, str] = {}          # reg -> assinatura da 1ª ocorrência
        contagem: dict[str, int] = {}
        manter: List[Registro] = []
        removidos: dict[str, int] = {}

        for r in arquivo.registros:
            lr = self.layout.registro(self.versao, r.reg)
            unico = bool(lr and lr.unico)
            if not unico:
                manter.append(r)
                continue

            assinatura = "|".join(r.campos)
            if r.reg not in vistos:
                vistos[r.reg] = assinatura
                manter.append(r)
            else:
                # já existe uma ocorrência: só remove se for idêntica
                if assinatura == vistos[r.reg]:
                    removidos[r.reg] = removidos.get(r.reg, 0) + 1
                else:
                    # conteúdo diferente: mantém, mas será sinalizado depois
                    manter.append(r)

        arquivo.registros = manter
        return sorted(removidos.items())

    # ------------------------------------------------------------------ #
    def _pendencias_nao_corrigiveis(self, arquivo: ArquivoECF) -> List[str]:
        """Roda a validação e retorna, em texto, o que exige o usuário."""
        val = Validador(self.layout, self.versao, obrig_como_erro=True)
        msgs: List[str] = []

        # duplicatas de únicos com conteúdo DIVERGENTE (não removidas)
        contagem: dict[str, int] = {}
        for r in arquivo.registros:
            lr = self.layout.registro(self.versao, r.reg)
            if lr and lr.unico:
                contagem[r.reg] = contagem.get(r.reg, 0) + 1
        for reg, q in contagem.items():
            if q > 1:
                msgs.append(
                    f"{reg}: {q} ocorrências de um registro único com conteúdos "
                    f"diferentes — resolva manualmente qual manter.")

        # quantidade de campos divergente e obrigatórios vazios
        from .validator import ValidateFields, ValidateObrigatorios
        for regra in (ValidateFields(self.layout, self.versao),
                      ValidateObrigatorios(self.layout, self.versao,
                                           severidade=Nivel.ERRO)):
            for o in regra.validar(arquivo):
                msgs.append(f"{o.registro}: {o.mensagem}")

        # remove repetições de mensagem, preservando ordem
        vistos = set()
        unicas = []
        for m in msgs:
            if m not in vistos:
                vistos.add(m)
                unicas.append(m)
        return unicas
