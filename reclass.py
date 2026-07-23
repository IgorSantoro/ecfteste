"""Motor de Hierarquia.

Deriva as relações pai/filho a partir do nível hierárquico do leiaute e
oferece utilidades para:
  * montar a árvore de exibição (ECF -> Blocos -> Registros);
  * localizar o registro pai de um dado registro;
  * calcular a posição canônica de inserção de um novo registro.
"""
from __future__ import annotations

from typing import Dict, List, Optional

from ..models import ArquivoECF, Registro
from .layout_loader import LayoutLoader


class Hierarquia:
    def __init__(self, layout: LayoutLoader, versao: str) -> None:
        self.layout = layout
        self.versao = versao

    # ------------------------------------------------------------------ #
    # Nível / pai teórico (segundo o leiaute)
    # ------------------------------------------------------------------ #
    def nivel(self, reg: str) -> int:
        lr = self.layout.registro(self.versao, reg)
        return lr.nivel if lr else 2

    def registro_pai_teorico(self, reg: str) -> Optional[str]:
        """Registro-pai segundo a Tabela de Registros (nível imediatamente
        inferior que o antecede na ordem do leiaute)."""
        ordem = self.layout.ordem_registros(self.versao)
        if reg not in ordem:
            return None
        idx = ordem.index(reg)
        meu_nivel = self.nivel(reg)
        for j in range(idx - 1, -1, -1):
            if self.nivel(ordem[j]) < meu_nivel:
                return ordem[j]
        return None

    # ------------------------------------------------------------------ #
    # Árvore concreta (a partir dos registros carregados)
    # ------------------------------------------------------------------ #
    def montar_arvore(self, arquivo: ArquivoECF) -> Dict:
        """Retorna estrutura aninhada para a TreeView:

        {'nome': 'ECF', 'blocos': [
            {'letra': '0', 'tipos': [
                {'reg': '0000', 'qtd': 1, 'nome': '...'}, ...]}, ...]}
        """
        raiz: Dict = {"nome": "ECF", "blocos": []}
        for bloco in arquivo.montar_blocos():
            tipos: List[Dict] = []
            vistos: Dict[str, int] = {}
            ordem_tipos: List[str] = []
            for r in bloco.registros:
                if r.reg not in vistos:
                    vistos[r.reg] = 0
                    ordem_tipos.append(r.reg)
                vistos[r.reg] += 1
            for reg in ordem_tipos:
                lr = self.layout.registro(self.versao, reg)
                tipos.append(
                    {
                        "reg": reg,
                        "qtd": vistos[reg],
                        "nome": lr.nome if lr else "",
                        "nivel": lr.nivel if lr else 0,
                    }
                )
            raiz["blocos"].append({"letra": bloco.letra, "tipos": tipos})
        return raiz
