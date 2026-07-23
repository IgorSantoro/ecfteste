"""Diálogo de inserção inteligente de registros.

Permite colar registros no formato ``|M300|...|`` ou importar um .txt
contendo apenas os registros a inserir. O posicionamento é automático — o
usuário nunca escolhe a linha.
"""
from __future__ import annotations

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog, QDialogButtonBox, QFileDialog, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QVBoxLayout,
)

EXEMPLO = "|M310|1.01.01.001|\n|M310|1.01.02.001|"


class InsertDialog(QDialog):
    """Coleta o texto dos registros a inserir. Não valida aqui — quem valida
    e posiciona é o Controlador."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Inserir registros")
        self.setMinimumSize(560, 420)
        self._texto: str = ""
        self._montar()

    def _montar(self) -> None:
        lay = QVBoxLayout(self)
        lay.setContentsMargins(18, 18, 18, 18)
        lay.setSpacing(12)

        titulo = QLabel("Inserção inteligente de registros")
        titulo.setObjectName("H2")
        lay.addWidget(titulo)

        dica = QLabel(
            "Cole os registros (um por linha) ou importe um arquivo .txt. "
            "O sistema localiza sozinho a posição correta, valida e atualiza "
            "todos os totalizadores."
        )
        dica.setObjectName("Fraco")
        dica.setWordWrap(True)
        lay.addWidget(dica)

        self.editor = QPlainTextEdit()
        self.editor.setPlaceholderText(EXEMPLO)
        lay.addWidget(self.editor, 1)

        linha_btn = QHBoxLayout()
        btn_arquivo = QPushButton("Importar .txt…")
        btn_arquivo.clicked.connect(self._importar_txt)
        btn_exemplo = QPushButton("Inserir exemplo")
        btn_exemplo.clicked.connect(lambda: self.editor.setPlainText(EXEMPLO))
        linha_btn.addWidget(btn_arquivo)
        linha_btn.addWidget(btn_exemplo)
        linha_btn.addStretch(1)
        lay.addLayout(linha_btn)

        botoes = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botoes.button(QDialogButtonBox.Ok).setText("Validar e inserir")
        botoes.button(QDialogButtonBox.Ok).setObjectName("Primario")
        botoes.accepted.connect(self._aceitar)
        botoes.rejected.connect(self.reject)
        lay.addWidget(botoes)

    def _importar_txt(self) -> None:
        caminho, _ = QFileDialog.getOpenFileName(
            self, "Selecionar arquivo de registros", "",
            "Arquivos SPED (*.txt);;Todos os arquivos (*.*)")
        if not caminho:
            return
        for enc in ("latin-1", "utf-8"):
            try:
                with open(caminho, "r", encoding=enc) as f:
                    self.editor.setPlainText(f.read())
                break
            except UnicodeDecodeError:
                continue

    def _aceitar(self) -> None:
        self._texto = self.editor.toPlainText().strip()
        if self._texto:
            self.accept()

    def texto_registros(self) -> str:
        return self._texto
