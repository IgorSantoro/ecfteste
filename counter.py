"""Inserção inteligente e regras de validação isoladas."""
from __future__ import annotations

from editor_ecf.core import (
    Contador, InsercaoInteligente, ParserECF, Validador,
)
from editor_ecf.core.validator import (
    Nivel, cnpj_valido, cpf_valido, data_valida,
)


def _arq(ecf_bytes, tmp_path):
    p = tmp_path / "in.txt"
    p.write_bytes(ecf_bytes)
    return ParserECF().ler(str(p))


def test_insercao_posiciona_no_bloco_correto(ecf_bytes, layout, versao,
                                             tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    novos = ParserECF().ler_texto("|0010|LP|G|N|A|...|")
    res = InsercaoInteligente(layout, versao).inserir(arq, novos)

    assert "0010" in res.inseridos
    regs = [r.reg for r in arq.registros]
    # 0010 deve ficar dentro do bloco 0, depois de 0000/0001, antes de 0990
    i0001 = regs.index("0001")
    i0010 = regs.index("0010")
    i0990 = regs.index("0990")
    assert i0001 < i0010 < i0990


def test_insercao_cria_bloco_ausente(ecf_bytes, layout, versao, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    # bloco C não existe na ECF sintética; inserir C040 deve criar C001/C990
    novos = ParserECF().ler_texto("|C040|1|02139940000191|")
    res = InsercaoInteligente(layout, versao).inserir(arq, novos)
    regs = [r.reg for r in arq.registros]
    assert "C040" in res.inseridos
    assert "C001" in regs and "C990" in regs
    assert regs.index("C001") < regs.index("C040") < regs.index("C990")


def test_validador_rejeita_campo_obrigatorio_vazio(ecf_bytes, layout, versao,
                                                   tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    novos = ParserECF().ler_texto("|M310||")  # COD_CTA obrigatório vazio
    ocs = Validador(layout, versao).validar_novos(novos, arq)
    assert any(o.nivel == Nivel.ERRO for o in ocs)


# ----------------------- helpers de validação --------------------------- #
def test_cnpj():
    assert cnpj_valido("02139940000191")
    assert not cnpj_valido("11111111111111")
    assert not cnpj_valido("123")


def test_cpf():
    assert cpf_valido("52998224725")
    assert not cpf_valido("00000000000")
    assert not cpf_valido("abc")


def test_data():
    assert data_valida("31122025")
    assert not data_valida("32012025")
    assert not data_valida("2025-12-31")
