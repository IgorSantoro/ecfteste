"""Motor de Inserção Inteligente.

Insere novos registros na posição correta **sem** que o usuário escolha a
linha. A posição é determinada pela ordem canônica do leiaute e pela
estrutura de blocos:

  1. Identifica o bloco de destino pelo primeiro caractere do REG.
  2. Localiza a janela do bloco (entre X001/abertura e X990/encerramento).
  3. Dentro do bloco, insere o registro logo após o último registro cuja
     posição canônica seja <= à do novo registro (e antes do encerrador),
     preservando a ordem oficial dos registros.

Ex.: um M300 é inserido entre M001 e M990, após os demais M300/M305 já
existentes e respeitando a ordem M300 < M305 < M310 ...
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from ..models import ArquivoECF, Registro
from .layout_loader import LayoutLoader


@dataclass
class ResultadoInsercao:
    inseridos: List[str] = field(default_factory=list)
    ignorados: List[Tuple[str, str]] = field(default_factory=list)  # (reg, motivo)
    posicoes: List[Tuple[str, int]] = field(default_factory=list)   # (reg, indice)

    @property
    def total_inseridos(self) -> int:
        return len(self.inseridos)


class InsercaoInteligente:
    def __init__(self, layout: LayoutLoader, versao: str) -> None:
        self.layout = layout
        self.versao = versao

    # ------------------------------------------------------------------ #
    def inserir(
        self, arquivo: ArquivoECF, novos: List[Registro]
    ) -> ResultadoInsercao:
        res = ResultadoInsercao()
        for novo in novos:
            if not self.layout.existe(self.versao, novo.reg):
                res.ignorados.append((novo.reg, "registro inexistente no leiaute"))
                continue
            pos = self._posicao_para(arquivo, novo)
            if pos is None:
                res.ignorados.append((novo.reg, f"bloco {novo.bloco} não encontrado"))
                continue
            arquivo.registros.insert(pos, novo)
            res.inseridos.append(novo.reg)
            res.posicoes.append((novo.reg, pos))
        return res

    # ------------------------------------------------------------------ #
    def _posicao_para(self, arquivo: ArquivoECF, novo: Registro) -> Optional[int]:
        """Calcula o índice de inserção para ``novo`` na lista de registros."""
        bloco = novo.bloco
        idx_novo = self.layout.indice_ordem(self.versao, novo.reg)

        # Localiza janela do bloco: [inicio_bloco, fim_bloco) na lista atual.
        inicio = None
        encerrador = None
        for i, r in enumerate(arquivo.registros):
            if r.bloco == bloco:
                if inicio is None:
                    inicio = i
                if r.reg.endswith("990"):
                    encerrador = i
        if inicio is None:
            # Bloco ainda não existe no arquivo: insere antes do bloco 9
            # (ou no fim) criando abertura/encerramento se necessário.
            return self._criar_bloco_e_posicao(arquivo, novo)

        limite = encerrador if encerrador is not None else self._fim_bloco(arquivo, bloco)

        # Percorre o bloco e para na primeira posição cujo registro tenha
        # índice canônico MAIOR que o do novo (ou no encerrador).
        pos = limite
        for i in range(inicio, limite + 1 if encerrador is None else limite):
            r = arquivo.registros[i]
            if r.reg.endswith("990"):
                pos = i
                break
            if self.layout.indice_ordem(self.versao, r.reg) > idx_novo:
                pos = i
                break
            pos = i + 1
        return pos

    # ------------------------------------------------------------------ #
    def _fim_bloco(self, arquivo: ArquivoECF, bloco: str) -> int:
        ult = 0
        for i, r in enumerate(arquivo.registros):
            if r.bloco == bloco:
                ult = i + 1
        return ult

    def _criar_bloco_e_posicao(
        self, arquivo: ArquivoECF, novo: Registro
    ) -> Optional[int]:
        """Cria abertura/encerramento do bloco e devolve a posição do dado.

        A abertura/encerramento seguem o leiaute; se o bloco não puder ser
        posicionado, retorna None.
        """
        bloco = novo.bloco
        ordem_blocos = self.layout._layouts[self.versao].get("blocos", [])
        if bloco not in ordem_blocos:
            return None
        rank = {b: i for i, b in enumerate(ordem_blocos)}
        # ponto de inserção do bloco: antes do primeiro bloco de rank maior
        ponto = None
        for i, r in enumerate(arquivo.registros):
            if rank.get(r.bloco, 99) > rank.get(bloco, 99):
                ponto = i
                break
        if ponto is None:
            ponto = len(arquivo.registros)

        abre = Registro(campos=[f"{bloco}001", "0"])
        fecha = Registro(campos=[f"{bloco}990", "3"])
        arquivo.registros.insert(ponto, abre)
        arquivo.registros.insert(ponto + 1, novo)
        arquivo.registros.insert(ponto + 2, fecha)
        return ponto + 1
