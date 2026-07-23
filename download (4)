"""Contador: correção automática dos totalizadores."""
from __future__ import annotations

from editor_ecf.core import Contador, ParserECF


def _por_reg(arq):
    return {r.reg: r.campos for r in arq.registros}


def test_recontagem_corrige_totalizadores(ecf_bytes, layout, versao, tmp_path):
    origem = tmp_path / "in.txt"
    origem.write_bytes(ecf_bytes)
    arq = ParserECF().ler(str(origem))

    Contador().recalcular(arq, layout.ordem_registros(versao))
    m = _por_reg(arq)

    # Bloco 0: 0000, 0001, 0990  -> 0990 = 3
    assert m["0990"][1] == "3"
    # 9999 = total de linhas do arquivo inteiro
    assert m["9999"][1] == str(arq.total_linhas)
    # 9990 = registros do bloco 9 (9001 + 9900* + 9990 + 9999)
    n_bloco9 = sum(1 for r in arq.registros if r.reg.startswith("9"))
    assert m["9990"][1] == str(n_bloco9)


def test_9900_uma_linha_por_tipo(ecf_bytes, layout, versao, tmp_path):
    origem = tmp_path / "in.txt"
    origem.write_bytes(ecf_bytes)
    arq = ParserECF().ler(str(origem))
    Contador().recalcular(arq, layout.ordem_registros(versao))

    tipos_9900 = [r.campos[1] for r in arq.registros if r.reg == "9900"]
    # cada tipo aparece uma única vez
    assert len(tipos_9900) == len(set(tipos_9900))
    # 9900 conta a si próprio
    assert "9900" in tipos_9900


def test_recontagem_idempotente(ecf_bytes, layout, versao, tmp_path):
    origem = tmp_path / "in.txt"
    origem.write_bytes(ecf_bytes)
    arq = ParserECF().ler(str(origem))
    ordem = layout.ordem_registros(versao)
    Contador().recalcular(arq, ordem)
    antes = _por_reg(arq)
    Contador().recalcular(arq, ordem)
    depois = _por_reg(arq)
    assert antes == depois, "recontar duas vezes não pode mudar nada"
