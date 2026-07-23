"""Motor de Leiaute.

Carrega a definição da ECF a partir de arquivos JSON (um por versão do
leiaute). Nenhuma regra estrutural é fixada em código: para suportar uma
nova versão da ECF basta acrescentar/substituir o JSON correspondente em
``/layouts``.

O JSON é gerado a partir do Manual de Orientação do Leiaute da ECF
(Tabela de Registros + Leiaute dos Registros) e contém, por registro:
nível hierárquico, obrigatoriedade de entrada, ocorrência, se é abertura
ou encerramento de bloco, número de campos e a lista de campos.
"""
from __future__ import annotations

import glob
import json
import os
import re
from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class CampoLayout:
    seq: int
    nome: str
    tipo: str = ""          # 'C' (texto) ou 'N' (numérico)
    obrigatorio: str = ""   # 'Sim' / 'Não' / ''


@dataclass
class LayoutRegistro:
    registro: str
    bloco: str
    nivel: int
    nome: str
    obrig_entrada: str
    ocorrencia: str
    abertura: bool
    encerramento: bool
    num_campos: int
    campos: List[CampoLayout] = field(default_factory=list)

    # ------ ocorrência ------
    @property
    def ocorrencia_max(self) -> int | None:
        """Máximo de ocorrências. ``None`` significa ilimitado (N)."""
        m = re.search(r"[;:]\s*([0-9N]+)\s*\]", self.ocorrencia)
        if not m:
            return None
        v = m.group(1)
        return None if v.upper() == "N" else int(v)

    @property
    def unico(self) -> bool:
        """True se o registro só pode ocorrer uma vez (ex.: [1;1])."""
        return self.ocorrencia_max == 1


class LayoutLoader:
    """Carrega e indexa os leiautes disponíveis."""

    def __init__(self, pasta_layouts: str) -> None:
        self.pasta = pasta_layouts
        self._layouts: Dict[str, Dict] = {}          # versao -> json bruto
        self._registros: Dict[str, Dict[str, LayoutRegistro]] = {}
        self._ordem: Dict[str, List[str]] = {}
        self._carregar_todos()

    # ------------------------------------------------------------------ #
    def _carregar_todos(self) -> None:
        for caminho in sorted(glob.glob(os.path.join(self.pasta, "ecf_*.json"))):
            try:
                dados = json.load(open(caminho, encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            versao = str(dados.get("versao", os.path.basename(caminho)))
            self._layouts[versao] = dados
            regs: Dict[str, LayoutRegistro] = {}
            for cod, rd in dados.get("registros", {}).items():
                campos = [
                    CampoLayout(
                        seq=c.get("seq", i + 1),
                        nome=c.get("nome", f"CAMPO_{i+1}"),
                        tipo=c.get("tipo", ""),
                        obrigatorio=c.get("obrigatorio", ""),
                    )
                    for i, c in enumerate(rd.get("campos", []))
                ]
                regs[cod] = LayoutRegistro(
                    registro=rd["registro"],
                    bloco=rd.get("bloco", cod[0]),
                    nivel=int(rd.get("nivel", 2)),
                    nome=rd.get("nome", cod),
                    obrig_entrada=rd.get("obrig_entrada", "F"),
                    ocorrencia=rd.get("ocorrencia", "[0;N]"),
                    abertura=bool(rd.get("abertura", False)),
                    encerramento=bool(rd.get("encerramento", False)),
                    num_campos=int(rd.get("num_campos", len(campos))),
                    campos=campos,
                )
            self._registros[versao] = regs
            self._ordem[versao] = list(dados.get("ordem_registros", regs.keys()))

    # ------------------------------------------------------------------ #
    @property
    def versoes(self) -> List[str]:
        return list(self._layouts.keys())

    def versao_padrao(self) -> str:
        return self.versoes[0] if self.versoes else ""

    def registros(self, versao: str) -> Dict[str, LayoutRegistro]:
        return self._registros.get(versao, {})

    def registro(self, versao: str, cod: str) -> LayoutRegistro | None:
        return self._registros.get(versao, {}).get(cod)

    def ordem_registros(self, versao: str) -> List[str]:
        return self._ordem.get(versao, [])

    def descricao(self, versao: str) -> str:
        return self._layouts.get(versao, {}).get("descricao", "")

    def existe(self, versao: str, cod: str) -> bool:
        return cod in self._registros.get(versao, {})

    def indice_ordem(self, versao: str, cod: str) -> int:
        """Posição canônica do registro na ordem do leiaute (para inserção)."""
        ordem = self._ordem.get(versao, [])
        try:
            return ordem.index(cod)
        except ValueError:
            return len(ordem)  # desconhecido vai para o fim do bloco
