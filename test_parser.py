"""Assistente: interpretação de comandos em português e segurança."""
from __future__ import annotations

from editor_ecf.core import Assistente, ParserECF


def _arq(ecf_bytes, tmp_path):
    p = tmp_path / "in.txt"
    p.write_bytes(ecf_bytes)
    return ParserECF().ler(str(p))


def test_interpreta_insercao(layout, versao):
    cmd = Assistente(layout, versao).interpretar(
        "inserir M310 com COD_CTA = 1.01.01.001")
    assert cmd.acao == "inserir"
    assert cmd.registro == "M310"
    assert cmd.campos == {"COD_CTA": "1.01.01.001"}


def test_valor_nao_engole_referencia_ao_registro(layout, versao):
    """'para 9.99 no M310' → valor é '9.99', não '9.99 no M310'."""
    cmd = Assistente(layout, versao).interpretar(
        "alterar COD_CTA para 9.99 no M310 onde COD_CTA = 1.01")
    assert cmd.campos == {"COD_CTA": "9.99"}
    assert cmd.filtro == {"COD_CTA": "1.01"}


def test_valor_com_espacos_preservado(layout, versao):
    cmd = Assistente(layout, versao).interpretar(
        "no 0000, alterar NOME para BANCO DO BRASIL SA")
    assert cmd.campos["NOME"] == "BANCO DO BRASIL SA"


def test_registro_montado_com_num_campos_do_leiaute(layout, versao,
                                                    ecf_bytes, tmp_path):
    """Mesmo informando 1 campo, a estrutura sai completa conforme o manual."""
    ass = Assistente(layout, versao)
    cmd = ass.interpretar("inserir M310 com COD_CTA = 1.01")
    novo = ass.registro_para_inserir(cmd)
    lr = layout.registro(versao, "M310")
    assert novo.num_campos == lr.num_campos


def test_nao_inventa_campo_obrigatorio(layout, versao, ecf_bytes, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    resp = Assistente(layout, versao).processar("inserir M310", arq)
    assert not resp.aplicavel          # não aplica
    assert "COD_CTA" in resp.mensagem  # pergunta pelo campo


def test_recusa_remover_abertura_de_bloco(layout, versao, ecf_bytes, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    resp = Assistente(layout, versao).processar("remover 0001", arq)
    assert not resp.aplicavel
    assert "estrutura" in resp.mensagem.lower()


def test_campo_inexistente_e_rejeitado(layout, versao, ecf_bytes, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    resp = Assistente(layout, versao).processar(
        "inserir M310 com CAMPO_FALSO = 1", arq)
    assert not resp.aplicavel
    assert "CAMPO_FALSO" in resp.mensagem


def test_consulta_quantos(layout, versao, ecf_bytes, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    resp = Assistente(layout, versao).processar("quantos 0000 existem?", arq)
    assert "1 ocorrência" in resp.mensagem
    assert not resp.aplicavel


def test_alteracao_gera_previa_sem_aplicar(layout, versao, ecf_bytes, tmp_path):
    arq = _arq(ecf_bytes, tmp_path)
    antes = arq.registros[0].para_linha()
    resp = Assistente(layout, versao).processar(
        "no 0000, alterar NOME para OUTRA EMPRESA LTDA", arq)
    assert resp.aplicavel and resp.previa
    # nada foi alterado ainda: prévia é só simulação
    assert arq.registros[0].para_linha() == antes
