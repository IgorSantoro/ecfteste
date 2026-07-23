"""Modelo do arquivo ECF inteiro: a "árvore em memória"."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from .bloco import Bloco
from .registro import Registro


@dataclass
class MetadadosECF:
    """Metadados extraídos do registro 0000."""

    versao_leiaute: str = ""
    cnpj: str = ""
    razao_social: str = ""
    nome_sped: str = ""
    dt_inicial: str = ""
    dt_final: str = ""
    ind_sit_ini: str = ""
    sit_especial: str = ""


@dataclass
class ArquivoECF:
    """Representa toda a ECF em memória.

    A *fonte da verdade* é ``registros`` (lista ordenada). Blocos e índices
    são visões derivadas, reconstruídas sob demanda.
    """

    registros: List[Registro] = field(default_factory=list)
    metadados: MetadadosECF = field(default_factory=MetadadosECF)
    encoding: str = "latin-1"
    nova_linha: str = "\r\n"
    caminho_original: str = ""

    # ------------------------------------------------------------------ #
    # Estatísticas / visões
    # ------------------------------------------------------------------ #
    @property
    def total_linhas(self) -> int:
        return len(self.registros)

    def contagem_por_tipo(self) -> Dict[str, int]:
        contagem: Dict[str, int] = {}
        for r in self.registros:
            contagem[r.reg] = contagem.get(r.reg, 0) + 1
        return contagem

    def blocos_presentes(self) -> List[str]:
        vistos: List[str] = []
        for r in self.registros:
            if r.bloco and r.bloco not in vistos:
                vistos.append(r.bloco)
        return vistos

    def montar_blocos(self) -> List[Bloco]:
        """Agrupa os registros em objetos Bloco preservando a ordem."""
        mapa: Dict[str, Bloco] = {}
        ordem: List[str] = []
        for r in self.registros:
            b = r.bloco
            if b not in mapa:
                mapa[b] = Bloco(letra=b)
                ordem.append(b)
            mapa[b].registros.append(r)
        return [mapa[b] for b in ordem]

    def registros_do_tipo(self, reg: str) -> List[Registro]:
        return [r for r in self.registros if r.reg == reg]

    # ------------------------------------------------------------------ #
    # Metadados
    # ------------------------------------------------------------------ #
    def atualizar_metadados_do_0000(self) -> None:
        r0000 = next((r for r in self.registros if r.reg == "0000"), None)
        if not r0000:
            return
        c = r0000.campos
        g = lambda i: c[i] if i < len(c) else ""
        self.metadados = MetadadosECF(
            nome_sped=g(1),
            versao_leiaute=g(2),
            cnpj=g(3),
            razao_social=g(4),
            ind_sit_ini=g(5),
            sit_especial=g(6),
            dt_inicial=g(9),
            dt_final=g(10),
        )
