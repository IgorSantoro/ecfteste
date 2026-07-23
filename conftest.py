"""Reparo automático: remoção de duplicatas únicas + totalizadores."""
from __future__ import annotations

from editor_ecf.core import Contador, ParserECF, Reparador


def _arq(ecf_bytes, tmp_path):
    p = tmp_path / "in.txt"
    p.write_bytes(ecf_bytes)
    return ParserECF().ler(str(p))


def test_reparo_remove_duplicata_unica(ecf_bytes, layout, versao, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    # duplica o 0000 (registro único [1;1]) de forma idêntica
    dup = ParserECF().ler_texto(arq.registros[0].para_linha())[0]
    arq.registros.insert(1, dup)
    assert arq.contagem_por_tipo()["0000"] == 2

    res = Reparador(layout, versao).reparar(arq)
    assert arq.contagem_por_tipo()["0000"] == 1
    assert ("0000", 1) in res.duplicatas_removidas


def test_reparo_corrige_totalizadores(ecf_bytes, layout, versao, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    Reparador(layout, versao).reparar(arq)
    m = {r.reg: r.campos for r in arq.registros}
    assert m["9999"][1] == str(arq.total_linhas)
    assert "9990" in m and "0990" in m


def test_reparo_nao_inventa_valores(ecf_bytes, layout, versao, tmp_path):
    """Campo obrigatório vazio deve aparecer como pendência, não ser preenchido."""
    arq = _arq(ecf_bytes, tmp_path)
    # insere M310 sem COD_CTA (obrigatório) para gerar pendência
    m310 = ParserECF().ler_texto("|M310||")[0]
    # coloca dentro do bloco M seria o certo, mas para o teste basta existir
    arq.registros.insert(1, m310)
    res = Reparador(layout, versao).reparar(arq)
    assert any("M310" in p and "COD_CTA" in p for p in res.pendencias)
    # o valor não foi inventado
    m310_final = [r for r in arq.registros if r.reg == "M310"][0]
    assert m310_final.campo(1).strip() == ""
