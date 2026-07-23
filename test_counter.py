"""Modelo de um registro individual do SPED ECF.

Uma linha do arquivo ECF tem o formato ``|CAMPO1|CAMPO2|...|CAMPON|``.
Ao separar por ``|`` obtemos ``['', c1, c2, ..., cn, '']``; portanto os
campos úteis são ``partes[1:-1]`` e ``campos[0]`` é sempre o código do
registro (REG).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Registro:
    """Representa um único registro (linha) da ECF.

    Attributes:
        campos: lista de valores dos campos, incluindo o REG na posição 0.
        origem: número (1-based) da linha no arquivo original, ou None se
            o registro foi inserido pela ferramenta.
    """

    campos: List[str] = field(default_factory=list)
    origem: int | None = None

    # ------------------------------------------------------------------ #
    # Fábricas
    # ------------------------------------------------------------------ #
    @classmethod
    def de_linha(cls, linha: str, origem: int | None = None) -> "Registro":
        """Constrói um Registro a partir de uma linha crua do TXT."""
        partes = linha.split("|")
        # Remove o primeiro e o último elemento vazios (bordas dos pipes).
        if partes and partes[0] == "":
            partes = partes[1:]
        if partes and partes[-1] == "":
            partes = partes[:-1]
        return cls(campos=partes, origem=origem)

    # ------------------------------------------------------------------ #
    # Propriedades
    # ------------------------------------------------------------------ #
    @property
    def reg(self) -> str:
        """Código do registro (ex.: '0000', 'M300')."""
        return self.campos[0] if self.campos else ""

    @property
    def bloco(self) -> str:
        """Letra/dígito do bloco (primeiro caractere do REG)."""
        return self.reg[0] if self.reg else ""

    @property
    def num_campos(self) -> int:
        """Quantidade de campos (inclui o REG)."""
        return len(self.campos)

    def campo(self, indice: int) -> str:
        """Retorna o valor do campo pelo índice (0 = REG)."""
        return self.campos[indice] if 0 <= indice < len(self.campos) else ""

    def set_campo(self, indice: int, valor: str) -> None:
        while len(self.campos) <= indice:
            self.campos.append("")
        self.campos[indice] = valor

    # ------------------------------------------------------------------ #
    # Serialização
    # ------------------------------------------------------------------ #
    def para_linha(self) -> str:
        """Reconstrói a linha no formato SPED (``|...|``)."""
        return "|" + "|".join(self.campos) + "|"

    def __str__(self) -> str:  # pragma: no cover - conveniência
        return self.para_linha()
