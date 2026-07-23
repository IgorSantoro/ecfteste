"""Editor Inteligente de SPED ECF — interface Streamlit.

Reaproveita integralmente a engine (parser, leiaute, validação, inserção
inteligente, totalizadores e exportação). Rode com:

    streamlit run editor_ecf/app.py
"""
from __future__ import annotations

import os
import sys

# Permite `streamlit run editor_ecf/app.py` a partir de qualquer pasta.
_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _RAIZ not in sys.path:
    sys.path.insert(0, _RAIZ)

import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

from editor_ecf import __version__  # noqa: E402
from editor_ecf.controller import ControladorECF  # noqa: E402
from editor_ecf.core.validator import Nivel  # noqa: E402

_PASTA = os.path.dirname(os.path.abspath(__file__))
PASTA_LAYOUTS = os.path.join(_PASTA, "layouts")
PASTA_LOGS = os.path.join(_PASTA, "logs")

ACCENT = "#1f9d8f"
OK = "#2e9e5b"
WARN = "#d9a441"
ERRO = "#d9534f"
INFO = "#3a8dde"

EXEMPLO = "|M310|1.01.01.001|\n|M310|1.01.02.001|"

st.set_page_config(page_title="Editor Inteligente de SPED ECF",
                   page_icon="📊", layout="wide")

st.markdown(f"""
<style>
  .block-container {{ padding-top: 2rem; }}
  h1, h2, h3 {{ letter-spacing: -.2px; }}
  .cartao {{ background: rgba(31,157,143,.07); border: 1px solid {ACCENT}33;
            border-radius: 12px; padding: 16px 20px; }}
  .chip {{ display:inline-block; padding:2px 10px; margin:2px;
           border:1px solid {ACCENT}55; border-radius:20px; font-size:12px;
           color:{ACCENT}; font-weight:600; }}
  div[data-testid="stMetricValue"] {{ color: {ACCENT}; }}
  .stDownloadButton button, .stButton button {{ border-radius: 8px; }}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------------------------------- #
# Estado
# --------------------------------------------------------------------------- #
@st.cache_resource
def _controlador(versao_app: str) -> ControladorECF:
    # ``versao_app`` participa da chave do cache: quando o pacote é
    # atualizado, o controlador antigo é descartado automaticamente.
    return ControladorECF(pasta_layouts=PASTA_LAYOUTS, pasta_logs=PASTA_LOGS)


ctrl = _controlador(__version__)
st.session_state.setdefault("carregado", False)
st.session_state.setdefault("log", [])


def registrar(msg: str) -> None:
    st.session_state["log"].insert(0, msg)


# --------------------------------------------------------------------------- #
# Barra lateral
# --------------------------------------------------------------------------- #
with st.sidebar:
    st.header("📊 Editor de SPED ECF")
    st.caption("Importe, edite e exporte a ECF com totalizadores automáticos.")

    up = st.file_uploader("Arquivo SPED ECF (.txt)", type=["txt"])
    if up is not None and st.button("Importar", type="primary",
                                    use_container_width=True):
        try:
            ctrl.importar_bytes(up.getvalue(), nome=up.name)
            st.session_state["carregado"] = True
            registrar(f"ECF importada: {ctrl.arquivo.total_linhas} linhas.")
            st.success("ECF importada com sucesso.")
        except Exception as exc:  # noqa: BLE001
            st.error(f"Falha ao importar: {exc}")

    if ctrl.layout.versoes:
        st.divider()
        vs = ctrl.layout.versoes
        atual = vs.index(ctrl.versao) if ctrl.versao in vs else 0
        ctrl.versao = st.selectbox("Leiaute ativo", vs, index=atual)
        st.caption(ctrl.layout.descricao(ctrl.versao))


# --------------------------------------------------------------------------- #
# Tela inicial (sem arquivo)
# --------------------------------------------------------------------------- #
if not st.session_state["carregado"] or ctrl.arquivo is None:
    st.title("Editor Inteligente de SPED ECF")
    st.write("Envie um arquivo **.txt** da ECF na barra lateral para começar.")
    st.markdown("""
    - **Importação** fiel (encoding e quebras de linha preservados).
    - **Inserção inteligente**: o sistema acha sozinho a posição do registro.
    - **Validação** estrutural por regras independentes.
    - **Totalizadores** (`X990`, `9900`, `9990`, `9999`) recalculados sozinhos.
    - **Exportação** compatível com o PVA da Receita.
    """)
    st.stop()


# --------------------------------------------------------------------------- #
# Abas
# --------------------------------------------------------------------------- #
d = ctrl.dados_painel()
st.title(d["empresa"] or "ECF")
st.caption(f"CNPJ {d['cnpj']}  •  Período {d['periodo']}  •  "
           f"{d['descricao_leiaute']}")

aba_painel, aba_chat, aba_reclass, aba_estr, aba_ins, aba_val, aba_exp = \
    st.tabs(["📈 Painel", "💬 Assistente", "🔄 Reclassificar", "🌳 Estrutura",
             "➕ Inserir", "✓ Validar", "💾 Exportar"])

# ----------------------------- Painel -------------------------------------- #
with aba_painel:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total de linhas", f"{d['linhas']:,}".replace(",", "."))
    c2.metric("Tipos de registro", d["tipos"])
    c3.metric("Blocos", len(d["blocos"]))
    c4.metric("Leiaute", d["versao"])

    st.subheader("Blocos presentes")
    st.markdown("".join(f"<span class='chip'>{b}</span>"
                        for b in d["blocos"]), unsafe_allow_html=True)

    st.subheader("Distribuição por tipo de registro")
    cont = ctrl.arquivo.contagem_por_tipo()
    df = pd.DataFrame(
        [{"Registro": k, "Nome": ctrl.info_registro(k)["nome"],
          "Quantidade": v} for k, v in sorted(cont.items())])
    st.dataframe(df, use_container_width=True, hide_index=True, height=340)

# --------------------------- Assistente ------------------------------------ #
with aba_chat:
    st.subheader("Assistente da ECF")
    st.caption("Diga o que precisa alterar ou inserir. Eu consulto o leiaute "
               "do manual, monto o registro com a estrutura correta e mostro "
               "uma **prévia** — nada é aplicado sem a sua confirmação.")

    st.session_state.setdefault("chat", [])
    st.session_state.setdefault("pendente", None)   # (Comando, prévia, msg)

    with st.expander("Exemplos de comandos"):
        st.markdown(
            "- `o que é o M300?`\n"
            "- `quantos M350 existem?`\n"
            "- `inserir M310 com COD_CTA = 1.01.01.001`\n"
            "- `no 0000, alterar NOME para EMPRESA X LTDA`\n"
            "- `alterar VALOR para 1500,00 no M300 onde COD_CTA = 1.01`\n"
            "- `remover M310 onde COD_CTA = 1.01.01.001`\n"
            "- `corrigir estrutura` · `recalcular totalizadores`\n"
            "- **Lote:** cole as linhas `|Y570|...|` (use a caixa abaixo); "
            "escreva *substituir* para trocar as existentes")

    with st.expander("📋 Colar lote de registros (para volumes grandes)"):
        st.caption("Cole as linhas prontas no formato `|Y570|...|`. Aceito "
                   "uma por linha, grudadas ou todas numa só. Confiro cada "
                   "registro contra o leiaute antes de aplicar.")
        lote = st.text_area("Registros", height=180, key="lote_txt",
                            placeholder="|Y570|00083430000114|POSTO REGINAS "
                                        "LTDA|N|1708|10025,15|150,38|0,00|")
        modo = st.radio(
            "O que fazer com os registros já existentes desse tipo?",
            ["Substituir (apagar os atuais e inserir estes)",
             "Inserir (manter os atuais e acrescentar estes)"],
            key="lote_modo")
        if st.button("Analisar lote", use_container_width=True):
            if not lote.strip():
                st.warning("Cole ao menos um registro.")
            else:
                prefixo = ("substituir " if modo.startswith("Substituir")
                           else "inserir ")
                try:
                    resp = ctrl.chat_processar(prefixo + lote)
                    st.session_state["chat"].append(
                        ("user", f"[lote de registros — "
                                 f"{modo.split(' ')[0].lower()}]"))
                    st.session_state["chat"].append(
                        ("assistant", resp.mensagem))
                    st.session_state["pendente"] = (
                        (resp.comando, resp.previa, resp.mensagem)
                        if resp.aplicavel and resp.comando else None)
                    st.rerun()
                except Exception as exc:  # noqa: BLE001
                    st.error(f"Erro ao interpretar o lote: {exc}")

    for papel, texto in st.session_state["chat"]:
        with st.chat_message(papel):
            st.markdown(texto)

    # ---- confirmação de uma operação pendente ---- #
    pend = st.session_state["pendente"]
    if pend is not None:
        cmd, previa, _ = pend
        with st.chat_message("assistant"):
            if previa:
                st.markdown("**Prévia da alteração:**")
                st.dataframe(
                    pd.DataFrame([{"Antes": a, "Depois": b}
                                  for a, b in previa]),
                    use_container_width=True, hide_index=True)
            c_ok, c_no = st.columns(2)
            if c_ok.button("✅ Confirmar e aplicar", type="primary",
                           use_container_width=True):
                try:
                    msg = ctrl.chat_aplicar(cmd)
                    st.session_state["chat"].append(("assistant", f"✅ {msg}"))
                    registrar(f"Chat: {msg}")
                except Exception as exc:  # noqa: BLE001
                    st.session_state["chat"].append(
                        ("assistant", f"❌ Falha ao aplicar: {exc}"))
                st.session_state["pendente"] = None
                st.rerun()
            if c_no.button("✖ Cancelar", use_container_width=True):
                st.session_state["chat"].append(
                    ("assistant", "Operação cancelada. Nada foi alterado."))
                st.session_state["pendente"] = None
                st.rerun()

    # ---- entrada do usuário ---- #
    pergunta = st.chat_input("O que você precisa alterar na ECF?")
    if pergunta:
        st.session_state["chat"].append(("user", pergunta))
        try:
            resp = ctrl.chat_processar(pergunta)
            st.session_state["chat"].append(("assistant", resp.mensagem))
            st.session_state["pendente"] = (
                (resp.comando, resp.previa, resp.mensagem)
                if resp.aplicavel and resp.comando else None)
        except Exception as exc:  # noqa: BLE001
            st.session_state["chat"].append(
                ("assistant", f"❌ Erro ao interpretar: {exc}"))
            st.session_state["pendente"] = None
        st.rerun()

    if st.session_state["chat"] and st.button("Limpar conversa"):
        st.session_state["chat"] = []
        st.session_state["pendente"] = None
        st.rerun()

# -------------------------- Reclassificar ---------------------------------- #
with aba_reclass:
    st.subheader("Reclassificação de códigos (M300 / M350)")
    st.caption("Importe a planilha De→Para com os valores mensais e anual. "
               "Transfiro os valores entre códigos **período a período** "
               "(Janeiro→A01 … Dezembro→A12, Anual→A00): valor igual ao do "
               "lançamento → o lançamento muda de código; menor → subtraio "
               "e crio o lançamento no código destino. Quando o lançamento "
               "tem contas vinculadas (M310/M305), a conta indicada decide "
               "qual usar e migra junto; quando é um valor agregado sem "
               "vínculos, caso a soma das linhas do mesmo código, cada uma "
               "saca sua parcela dele.")

    st.session_state.setdefault("reclass_regras", None)
    st.session_state.setdefault("reclass_previa", None)

    plan = st.file_uploader("Planilha de reclassificação (.xlsx)",
                            type=["xlsx", "xlsm"], key="reclass_file")

    with st.expander("Mapeamento das colunas", expanded=False):
        st.caption("Ajuste se a sua planilha usar outras colunas.")
        cc1, cc2, cc3 = st.columns(3)
        col_de = cc1.text_input("Código atual (De)", value="Y")
        col_para = cc2.text_input("Código destino (Para)", value="Z")
        col_rel = cc3.text_input("Relacionamento", value="F")
        cc4, cc5, cc6 = st.columns(3)
        col_cb = cc4.text_input("Conta da Parte B", value="G")
        col_desc = cc5.text_input("Descrição (desempate)", value="C")
        col_val = cc6.text_input("Valor anual", value="W")
        cc7, cc8 = st.columns(2)
        col_mes = cc7.text_input("Primeiro mês (Janeiro)", value="K",
                                 help="Fev–Dez seguem nas colunas contíguas.")
        col_imp = cc8.text_input("Imposto (AMBOS/IRPJ/CSLL)", value="I")

    alterar_desc = st.checkbox(
        "Nas trocas integrais, substituir a descrição pela oficial da "
        "tabela de códigos",
        value=False,
        help="Lançamentos novos (transferência parcial) sempre recebem a "
             "descrição oficial do código destino. Esta opção estende isso "
             "às trocas integrais; desmarcada, a descrição atual é mantida.")

    if plan is not None and st.button("Ler planilha e gerar prévia",
                                      type="primary"):
        try:
            colunas = {"de": col_de, "para": col_para,
                       "relacionamento": col_rel, "conta_b": col_cb,
                       "descricao": col_desc, "valor": col_val,
                       "meses_inicio": col_mes, "imposto": col_imp}
            regras, avisos = ctrl.reclass_ler_planilha(plan.getvalue(),
                                                       colunas=colunas)
            st.session_state["reclass_regras"] = regras
            st.session_state["reclass_previa"] = ctrl.reclass_previa(
                regras, alterar_descricao=alterar_desc)
            for a in avisos:
                st.info(a)
            registrar(f"Reclassificação: {len(regras)} regra(s) lida(s).")
        except Exception as exc:  # noqa: BLE001
            st.error(f"Falha ao ler a planilha: {exc}")

    regras = st.session_state["reclass_regras"]
    res = st.session_state["reclass_previa"]

    # Objetos guardados por uma versão anterior do código (sessão antiga do
    # Streamlit) não têm os campos novos — descarta e pede nova prévia.
    if res is not None and not hasattr(res, "problemas"):
        st.session_state["reclass_regras"] = None
        st.session_state["reclass_previa"] = None
        regras = res = None
        st.info("O aplicativo foi atualizado. Gere a prévia novamente.")

    if regras is not None and res is not None:
        from editor_ecf.core.reclass import fmt_brl

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Regras na planilha", len(regras))
        c2.metric("Operações previstas", len(res.correspondencias))
        c3.metric("Problemas", len(res.problemas))
        c4.metric("Conflitos", len(res.conflitos))

        total_mov = sum(c.montante for c in res.correspondencias)
        st.caption(f"Valor total movimentado (soma de todos os períodos e "
                   f"impostos): **R$ {fmt_brl(total_mov)}**")

        for a in res.avisos:
            st.info(a)

        if res.conflitos:
            st.error("**Conflitos encontrados — nada será aplicado.** "
                     "Ajuste a planilha e gere a prévia de novo.")
            st.dataframe(pd.DataFrame({"Conflito": res.conflitos}),
                         use_container_width=True, hide_index=True)

        if res.problemas:
            st.warning("**Períodos com problema** (não serão alterados; "
                       "o restante segue normal):")
            st.dataframe(pd.DataFrame({"Problema": res.problemas}),
                         use_container_width=True, hide_index=True)

        if res.correspondencias:
            st.markdown("**Prévia da reclassificação** — cada linha é uma "
                        "operação em um período:")
            st.dataframe(pd.DataFrame([{
                "Imposto": "IRPJ" if c.registro == "M300" else "CSLL",
                "Período": c.periodo,
                "L.plan.": c.regra.linha,
                "De": c.regra.de,
                "Para": c.regra.para,
                "Valor movido": "R$ " + fmt_brl(c.montante),
                "Modo": {"integral": "troca integral",
                         "parcial": "cria lançamento",
                         "soma_destino": "soma no destino existente"
                         }.get(c.modo, c.modo),
                "Critério": c.criterio,
                "Origem antes": c.antes,
                "Origem depois": c.depois or "(removido)",
                "Destino": (c.destino_depois if c.modo == "soma_destino"
                            else (c.novo or c.depois)),
            } for c in res.correspondencias]),
                use_container_width=True, hide_index=True, height=420)

        if res.sem_alvo:
            st.warning("Regras **sem lançamento correspondente** no arquivo:")
            st.dataframe(pd.DataFrame([{
                "Linha planilha": r.linha, "De": r.de, "Para": r.para,
                "Vínculo": ("Parte B " + r.conta_b if r.por_parte_b
                            else "Conta " + r.relacionamento),
                "Detalhe": det,
            } for r, det in res.sem_alvo]),
                use_container_width=True, hide_index=True)

        if res.aplicavel:
            st.markdown("---")
            if st.button("✅ Aplicar reclassificação", type="primary"):
                try:
                    msg = ctrl.reclass_aplicar(
                        res, alterar_descricao=alterar_desc)
                    registrar(f"Reclassificação aplicada: {msg}")
                    st.success(msg + "  Baixe o arquivo na aba **Exportar**.")
                    st.session_state["reclass_previa"] = None
                    st.session_state["reclass_regras"] = None
                except Exception as exc:  # noqa: BLE001
                    st.error(f"Falha ao aplicar: {exc}")
        elif not res.conflitos and not res.correspondencias:
            st.warning("Nenhuma regra encontrou lançamento correspondente. "
                       "Confira o mapeamento das colunas e os vínculos.")

# --------------------------- Estrutura ------------------------------------- #
with aba_estr:
    arvore = ctrl.montar_arvore()
    col_a, col_b = st.columns([1, 1])

    with col_a:
        st.subheader("Árvore da ECF")
        for bloco in arvore["blocos"]:
            with st.expander(f"Bloco {bloco['letra']}  "
                             f"({len(bloco['tipos'])} tipos)"):
                st.dataframe(
                    pd.DataFrame([{"Registro": t["reg"], "Nome": t["nome"],
                                   "Qtd": t["qtd"]} for t in bloco["tipos"]]),
                    use_container_width=True, hide_index=True)

    with col_b:
        st.subheader("Detalhe do registro")
        todos = sorted(ctrl.arquivo.contagem_por_tipo().keys())
        reg = st.selectbox("Selecione um registro", todos)
        if reg:
            info = ctrl.info_registro(reg)
            st.markdown(f"### {info['reg']} — {info['nome']}")
            st.caption(
                f"Nível {info['nivel']}  •  Ocorrência: {info['ocorrencia']}  "
                f"•  Obrigatoriedade: {info['obrig']}  •  "
                f"No arquivo: {info['qtd']}")
            if info["campos"]:
                st.dataframe(
                    pd.DataFrame([{"Nº": c["seq"], "Campo": c["nome"],
                                   "Tipo": c["tipo"],
                                   "Obrigatório": "Sim" if c["obrig"] else "Não"}
                                  for c in info["campos"]]),
                    use_container_width=True, hide_index=True, height=360)

# ---------------------------- Inserir -------------------------------------- #
with aba_ins:
    st.subheader("Inserção inteligente de registros")
    st.caption("Cole os registros (um por linha). O sistema localiza a posição "
               "correta, valida e atualiza todos os totalizadores.")
    if st.button("Inserir exemplo"):
        st.session_state["texto_ins"] = EXEMPLO
    texto = st.text_area("Registros", key="texto_ins",
                         placeholder=EXEMPLO, height=180)

    if st.button("Validar e inserir", type="primary"):
        if not texto.strip():
            st.warning("Cole ao menos um registro.")
        else:
            rel = ctrl.inserir_texto(texto)
            erros = [o for o in rel.erros if o.nivel == Nivel.ERRO]
            if erros and not rel.adicionados:
                st.error(f"Inserção abortada: {len(erros)} erro(s).")
                st.dataframe(pd.DataFrame(
                    [{"Nível": o.nivel.value, "Registro": o.registro,
                      "Regra": o.regra, "Mensagem": o.mensagem}
                     for o in rel.erros]),
                    use_container_width=True, hide_index=True)
                registrar(f"Inserção abortada: {len(erros)} erro(s).")
            else:
                registrar(
                    f"Inseridos {len(rel.adicionados)}; "
                    f"ignorados {len(rel.ignorados)}; "
                    f"totalizadores {', '.join(rel.totalizadores) or '—'}.")
                c1, c2, c3 = st.columns(3)
                c1.metric("Adicionados", len(rel.adicionados))
                c2.metric("Ignorados", len(rel.ignorados))
                c3.metric("Total de linhas", rel.total_linhas)
                st.success(
                    f"Totalizadores atualizados: "
                    f"{', '.join(rel.totalizadores)}  •  {rel.tempo_seg:.3f}s")
                if rel.ignorados:
                    st.dataframe(pd.DataFrame(
                        [{"Registro": r, "Motivo": m}
                         for r, m in rel.ignorados]),
                        use_container_width=True, hide_index=True)

# ---------------------------- Validar -------------------------------------- #
with aba_val:
    st.subheader("Validação estrutural")
    cval1, cval2 = st.columns([1, 1])
    with cval1:
        val_click = st.button("Validar estrutura completa", type="primary",
                              use_container_width=True)
    with cval2:
        rep_click = st.button("🛠️ Corrigir automaticamente (seguro)",
                              use_container_width=True)

    st.caption("A correção automática recalcula todos os totalizadores e "
               "remove duplicatas de registros únicos. Ela **não inventa "
               "valores** de campo: erros de conteúdo (campo obrigatório vazio, "
               "quantidade de campos divergente) são apenas listados para você "
               "resolver.")

    if val_click:
        ocs = ctrl.validar()
        n_erro = sum(1 for o in ocs if o.nivel == Nivel.ERRO)
        n_aviso = sum(1 for o in ocs if o.nivel == Nivel.AVISO)
        n_info = sum(1 for o in ocs if o.nivel == Nivel.INFO)
        registrar(f"Validação: {len(ocs)} ocorrência(s), {n_erro} erro(s).")
        c1, c2, c3 = st.columns(3)
        c1.metric("Erros", n_erro)
        c2.metric("Avisos", n_aviso)
        c3.metric("Infos", n_info)
        if not ocs:
            st.success("Nenhuma inconsistência encontrada. Estrutura íntegra.")
        else:
            df = pd.DataFrame([{"Nível": o.nivel.value, "Registro": o.registro,
                                "Linha": o.linha or "-", "Regra": o.regra,
                                "Mensagem": o.mensagem} for o in ocs])

            def _cor(v):
                m = {"ERRO": ERRO, "AVISO": WARN, "INFO": INFO}
                return f"color:{m.get(v,'')}; font-weight:600"
            st.dataframe(df.style.map(_cor, subset=["Nível"]),
                         use_container_width=True, hide_index=True, height=420)

    if rep_click:
        res = ctrl.reparar()
        registrar(f"Reparo: {len(res.duplicatas_removidas)} tipo(s) de "
                  f"duplicata; {len(res.totalizadores)} totalizadores; "
                  f"{len(res.pendencias)} pendência(s).")
        c1, c2, c3 = st.columns(3)
        c1.metric("Tipos de duplicata removidos", len(res.duplicatas_removidas))
        c2.metric("Totalizadores atualizados", len(res.totalizadores))
        c3.metric("Total de linhas", res.total_linhas)
        st.success("Correções seguras aplicadas. Baixe o arquivo na aba "
                   "**Exportar**.")

        if res.duplicatas_removidas:
            st.markdown("**Duplicatas removidas (registros únicos):**")
            st.dataframe(pd.DataFrame(
                [{"Registro": r, "Removidas": q}
                 for r, q in res.duplicatas_removidas]),
                use_container_width=True, hide_index=True)

        if res.pendencias:
            st.markdown("**Pendências que exigem sua decisão "
                        "(não corrigidas automaticamente):**")
            st.dataframe(pd.DataFrame({"Pendência": res.pendencias}),
                         use_container_width=True, hide_index=True, height=260)
        else:
            st.info("Nenhuma pendência de conteúdo. Estrutura pronta para o PVA.")

# ---------------------------- Exportar ------------------------------------- #
with aba_exp:
    st.subheader("Exportar arquivo compatível com o PVA")
    st.caption("Gera o .txt preservando encoding, quebras de linha e ordem.")
    dados = ctrl.exportar_bytes()
    st.metric("Linhas no arquivo", ctrl.arquivo.total_linhas)
    st.download_button(
        "⬇️  Baixar ECF (.txt)", data=dados,
        file_name="ECF_editada.txt", mime="text/plain", type="primary")

# ------------------------------- Log --------------------------------------- #
with st.sidebar:
    st.divider()
    st.caption("Log da sessão")
    for linha in st.session_state["log"][:12]:
        st.text(linha)
