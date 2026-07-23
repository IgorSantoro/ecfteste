"""Modelo de um bloco lógico da ECF (0, C, E, J, K, L, M, N, ... 9)."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .registro import Registro


@dataclass
class Bloco:
    """Agrupa os registros de um mesmo bloco para fins de visualização."""

    letra: str
    registros: List[Registro] = field(default_factory=list)

    @property
    def total_registros(self) -> int:
        return len(self.registros)

    @property
    def registro_abertura(self) -> Registro | None:
        for r in self.registros:
            if r.reg.endswith("001") or r.reg == "0000":
                return r
        return None

    @property
    def registro_encerramento(self) -> Registro | None:
        for r in self.registros:
            if r.reg.endswith("990"):
                return r
        return None

    def contagem_por_tipo(self) -> dict[str, int]:
        """Retorna {REG: quantidade} para os registros do bloco."""
        contagem: dict[str, int] = {}
        for r in self.registros:
            contagem[r.reg] = contagem.get(r.reg, 0) + 1
        return contagem
