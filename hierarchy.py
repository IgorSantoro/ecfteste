"""Ponto de entrada do Editor Inteligente de SPED ECF.

Uso:
    python -m editor_ecf.main
ou:
    python editor_ecf/main.py
"""
from __future__ import annotations

import os
import sys

# Permite executar tanto como módulo quanto como script solto.
_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _RAIZ not in sys.path:
    sys.path.insert(0, _RAIZ)

from PySide6.QtWidgets import QApplication  # noqa: E402

from editor_ecf.controller import ControladorECF  # noqa: E402
from editor_ecf.ui import JanelaPrincipal, Tema, aplicar_tema  # noqa: E402

_PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_LAYOUTS = os.path.join(_PASTA, "layouts")
PASTA_LOGS = os.path.join(_PASTA, "logs")


def main() -> int:
    app = QApplication(sys.argv)
    app.setApplicationName("Editor Inteligente de SPED ECF")
    aplicar_tema(app, Tema.DARK)

    controlador = ControladorECF(pasta_layouts=PASTA_LAYOUTS,
                                 pasta_logs=PASTA_LOGS)
    janela = JanelaPrincipal(controlador, app)
    janela.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
