"""Janela principal do Editor Inteligente de SPED ECF.

Reúne árvore da ECF, painel/dashboard, detalhe de registro, log e as ações
de importar, inserir, validar, recalcular e exportar. Operações pesadas
rodam em ``QThread`` para não travar a interface.
"""
from __future__ import annotations

import os
from typing import Callable, List, Optional

from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QAction, QColor, QFont
from PySide6.QtWidgets import (
    QFileDialog, QFrame, QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMessageBox, QPlainTextEdit, QProgressBar, QPushButton, QSplitter,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBar, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget,
)

from ..controller import ControladorECF, RelatorioOperacao
from ..core.validator import Nivel
from .insert_dialog import InsertDialog
from .settings import SettingsDialog
from .theme import ACCENT, ERRO, OK, WARN, Tema, aplicar_tema
from .validation_dialog import ValidationDialog

# --------------------------------------------------------------------------- #
# CONSTANTES DE INTERFACE
# --------------------------------------------------------------------------- #
TITULO = "Editor Inteligente de SPED ECF"
LARGURA_MIN = 1180
ALTURA_MIN = 720
ARVORE_LARGURA = 380


# --------------------------------------------------------------------------- #
# Worker genérico para operações pesadas
# --------------------------------------------------------------------------- #
class Worker(QThread):
    """Executa uma função em segundo plano e emite o resultado ou o erro."""

    concluido = Signal(object)
    falhou = Signal(str)

    def __init__(self, funcao: Callable, *args) -> None:
        super().__init__()
        self._funcao = funcao
        self._args = args

    def run(self) -> None:  # pragma: no cover - depende de thread/GUI
        try:
            self.concluido.emit(self._funcao(*self._args))
        except Exception as exc:  # noqa: BLE001
            self.falhou.emit(str(exc))


# --------------------------------------------------------------------------- #
# Cartão de KPI reutilizável
# --------------------------------------------------------------------------- #
class KpiCard(QFrame):
    def __init__(self, rotulo: str) -> None:
        super().__init__()
        self.setObjectName("Card")
        lay = QVBoxLayout(self)
        lay.setContentsMargins(16, 14, 16, 14)
        lay.setSpacing(4)
        self.lbl_valor = QLabel("—")
        self.lbl_valor.setObjectName("KpiValor")
        lbl_rot = QLabel(rotulo)
        lbl_rot.setObjectName("KpiRotulo")
        lay.addWidget(self.lbl_valor)
        lay.addWidget(lbl_rot)

    def definir(self, valor) -> None:
        self.lbl_valor.setText(str(valor))


# --------------------------------------------------------------------------- #
# Janela principal
# --------------------------------------------------------------------------- #
class JanelaPrincipal(QMainWindow):
    def __init__(self, controlador: ControladorECF, app) -> None:
        super().__init__()
        self.ctrl = controlador
        self.app = app
        self.tema = Tema.DARK
        self._worker: Optional[Worker] = None

        self.setWindowTitle(TITULO)
        self.setMinimumSize(LARGURA_MIN, ALTURA_MIN)

        self._montar_toolbar()
        self._montar_central()
        self._montar_status()
        self._atualizar_acoes()

    # ------------------------------------------------------------------ #
    # Construção da UI
    # ------------------------------------------------------------------ #
    def _montar_toolbar(self) -> None:
        tb = QToolBar()
        tb.setMovable(False)
        self.addToolBar(tb)

        self.act_importar = QAction("📂  Importar ECF", self)
        self.act_importar.triggered.connect(self.importar)
        tb.addAction(self.act_importar)

        self.act_inserir = QAction("➕  Inserir registros", self)
        self.act_inserir.triggered.connect(self.inserir)
        tb.addAction(self.act_inserir)

        self.act_validar = QAction("✓  Validar", self)
        self.act_validar.triggered.connect(self.validar)
        tb.addAction(self.act_validar)

        self.act_recalc = QAction("∑  Recalcular totalizadores", self)
        self.act_recalc.triggered.connect(self.recalcular)
        tb.addAction(self.act_recalc)

        self.act_exportar = QAction("💾  Exportar", self)
        self.act_exportar.triggered.connect(self.exportar)
        tb.addAction(self.act_exportar)

        espac = QWidget()
        espac.setSizePolicy(espac.sizePolicy().horizontalPolicy().Expanding,
                            espac.sizePolicy().verticalPolicy().Preferred)
        tb.addWidget(espac)

        self.act_tema = QAction("🌗  Tema", self)
        self.act_tema.triggered.connect(self.alternar_tema)
        tb.addAction(self.act_tema)

        self.act_config = QAction("⚙  Configurações", self)
        self.act_config.triggered.connect(self.abrir_config)
        tb.addAction(self.act_config)

    def _montar_central(self) -> None:
        split = QSplitter(Qt.Horizontal)

        # --- Árvore da ECF ---
        self.arvore = QTreeWidget()
        self.arvore.setHeaderLabels(["Estrutura", "Qtd."])
        self.arvore.setColumnWidth(0, 250)
        self.arvore.setAlternatingRowColors(True)
        self.arvore.itemClicked.connect(self._registro_selecionado)
        split.addWidget(self.arvore)

        # --- Painel de abas à direita ---
        self.abas = QTabWidget()
        self.abas.addTab(self._aba_painel(), "Painel")
        self.abas.addTab(self._aba_registro(), "Registro")
        self.abas.addTab(self._aba_log(), "Log")
        split.addWidget(self.abas)

        split.setSizes([ARVORE_LARGURA, LARGURA_MIN - ARVORE_LARGURA])
        split.setStretchFactor(1, 1)
        self.setCentralWidget(split)

    def _aba_painel(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(18, 18, 18, 18)
        lay.setSpacing(16)

        # Cabeçalho da empresa
        cab = QFrame()
        cab.setObjectName("Card")
        cl = QVBoxLayout(cab)
        cl.setContentsMargins(18, 16, 18, 16)
        self.lbl_empresa = QLabel("Nenhuma ECF carregada")
        self.lbl_empresa.setObjectName("H1")
        self.lbl_sub = QLabel("Importe um arquivo SPED ECF para começar.")
        self.lbl_sub.setObjectName("Fraco")
        cl.addWidget(self.lbl_empresa)
        cl.addWidget(self.lbl_sub)
        lay.addWidget(cab)

        # KPIs
        grid = QGridLayout()
        grid.setSpacing(14)
        self.kpi_linhas = KpiCard("Total de linhas")
        self.kpi_tipos = KpiCard("Tipos de registro")
        self.kpi_blocos = KpiCard("Blocos")
        self.kpi_versao = KpiCard("Leiaute")
        for i, k in enumerate((self.kpi_linhas, self.kpi_tipos,
                               self.kpi_blocos, self.kpi_versao)):
            grid.addWidget(k, 0, i)
        lay.addLayout(grid)

        # Status + blocos
        card_status = QFrame()
        card_status.setObjectName("Card")
        sl = QVBoxLayout(card_status)
        sl.setContentsMargins(18, 16, 18, 16)
        sl.setSpacing(10)
        t = QLabel("Situação estrutural")
        t.setObjectName("H2")
        sl.addWidget(t)
        self.lbl_status = QLabel("● Aguardando importação")
        self.lbl_status.setStyleSheet(f"color:{WARN}; font-weight:600;")
        sl.addWidget(self.lbl_status)
        self.lbl_blocos = QLabel("")
        self.lbl_blocos.setObjectName("Fraco")
        self.lbl_blocos.setWordWrap(True)
        sl.addWidget(self.lbl_blocos)
        lay.addWidget(card_status)

        lay.addStretch(1)
        return w

    def _aba_registro(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(18, 18, 18, 18)
        lay.setSpacing(12)

        self.lbl_reg_titulo = QLabel("Selecione um registro na árvore")
        self.lbl_reg_titulo.setObjectName("H2")
        lay.addWidget(self.lbl_reg_titulo)

        self.lbl_reg_meta = QLabel("")
        self.lbl_reg_meta.setObjectName("Fraco")
        self.lbl_reg_meta.setWordWrap(True)
        lay.addWidget(self.lbl_reg_meta)

        self.tab_campos = QTableWidget(0, 4)
        self.tab_campos.setHorizontalHeaderLabels(
            ["Nº", "Campo", "Tipo", "Obrigatório"])
        self.tab_campos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tab_campos.setAlternatingRowColors(True)
        self.tab_campos.verticalHeader().setVisible(False)
        self.tab_campos.horizontalHeader().setStretchLastSection(True)
        lay.addWidget(self.tab_campos, 1)
        return w

    def _aba_log(self) -> QWidget:
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(18, 18, 18, 18)
        self.txt_log = QPlainTextEdit()
        self.txt_log.setReadOnly(True)
        lay.addWidget(self.txt_log)
        return w

    def _montar_status(self) -> None:
        self.barra = self.statusBar()
        self.progress = QProgressBar()
        self.progress.setMaximumWidth(220)
        self.progress.setRange(0, 0)  # indeterminado
        self.progress.hide()
        self.barra.addPermanentWidget(self.progress)
        self.barra.showMessage("Pronto.")

    # ------------------------------------------------------------------ #
    # Estado das ações
    # ------------------------------------------------------------------ #
    def _tem_arquivo(self) -> bool:
        return self.ctrl.arquivo is not None

    def _atualizar_acoes(self) -> None:
        ok = self._tem_arquivo()
        for a in (self.act_inserir, self.act_validar,
                  self.act_recalc, self.act_exportar):
            a.setEnabled(ok)

    def _log(self, msg: str) -> None:
        self.txt_log.appendPlainText(msg)

    def _ocupado(self, on: bool, msg: str = "") -> None:
        self.progress.setVisible(on)
        for a in (self.act_importar, self.act_inserir, self.act_validar,
                  self.act_recalc, self.act_exportar, self.act_config):
            a.setEnabled(not on if a is not self.act_importar else not on)
        if on:
            self.barra.showMessage(msg)
        else:
            self.barra.showMessage("Pronto.")
            self._atualizar_acoes()

    # ------------------------------------------------------------------ #
    # Ações — Importar
    # ------------------------------------------------------------------ #
    def importar(self) -> None:
        caminho, _ = QFileDialog.getOpenFileName(
            self, "Importar arquivo SPED ECF", "",
            "Arquivos SPED (*.txt);;Todos os arquivos (*.*)")
        if not caminho:
            return
        self._ocupado(True, "Importando e interpretando a ECF…")
        self._rodar(lambda: self.ctrl.importar(caminho),
                    self._pos_importar,
                    f"Falha ao importar")

    def _pos_importar(self, _arq) -> None:
        self._ocupado(False)
        self._recarregar_visao()
        self._log(f"ECF importada: {self.ctrl.arquivo.total_linhas} linhas.")
        self.barra.showMessage("ECF importada com sucesso.", 5000)

    # ------------------------------------------------------------------ #
    # Ações — Inserir
    # ------------------------------------------------------------------ #
    def inserir(self) -> None:
        dlg = InsertDialog(self)
        if not dlg.exec():
            return
        texto = dlg.texto_registros()
        self._ocupado(True, "Validando e inserindo registros…")
        self._rodar(lambda: self.ctrl.inserir_texto(texto),
                    self._pos_inserir,
                    "Falha ao inserir")

    def _pos_inserir(self, rel: RelatorioOperacao) -> None:
        self._ocupado(False)
        erros = [o for o in rel.erros if o.nivel == Nivel.ERRO]
        if erros and not rel.adicionados:
            ValidationDialog(rel.erros, self).exec()
            self._log(f"Inserção abortada: {len(erros)} erro(s).")
            return
        self._recarregar_visao()
        self._log(
            f"Inseridos {len(rel.adicionados)} registro(s); "
            f"ignorados {len(rel.ignorados)}; "
            f"totalizadores {', '.join(rel.totalizadores) or '—'}; "
            f"{rel.tempo_seg:.3f}s.")
        QMessageBox.information(
            self, "Inserção concluída",
            f"Registros adicionados: {len(rel.adicionados)}\n"
            f"Registros ignorados: {len(rel.ignorados)}\n"
            f"Totalizadores atualizados: {len(rel.totalizadores)}\n"
            f"Total de linhas: {rel.total_linhas}\n"
            f"Tempo: {rel.tempo_seg:.3f}s")

    # ------------------------------------------------------------------ #
    # Ações — Validar
    # ------------------------------------------------------------------ #
    def validar(self) -> None:
        self._ocupado(True, "Validando estrutura completa…")
        self._rodar(self.ctrl.validar, self._pos_validar, "Falha ao validar")

    def _pos_validar(self, ocorrencias) -> None:
        self._ocupado(False)
        n_erro = sum(1 for o in ocorrencias if o.nivel == Nivel.ERRO)
        self._atualizar_status_estrutural(n_erro, len(ocorrencias))
        self._log(f"Validação: {len(ocorrencias)} ocorrência(s), "
                  f"{n_erro} erro(s).")
        ValidationDialog(ocorrencias, self).exec()

    # ------------------------------------------------------------------ #
    # Ações — Recalcular
    # ------------------------------------------------------------------ #
    def recalcular(self) -> None:
        self._ocupado(True, "Recalculando totalizadores…")
        self._rodar(self.ctrl.recalcular_totalizadores,
                    self._pos_recalcular, "Falha ao recalcular")

    def _pos_recalcular(self, rel: RelatorioOperacao) -> None:
        self._ocupado(False)
        self._recarregar_visao()
        self._log(f"Totalizadores recalculados: "
                  f"{', '.join(rel.totalizadores)} — "
                  f"total {rel.total_linhas} linhas.")
        self.barra.showMessage("Totalizadores atualizados.", 4000)

    # ------------------------------------------------------------------ #
    # Ações — Exportar
    # ------------------------------------------------------------------ #
    def exportar(self) -> None:
        caminho, _ = QFileDialog.getSaveFileName(
            self, "Exportar ECF", "ECF_editada.txt",
            "Arquivos SPED (*.txt)")
        if not caminho:
            return
        self._ocupado(True, "Gerando arquivo compatível com o PVA…")
        self._rodar(lambda: self.ctrl.exportar(caminho),
                    lambda n: self._pos_exportar(n, caminho),
                    "Falha ao exportar")

    def _pos_exportar(self, n: int, caminho: str) -> None:
        self._ocupado(False)
        self._log(f"Exportado: {os.path.basename(caminho)} ({n} linhas).")
        QMessageBox.information(
            self, "Exportação concluída",
            f"Arquivo gerado com {n} linhas.\n\n{caminho}")

    # ------------------------------------------------------------------ #
    # Configurações / Tema
    # ------------------------------------------------------------------ #
    def abrir_config(self) -> None:
        dlg = SettingsDialog(self.tema, self.ctrl.versao,
                             self.ctrl.layout.versoes, self)
        if not dlg.exec():
            return
        self.tema = dlg.tema_escolhido()
        aplicar_tema(self.app, self.tema)
        nova = dlg.versao_escolhida()
        if nova != self.ctrl.versao:
            self.ctrl.versao = nova
            self._log(f"Leiaute ativo alterado para {nova}.")
            if self._tem_arquivo():
                self._recarregar_visao()

    def alternar_tema(self) -> None:
        self.tema = Tema.LIGHT if self.tema == Tema.DARK else Tema.DARK
        aplicar_tema(self.app, self.tema)

    # ------------------------------------------------------------------ #
    # Infra de threads
    # ------------------------------------------------------------------ #
    def _rodar(self, funcao: Callable, ok: Callable, erro_prefixo: str) -> None:
        self._worker = Worker(funcao)
        self._worker.concluido.connect(ok)
        self._worker.falhou.connect(
            lambda m: self._erro(f"{erro_prefixo}: {m}"))
        self._worker.start()

    def _erro(self, msg: str) -> None:
        self._ocupado(False)
        self._log("ERRO: " + msg)
        QMessageBox.critical(self, "Erro", msg)

    # ------------------------------------------------------------------ #
    # Atualização da visão (árvore + painel)
    # ------------------------------------------------------------------ #
    def _recarregar_visao(self) -> None:
        self._preencher_arvore()
        self._preencher_painel()

    def _preencher_arvore(self) -> None:
        self.arvore.clear()
        arvore = self.ctrl.montar_arvore()
        raiz = QTreeWidgetItem([arvore["nome"], ""])
        f = raiz.font(0)
        f.setBold(True)
        raiz.setFont(0, f)
        self.arvore.addTopLevelItem(raiz)
        for bloco in arvore["blocos"]:
            item_b = QTreeWidgetItem([f"Bloco {bloco['letra']}", ""])
            fb = item_b.font(0)
            fb.setBold(True)
            item_b.setFont(0, fb)
            item_b.setForeground(0, QColor(ACCENT))
            raiz.addChild(item_b)
            for tipo in bloco["tipos"]:
                it = QTreeWidgetItem(
                    [f"{tipo['reg']}  {tipo['nome']}", str(tipo["qtd"])])
                it.setData(0, Qt.UserRole, tipo["reg"])
                item_b.addChild(it)
        raiz.setExpanded(True)

    def _preencher_painel(self) -> None:
        d = self.ctrl.dados_painel()
        if not d:
            return
        self.lbl_empresa.setText(d["empresa"] or "—")
        self.lbl_sub.setText(
            f"CNPJ {d['cnpj']}   •   Período {d['periodo']}   •   "
            f"{d['descricao_leiaute']}")
        self.kpi_linhas.definir(f"{d['linhas']:,}".replace(",", "."))
        self.kpi_tipos.definir(d["tipos"])
        self.kpi_blocos.definir(len(d["blocos"]))
        self.kpi_versao.definir(d["versao"])
        self.lbl_blocos.setText("Blocos presentes:  " + "   ".join(
            f"[{b}]" for b in d["blocos"]))
        self._atualizar_status_estrutural(None, None)

    def _atualizar_status_estrutural(self, n_erro, total) -> None:
        if n_erro is None:
            self.lbl_status.setText("● Importada — validação pendente")
            self.lbl_status.setStyleSheet(f"color:{WARN}; font-weight:600;")
        elif n_erro == 0:
            self.lbl_status.setText("● Estrutura íntegra — pronta para o PVA")
            self.lbl_status.setStyleSheet(f"color:{OK}; font-weight:600;")
        else:
            self.lbl_status.setText(
                f"● {n_erro} erro(s) estrutural(is) de {total} ocorrência(s)")
            self.lbl_status.setStyleSheet(f"color:{ERRO}; font-weight:600;")

    # ------------------------------------------------------------------ #
    # Seleção de registro na árvore
    # ------------------------------------------------------------------ #
    def _registro_selecionado(self, item: QTreeWidgetItem) -> None:
        reg = item.data(0, Qt.UserRole)
        if not reg:
            return
        info = self.ctrl.info_registro(reg)
        self.abas.setCurrentIndex(1)
        self.lbl_reg_titulo.setText(f"{info['reg']} — {info['nome']}")
        self.lbl_reg_meta.setText(
            f"Nível {info['nivel']}   •   Ocorrência: {info['ocorrencia']}   "
            f"•   Obrigatoriedade: {info['obrig']}   •   "
            f"Ocorrências no arquivo: {info['qtd']}")
        campos = info["campos"]
        self.tab_campos.setRowCount(len(campos))
        for i, c in enumerate(campos):
            self.tab_campos.setItem(i, 0, QTableWidgetItem(str(c["seq"])))
            self.tab_campos.setItem(i, 1, QTableWidgetItem(c["nome"]))
            self.tab_campos.setItem(i, 2, QTableWidgetItem(c["tipo"]))
            self.tab_campos.setItem(
                i, 3, QTableWidgetItem("Sim" if c["obrig"] else "Não"))
        self.tab_campos.resizeColumnsToContents()
        self.tab_campos.horizontalHeader().setStretchLastSection(True)
