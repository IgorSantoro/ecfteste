"""Tema visual corporativo (Dark / Light) via QSS.

Paleta e métricas ficam concentradas em constantes no topo do módulo para
facilitar ajustes finos sem caçar valores espalhados pelo QSS.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

# --------------------------------------------------------------------------- #
# CONSTANTES DE PALETA — ajuste aqui para reestilizar todo o app
# --------------------------------------------------------------------------- #
ACCENT = "#1f9d8f"          # verde-petróleo corporativo (destaque principal)
ACCENT_HOVER = "#25b3a3"
ACCENT_PRESSED = "#17796e"

OK = "#2e9e5b"              # indicadores
WARN = "#d9a441"            # âmbar
ERRO = "#d9534f"
INFO = "#3a8dde"

RAIO = "8px"               # raio de borda padrão
FONTE = "Segoe UI, Inter, 'Noto Sans', Arial, sans-serif"
FONTE_MONO = "'Cascadia Code', 'JetBrains Mono', Consolas, 'Courier New', monospace"


@dataclass(frozen=True)
class Paleta:
    nome: str
    janela: str
    superficie: str
    superficie_alt: str
    borda: str
    texto: str
    texto_fraco: str
    cabecalho: str
    selecao: str


DARK = Paleta(
    nome="dark",
    janela="#0f1419",
    superficie="#161c24",
    superficie_alt="#1c2530",
    borda="#2a3542",
    texto="#e6edf3",
    texto_fraco="#8b97a5",
    cabecalho="#12181f",
    selecao="#1f9d8f",
)

LIGHT = Paleta(
    nome="light",
    janela="#eef1f4",
    superficie="#ffffff",
    superficie_alt="#f4f6f9",
    borda="#d5dbe2",
    texto="#1a2230",
    texto_fraco="#5c6773",
    cabecalho="#e3e8ee",
    selecao="#1f9d8f",
)


class Tema(str, Enum):
    DARK = "dark"
    LIGHT = "light"


def _qss(p: Paleta) -> str:
    return f"""
* {{
    font-family: {FONTE};
    font-size: 13px;
    color: {p.texto};
    outline: none;
}}
QWidget {{ background: {p.janela}; }}
QMainWindow, QDialog {{ background: {p.janela}; }}

/* ---------- Cartões / superfícies ---------- */
QFrame#Card, QGroupBox {{
    background: {p.superficie};
    border: 1px solid {p.borda};
    border-radius: {RAIO};
}}
QLabel#H1 {{ font-size: 19px; font-weight: 700; }}
QLabel#H2 {{ font-size: 15px; font-weight: 600; }}
QLabel#Fraco {{ color: {p.texto_fraco}; }}
QLabel#KpiValor {{ font-size: 22px; font-weight: 700; color: {ACCENT}; }}
QLabel#KpiRotulo {{ color: {p.texto_fraco}; font-size: 11px;
    text-transform: uppercase; letter-spacing: 1px; }}

/* ---------- Toolbar ---------- */
QToolBar {{
    background: {p.cabecalho};
    border: none;
    border-bottom: 1px solid {p.borda};
    padding: 6px 8px;
    spacing: 6px;
}}
QToolButton {{
    background: transparent;
    border: 1px solid transparent;
    border-radius: {RAIO};
    padding: 7px 12px;
    font-weight: 600;
}}
QToolButton:hover {{ background: {p.superficie_alt}; border-color: {p.borda}; }}
QToolButton:pressed {{ background: {p.borda}; }}

/* ---------- Botões ---------- */
QPushButton {{
    background: {p.superficie_alt};
    border: 1px solid {p.borda};
    border-radius: {RAIO};
    padding: 8px 16px;
    font-weight: 600;
}}
QPushButton:hover {{ border-color: {ACCENT}; }}
QPushButton:pressed {{ background: {p.borda}; }}
QPushButton#Primario {{
    background: {ACCENT}; border-color: {ACCENT}; color: #ffffff;
}}
QPushButton#Primario:hover {{ background: {ACCENT_HOVER}; border-color: {ACCENT_HOVER}; }}
QPushButton#Primario:pressed {{ background: {ACCENT_PRESSED}; }}
QPushButton:disabled {{ color: {p.texto_fraco}; border-color: {p.borda};
    background: {p.superficie}; }}

/* ---------- Árvore / tabelas ---------- */
QTreeWidget, QTableWidget, QListWidget, QTreeView, QTableView {{
    background: {p.superficie};
    border: 1px solid {p.borda};
    border-radius: {RAIO};
    alternate-background-color: {p.superficie_alt};
    selection-background-color: {ACCENT};
    selection-color: #ffffff;
}}
QHeaderView::section {{
    background: {p.cabecalho};
    color: {p.texto_fraco};
    border: none;
    border-bottom: 1px solid {p.borda};
    padding: 8px 10px;
    font-weight: 600;
}}
QTreeWidget::item, QTableWidget::item {{ padding: 4px 6px; }}
QTreeWidget::item:selected, QTableWidget::item:selected {{
    background: {ACCENT}; color: #ffffff;
}}

/* ---------- Entradas ---------- */
QLineEdit, QPlainTextEdit, QTextEdit, QComboBox, QSpinBox {{
    background: {p.superficie_alt};
    border: 1px solid {p.borda};
    border-radius: {RAIO};
    padding: 7px 10px;
    selection-background-color: {ACCENT};
}}
QPlainTextEdit, QTextEdit {{ font-family: {FONTE_MONO}; }}
QLineEdit:focus, QPlainTextEdit:focus, QComboBox:focus {{ border-color: {ACCENT}; }}
QComboBox::drop-down {{ border: none; width: 22px; }}
QComboBox QAbstractItemView {{
    background: {p.superficie}; border: 1px solid {p.borda};
    selection-background-color: {ACCENT}; selection-color: #fff;
}}

/* ---------- Abas ---------- */
QTabWidget::pane {{ border: 1px solid {p.borda}; border-radius: {RAIO};
    top: -1px; background: {p.superficie}; }}
QTabBar::tab {{
    background: transparent; color: {p.texto_fraco};
    padding: 9px 18px; border: none; font-weight: 600;
}}
QTabBar::tab:selected {{ color: {p.texto};
    border-bottom: 2px solid {ACCENT}; }}
QTabBar::tab:hover {{ color: {p.texto}; }}

/* ---------- Barras de rolagem ---------- */
QScrollBar:vertical {{ background: transparent; width: 12px; margin: 2px; }}
QScrollBar::handle:vertical {{ background: {p.borda}; border-radius: 6px;
    min-height: 30px; }}
QScrollBar::handle:vertical:hover {{ background: {p.texto_fraco}; }}
QScrollBar:horizontal {{ background: transparent; height: 12px; margin: 2px; }}
QScrollBar::handle:horizontal {{ background: {p.borda}; border-radius: 6px;
    min-width: 30px; }}
QScrollBar::add-line, QScrollBar::sub-line {{ height: 0; width: 0; }}

/* ---------- Status / progresso ---------- */
QStatusBar {{ background: {p.cabecalho}; border-top: 1px solid {p.borda};
    color: {p.texto_fraco}; }}
QProgressBar {{ background: {p.superficie_alt}; border: 1px solid {p.borda};
    border-radius: {RAIO}; text-align: center; height: 18px; }}
QProgressBar::chunk {{ background: {ACCENT}; border-radius: {RAIO}; }}

QSplitter::handle {{ background: {p.borda}; }}
QSplitter::handle:horizontal {{ width: 2px; }}
QToolTip {{ background: {p.cabecalho}; color: {p.texto};
    border: 1px solid {p.borda}; padding: 5px; border-radius: 6px; }}
"""


def paleta_de(tema: Tema) -> Paleta:
    return DARK if tema == Tema.DARK else LIGHT


def aplicar_tema(app, tema: Tema) -> None:
    """Aplica o QSS correspondente ao QApplication inteiro."""
    app.setStyleSheet(_qss(paleta_de(tema)))
