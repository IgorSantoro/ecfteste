"""Diálogo de relatório de validação.

Exibe as ocorrências (erros, avisos, informações) em tabela colorida.
"""
from __future__ import annotations

from typing import List

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel, QTableWidget,
    QTableWidgetItem, QVBoxLayout,
)

from ..core.validator import Nivel, Ocorrencia
from .theme import ERRO, INFO, OK, WARN

_COR = {Nivel.ERRO: ERRO, Nivel.AVISO: WARN, Nivel.INFO: INFO}


class ValidationDialog(QDialog):
    def __init__(self, ocorrencias: List[Ocorrencia], parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Relatório de validação")
        self.setMinimumSize(760, 480)
        self._montar(ocorrencias)

    def _montar(self, ocs: List[Ocorrencia]) -> None:
        lay = QVBoxLayout(self)
        lay.setContentsMargins(18, 18, 18, 18)
        lay.setSpacing(12)

        n_erro = sum(1 for o in ocs if o.nivel == Nivel.ERRO)
        n_aviso = sum(1 for o in ocs if o.nivel == Nivel.AVISO)
        n_info = sum(1 for o in ocs if o.nivel == Nivel.INFO)

        cab = QHBoxLayout()
        titulo = QLabel("Resultado da validação estrutural")
        titulo.setObjectName("H2")
        cab.addWidget(titulo)
        cab.addStretch(1)
        for rot, val, cor in (("Erros", n_erro, ERRO),
                              ("Avisos", n_aviso, WARN),
                              ("Infos", n_info, INFO)):
            chip = QLabel(f"● {rot}: {val}")
            chip.setStyleSheet(f"color:{cor}; font-weight:600;")
            cab.addWidget(chip)
        lay.addLayout(cab)

        if not ocs:
            ok = QLabel("Nenhuma inconsistência encontrada. Estrutura íntegra.")
            ok.setStyleSheet(f"color:{OK}; font-weight:600; font-size:14px;")
            ok.setAlignment(Qt.AlignCenter)
            lay.addWidget(ok, 1)
        else:
            tab = QTableWidget(len(ocs), 5)
            tab.setHorizontalHeaderLabels(
                ["Nível", "Registro", "Linha", "Regra", "Mensagem"])
            tab.setEditTriggers(QTableWidget.NoEditTriggers)
            tab.setAlternatingRowColors(True)
            tab.verticalHeader().setVisible(False)
            for i, o in enumerate(ocs):
                item_nivel = QTableWidgetItem(o.nivel.value)
                item_nivel.setForeground(QColor(_COR.get(o.nivel, INFO)))
                tab.setItem(i, 0, item_nivel)
                tab.setItem(i, 1, QTableWidgetItem(o.registro))
                tab.setItem(i, 2, QTableWidgetItem(str(o.linha or "-")))
                tab.setItem(i, 3, QTableWidgetItem(o.regra))
                tab.setItem(i, 4, QTableWidgetItem(o.mensagem))
            tab.resizeColumnsToContents()
            tab.horizontalHeader().setStretchLastSection(True)
            lay.addWidget(tab, 1)

        botoes = QDialogButtonBox(QDialogButtonBox.Close)
        botoes.rejected.connect(self.reject)
        botoes.accepted.connect(self.accept)
        botoes.button(QDialogButtonBox.Close).clicked.connect(self.accept)
        lay.addWidget(botoes)
