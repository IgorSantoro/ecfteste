"""Parser do arquivo SPED ECF (.txt).

Lê o arquivo preservando encoding (ISO-8859-1/latin-1) e terminadores de
linha (CRLF), constrói a árvore em memória (``ArquivoECF``) e extrai
metadados do registro 0000.
"""
from __future__ import annotations

from typing import Tuple

from ..models import ArquivoECF, Registro


class ParserECF:
    """Converte bytes do TXT em um ``ArquivoECF``."""

    def ler(self, caminho: str) -> ArquivoECF:
        with open(caminho, "rb") as fh:
            bruto = fh.read()
        return self.ler_bytes(bruto, caminho_original=caminho)

    def ler_bytes(self, bruto: bytes,
                  caminho_original: str = "") -> ArquivoECF:
        """Interpreta o conteúdo de uma ECF a partir de bytes (ex.: upload)."""
        encoding = self._detectar_encoding(bruto)
        nova_linha = "\r\n" if b"\r\n" in bruto else "\n"
        texto = bruto.decode(encoding, errors="replace")

        arquivo = ArquivoECF(
            encoding=encoding,
            nova_linha=nova_linha,
            caminho_original=caminho_original,
        )
        linhas = texto.split(nova_linha)
        num = 0
        for linha in linhas:
            if not linha.strip():
                continue
            num += 1
            # Um registro válido começa por '|' e possui pelo menos |REG|
            if not linha.startswith("|"):
                continue
            arquivo.registros.append(Registro.de_linha(linha, origem=num))

        arquivo.atualizar_metadados_do_0000()
        return arquivo

    def ler_texto(self, texto: str) -> list[Registro]:
        """Interpreta um trecho colado (várias linhas ``|REG|...|``)."""
        registros: list[Registro] = []
        for linha in texto.replace("\r\n", "\n").split("\n"):
            linha = linha.strip()
            if not linha or not linha.startswith("|"):
                continue
            registros.append(Registro.de_linha(linha))
        return registros

    # ------------------------------------------------------------------ #
    @staticmethod
    def _detectar_encoding(bruto: bytes) -> str:
        """SPED ECF usa ISO-8859-1. Tenta UTF-8 só como fallback seguro."""
        try:
            bruto.decode("utf-8")
            # Se decodifica em UTF-8 sem erro E contém acentos multibyte,
            # ainda assim mantemos latin-1 como padrão do SPED, exceto se
            # houver BOM/estrutura UTF-8 clara.
            if bruto.startswith(b"\xef\xbb\xbf"):
                return "utf-8-sig"
        except UnicodeDecodeError:
            pass
        return "latin-1"
