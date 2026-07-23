"""Fixtures compartilhadas dos testes."""
from __future__ import annotations

import os

import pytest

from editor_ecf.core import LayoutLoader

_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_LAYOUTS = os.path.join(_RAIZ, "layouts")


@pytest.fixture(scope="session")
def layout() -> LayoutLoader:
    return LayoutLoader(PASTA_LAYOUTS)


@pytest.fixture(scope="session")
def versao(layout: LayoutLoader) -> str:
    return "0012"


@pytest.fixture()
def ecf_bytes() -> bytes:
    """ECF sintética mínima, mas estruturalmente coerente, em latin-1/CRLF.

    Totalizadores propositalmente 'errados' para os testes de recontagem
    provarem que o Contador os corrige.
    """
    linhas = [
        "|0000|LECF|0012|02139940000191|EMPRESA TESTE LTDA|"
        "01012025|31122025|0|0|N|N|N||",
        "|0001|0|",
        "|0990|1|",                       # errado de propósito (deveria ser 3)
        "|9001|0|",
        "|9990|0|",                       # errado de propósito
        "|9999|0|",                       # errado de propósito
    ]
    return ("\r\n".join(linhas) + "\r\n").encode("latin-1")
