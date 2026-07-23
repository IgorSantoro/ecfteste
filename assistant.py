"""Motor de Exportação.

Gera um novo arquivo .txt preservando:
  * encoding original (ISO-8859-1/latin-1);
  * terminadores de linha (CRLF);
  * ordem dos registros;
  * formato SPED (``|campo|campo|``).

O arquivo resultante é compatível com importação no PVA da Receita.
"""
from __future__ import annotations

from ..models import ArquivoECF


class Exportador:
    def exportar(self, arquivo: ArquivoECF, caminho: str) -> int:
        """Escreve a ECF em ``caminho``. Retorna o número de linhas gravadas."""
        linhas = [r.para_linha() for r in arquivo.registros]
        conteudo = arquivo.nova_linha.join(linhas) + arquivo.nova_linha
        dados = conteudo.encode(arquivo.encoding, errors="replace")
        with open(caminho, "wb") as fh:
            fh.write(dados)
        return len(linhas)

    def para_bytes(self, arquivo: ArquivoECF) -> bytes:
        linhas = [r.para_linha() for r in arquivo.registros]
        conteudo = arquivo.nova_linha.join(linhas) + arquivo.nova_linha
        return conteudo.encode(arquivo.encoding, errors="replace")
