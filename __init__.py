"""Lote de registros colados: extração, validação e substituição."""
from __future__ import annotations

from editor_ecf.core import Assistente, ParserECF

LINHA_A = "|Y570|00083430000114|POSTO REGINAS LTDA|N|1708|10025,15|150,38|0,00|"
LINHA_B = "|Y570|00371046000117|SM SUPERMERCADOS LTDA|N|5952|44000,00|0,00|440,00|"


def _arq(ecf_bytes, tmp_path):
    p = tmp_path / "in.txt"
    p.write_bytes(ecf_bytes)
    return ParserECF().ler(str(p))


def test_extrai_linhas_separadas_por_quebra(layout, versao):
    brutos = Assistente(layout, versao).extrair_brutos(
        LINHA_A + "\n" + LINHA_B)
    assert len(brutos) == 2
    assert all(r.reg == "Y570" for r in brutos)
    assert brutos[0].num_campos == 8


def test_extrai_linhas_coladas_numa_so(layout, versao):
    """Formato que o chat produz: '...|0,00| |Y570|...'."""
    brutos = Assistente(layout, versao).extrair_brutos(
        LINHA_A + " " + LINHA_B)
    assert len(brutos) == 2
    assert brutos[1].campo(1) == "00371046000117"


def test_extrai_com_texto_antes(layout, versao):
    """O pedido pode preceder a primeira linha colada."""
    brutos = Assistente(layout, versao).extrair_brutos(
        "apagar as anteriores e substituir por " + LINHA_A + " " + LINHA_B)
    assert len(brutos) == 2
    assert brutos[0].campo(1) == "00083430000114"


def test_preserva_conteudo_exato(layout, versao):
    brutos = Assistente(layout, versao).extrair_brutos(LINHA_A)
    assert brutos[0].para_linha() == LINHA_A


def test_lote_sem_palavra_chave_insere(layout, versao, ecf_bytes, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    resp = Assistente(layout, versao).processar(LINHA_A, arq)
    assert resp.aplicavel
    assert resp.comando.acao == "lote_inserir"


def test_lote_com_substituir(layout, versao, ecf_bytes, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    resp = Assistente(layout, versao).processar(
        "substituir o bloco: " + LINHA_A, arq)
    assert resp.comando.acao == "lote_substituir"


def test_lote_rejeita_numero_de_campos_errado(layout, versao, ecf_bytes,
                                              tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    curta = "|Y570|00083430000114|EMPRESA|N|"      # faltam campos
    resp = Assistente(layout, versao).processar(curta, arq)
    assert not resp.aplicavel
    assert "campos" in resp.mensagem.lower()


def test_lote_rejeita_obrigatorio_vazio(layout, versao, ecf_bytes, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    vazio = "|Y570||POSTO X LTDA|N|1708|10025,15|150,38|0,00|"  # CNPJ vazio
    resp = Assistente(layout, versao).processar(vazio, arq)
    assert not resp.aplicavel
    assert "CNPJ_FON" in resp.mensagem


def test_pedido_de_substituicao_sem_dados_pede_as_linhas(layout, versao,
                                                        ecf_bytes, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    resp = Assistente(layout, versao).processar(
        "Preciso substituir o bloco do Y570 inteiro", arq)
    assert not resp.aplicavel
    assert "cole" in resp.mensagem.lower()
