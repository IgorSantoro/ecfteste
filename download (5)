"""Parser + Exportador: fidelidade de bytes (encoding, CRLF, ordem)."""
from __future__ import annotations

import os

import pytest

from editor_ecf.core import Exportador, ParserECF

REAL = os.environ.get("ECF_REAL", "")


def test_roundtrip_sintetico(ecf_bytes, tmp_path):
    origem = tmp_path / "in.txt"
    origem.write_bytes(ecf_bytes)

    arq = ParserECF().ler(str(origem))
    saida = Exportador().para_bytes(arq)

    assert saida == ecf_bytes, "round-trip deveria ser byte-idêntico"
    assert arq.encoding.lower() in ("latin-1", "iso-8859-1")
    assert arq.nova_linha == "\r\n"


def test_campos_preservados(ecf_bytes, tmp_path):
    origem = tmp_path / "in.txt"
    origem.write_bytes(ecf_bytes)
    arq = ParserECF().ler(str(origem))
    r0000 = arq.registros[0]
    assert r0000.reg == "0000"
    assert r0000.campos[3] == "02139940000191"  # CNPJ preservado


@pytest.mark.skipif(not REAL or not os.path.exists(REAL),
                    reason="defina ECF_REAL apontando para uma ECF real")
def test_roundtrip_arquivo_real():
    with open(REAL, "rb") as f:
        original = f.read()
    arq = ParserECF().ler(REAL)
    assert Exportador().para_bytes(arq) == original
