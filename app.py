"""Diálogo de configurações: tema e versão de leiaute ativa."""
from __future__ import annotations

from typing import List

from PySide6.QtWidgets import (
    QComboBox, QDialog, QDialogButtonBox, QFormLayout, QLabel, QVBoxLayout,
)

from .theme import Tema


class SettingsDialog(QDialog):
    def __init__(self, tema_atual: Tema, versao_atual: str,
                 versoes: List[str], parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Configurações")
        self.setMinimumWidth(420)
        self._montar(tema_atual, versao_atual, versoes)

    def _montar(self, tema: Tema, versao: str, versoes: List[str]) -> None:
        lay = QVBoxLayout(self)
        lay.setContentsMargins(18, 18, 18, 18)
        lay.setSpacing(14)

        titulo = QLabel("Preferências")
        titulo.setObjectName("H2")
        lay.addWidget(titulo)

        form = QFormLayout()
        form.setSpacing(12)

        self.cb_tema = QComboBox()
        self.cb_tema.addItems(["Escuro", "Claro"])
        self.cb_tema.setCurrentIndex(0 if tema == Tema.DARK else 1)
        form.addRow("Tema:", self.cb_tema)

        self.cb_versao = QComboBox()
        self.cb_versao.addItems(versoes)
        if versao in versoes:
            self.cb_versao.setCurrentText(versao)
        form.addRow("Leiaute ativo:", self.cb_versao)

        lay.addLayout(form)

        dica = QLabel(
            "Novas versões da ECF são adicionadas apenas colocando o JSON "
            "correspondente na pasta /layouts — nenhuma alteração de código."
        )
        dica.setObjectName("Fraco")
        dica.setWordWrap(True)
        lay.addWidget(dica)

        botoes = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botoes.button(QDialogButtonBox.Ok).setObjectName("Primario")
        botoes.accepted.connect(self.accept)
        botoes.rejected.connect(self.reject)
        lay.addWidget(botoes)

    def tema_escolhido(self) -> Tema:
        return Tema.DARK if self.cb_tema.currentIndex() == 0 else Tema.LIGHT

    def versao_escolhida(self) -> str:
        return self.cb_versao.currentText()
