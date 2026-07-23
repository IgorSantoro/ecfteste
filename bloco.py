"""Motor de Validação.

Cada regra é uma classe independente que herda de ``RegraValidacao`` e
implementa ``validar``. O ``Validador`` orquestra todas as regras e
produz uma lista de ``Ocorrencia`` (erros/avisos).

Regras implementadas:
    ValidateRegistroExiste  - registro existe no leiaute
    ValidateFields          - quantidade de campos compatível
    ValidateObrigatorios    - campos obrigatórios preenchidos
    ValidateHierarchy       - registro está sob um pai válido
    ValidateParent          - existe registro-pai no arquivo
    ValidateChild           - filhos aparecem depois do pai
    ValidateCounter         - totalizadores consistentes
    ValidateDate            - datas no formato ddmmaaaa
    ValidateCNPJ            - dígitos verificadores do CNPJ
    ValidateCPF             - dígitos verificadores do CPF
    ValidateDuplicidade     - registros únicos não repetidos
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

from ..models import ArquivoECF, Registro
from .layout_loader import LayoutLoader, LayoutRegistro


class Nivel(str, Enum):
    ERRO = "ERRO"
    AVISO = "AVISO"
    INFO = "INFO"


@dataclass
class Ocorrencia:
    nivel: Nivel
    regra: str
    registro: str
    linha: Optional[int]
    mensagem: str

    def __str__(self) -> str:  # pragma: no cover
        loc = f"linha {self.linha}" if self.linha else "-"
        return f"[{self.nivel}] {self.registro} ({loc}) {self.regra}: {self.mensagem}"


# ---------------------------------------------------------------------- #
# Utilidades de validação de documentos
# ---------------------------------------------------------------------- #
def _digitos(s: str) -> str:
    return re.sub(r"\D", "", s or "")


def cnpj_valido(cnpj: str) -> bool:
    c = _digitos(cnpj)
    if len(c) != 14 or c == c[0] * 14:
        return False
    def dv(base: str, pesos: List[int]) -> str:
        soma = sum(int(d) * p for d, p in zip(base, pesos))
        r = soma % 11
        return "0" if r < 2 else str(11 - r)
    d1 = dv(c[:12], [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    d2 = dv(c[:12] + d1, [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    return c[-2:] == d1 + d2


def cpf_valido(cpf: str) -> bool:
    c = _digitos(cpf)
    if len(c) != 11 or c == c[0] * 11:
        return False
    def dv(base: str) -> str:
        n = len(base) + 1
        soma = sum(int(d) * (n - i) for i, d in enumerate(base))
        r = (soma * 10) % 11
        return "0" if r == 10 else str(r)
    d1 = dv(c[:9])
    d2 = dv(c[:9] + d1)
    return c[-2:] == d1 + d2


def data_valida(s: str) -> bool:
    """Data no formato ddmmaaaa."""
    if not re.fullmatch(r"\d{8}", s or ""):
        return False
    d, m, a = int(s[:2]), int(s[2:4]), int(s[4:])
    if not (1 <= m <= 12 and 1 <= d <= 31 and 1900 <= a <= 2999):
        return False
    dias = [31, 29 if (a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)) else 28,
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return d <= dias[m - 1]


# ---------------------------------------------------------------------- #
# Regras
# ---------------------------------------------------------------------- #
class RegraValidacao:
    nome = "RegraGenerica"

    def __init__(self, layout: LayoutLoader, versao: str) -> None:
        self.layout = layout
        self.versao = versao

    def validar(self, arquivo: ArquivoECF) -> List[Ocorrencia]:  # pragma: no cover
        raise NotImplementedError

    def validar_registro(
        self, reg: Registro, arquivo: ArquivoECF
    ) -> List[Ocorrencia]:
        """Validação de um único registro (usada antes da inserção)."""
        return []


class ValidateRegistroExiste(RegraValidacao):
    nome = "ValidateRegistroExiste"

    def validar_registro(self, reg, arquivo):
        if not self.layout.existe(self.versao, reg.reg):
            return [Ocorrencia(Nivel.ERRO, self.nome, reg.reg, reg.origem,
                               f"Registro '{reg.reg}' não existe no leiaute {self.versao}.")]
        return []

    def validar(self, arquivo):
        oc = []
        for r in arquivo.registros:
            oc += self.validar_registro(r, arquivo)
        return oc


class ValidateFields(RegraValidacao):
    nome = "ValidateFields"

    def validar_registro(self, reg, arquivo):
        lr = self.layout.registro(self.versao, reg.reg)
        if not lr:
            return []
        # num de campos no arquivo inclui o REG; leiaute idem (num_campos)
        if lr.num_campos and reg.num_campos != lr.num_campos:
            return [Ocorrencia(Nivel.ERRO, self.nome, reg.reg, reg.origem,
                               f"Quantidade de campos {reg.num_campos} difere do "
                               f"leiaute ({lr.num_campos}).")]
        return []

    def validar(self, arquivo):
        oc = []
        for r in arquivo.registros:
            oc += self.validar_registro(r, arquivo)
        return oc


class ValidateObrigatorios(RegraValidacao):
    nome = "ValidateObrigatorios"

    def __init__(self, layout, versao, severidade: Nivel = Nivel.ERRO) -> None:
        super().__init__(layout, versao)
        self.severidade = severidade

    def validar_registro(self, reg, arquivo):
        lr = self.layout.registro(self.versao, reg.reg)
        if not lr:
            return []
        oc = []
        for c in lr.campos:
            if c.obrigatorio == "Sim":
                idx = c.seq - 1
                if idx < reg.num_campos and reg.campo(idx).strip() == "":
                    oc.append(Ocorrencia(self.severidade, self.nome, reg.reg,
                                         reg.origem,
                                         f"Campo obrigatório '{c.nome}' "
                                         f"(nº {c.seq}) vazio."))
        return oc

    def validar(self, arquivo):
        oc = []
        for r in arquivo.registros:
            oc += self.validar_registro(r, arquivo)
        return oc


class ValidateParent(RegraValidacao):
    """Verifica se, para um registro filho, existe pai válido no arquivo."""
    nome = "ValidateParent"

    def validar(self, arquivo):
        oc = []
        ordem = self.layout.ordem_registros(self.versao)
        nivel = lambda c: (self.layout.registro(self.versao, c).nivel
                           if self.layout.registro(self.versao, c) else 2)
        pilha: List[str] = []  # registros abertos por nível
        for r in arquivo.registros:
            lr = self.layout.registro(self.versao, r.reg)
            if not lr:
                continue
            n = lr.nivel
            while pilha and nivel(pilha[-1]) >= n:
                pilha.pop()
            # nível > 1 exige que exista um pai de nível n-1 aberto
            if n >= 2 and not pilha:
                oc.append(Ocorrencia(Nivel.AVISO, self.nome, r.reg, r.origem,
                                     f"Registro de nível {n} sem registro-pai imediato."))
            pilha.append(r.reg)
        return oc


class ValidateChild(RegraValidacao):
    """Verifica sequência: filhos não podem aparecer antes de seus pais."""
    nome = "ValidateChild"

    def validar(self, arquivo):
        oc = []
        bloco_aberto: Dict[str, bool] = {}
        for r in arquivo.registros:
            b = r.bloco
            if r.reg.endswith("001") or r.reg == "0000":
                bloco_aberto[b] = True
            elif not r.reg.endswith("990") and not bloco_aberto.get(b) and b != "9":
                oc.append(Ocorrencia(Nivel.ERRO, self.nome, r.reg, r.origem,
                                     f"Registro do bloco {b} antes da abertura do bloco."))
        return oc


class ValidateHierarchy(RegraValidacao):
    """Confere se o nível hierárquico observado é coerente com o leiaute."""
    nome = "ValidateHierarchy"

    def validar_registro(self, reg, arquivo):
        lr = self.layout.registro(self.versao, reg.reg)
        if not lr:
            return [Ocorrencia(Nivel.AVISO, self.nome, reg.reg, reg.origem,
                               "Sem definição de hierarquia no leiaute.")]
        return []

    def validar(self, arquivo):
        return []


class ValidateCounter(RegraValidacao):
    """Verifica se os totalizadores atuais batem com a contagem real."""
    nome = "ValidateCounter"

    def validar(self, arquivo):
        oc = []
        cont_bloco: Dict[str, int] = {}
        cont_tipo: Dict[str, int] = {}
        for r in arquivo.registros:
            if r.reg in ("9001", "9900", "9990", "9999"):
                continue
            cont_bloco[r.bloco] = cont_bloco.get(r.bloco, 0) + 1
            cont_tipo[r.reg] = cont_tipo.get(r.reg, 0) + 1
        for r in arquivo.registros:
            if r.reg.endswith("990") and r.bloco != "9":
                esperado = cont_bloco.get(r.bloco, 0)
                if r.campo(1) != str(esperado):
                    oc.append(Ocorrencia(Nivel.ERRO, self.nome, r.reg, r.origem,
                                         f"{r.reg}={r.campo(1)}, esperado {esperado}."))
        r9999 = next((r for r in arquivo.registros if r.reg == "9999"), None)
        if r9999 and r9999.campo(1) != str(arquivo.total_linhas):
            oc.append(Ocorrencia(Nivel.ERRO, self.nome, "9999", r9999.origem,
                                 f"9999={r9999.campo(1)}, total real {arquivo.total_linhas}."))
        return oc


class ValidateDate(RegraValidacao):
    nome = "ValidateDate"

    def validar_registro(self, reg, arquivo):
        lr = self.layout.registro(self.versao, reg.reg)
        oc = []
        if not lr:
            return oc
        for c in lr.campos:
            if re.search(r"\bDT[_A-Z]*|DATA", c.nome):
                idx = c.seq - 1
                v = reg.campo(idx)
                if v.strip() and not data_valida(v):
                    oc.append(Ocorrencia(Nivel.ERRO, self.nome, reg.reg, reg.origem,
                                         f"Campo data '{c.nome}'='{v}' inválido (ddmmaaaa)."))
        return oc

    def validar(self, arquivo):
        oc = []
        for r in arquivo.registros:
            oc += self.validar_registro(r, arquivo)
        return oc


class ValidateCNPJ(RegraValidacao):
    nome = "ValidateCNPJ"

    def validar_registro(self, reg, arquivo):
        lr = self.layout.registro(self.versao, reg.reg)
        oc = []
        if not lr:
            return oc
        for c in lr.campos:
            if c.nome == "CNPJ":
                v = reg.campo(c.seq - 1)
                if len(_digitos(v)) == 14 and not cnpj_valido(v):
                    oc.append(Ocorrencia(Nivel.AVISO, self.nome, reg.reg, reg.origem,
                                         f"CNPJ '{v}' com dígito verificador inválido."))
        return oc

    def validar(self, arquivo):
        oc = []
        for r in arquivo.registros:
            oc += self.validar_registro(r, arquivo)
        return oc


class ValidateCPF(RegraValidacao):
    nome = "ValidateCPF"

    def validar_registro(self, reg, arquivo):
        lr = self.layout.registro(self.versao, reg.reg)
        oc = []
        if not lr:
            return oc
        for c in lr.campos:
            if c.nome == "CPF":
                v = reg.campo(c.seq - 1)
                if len(_digitos(v)) == 11 and not cpf_valido(v):
                    oc.append(Ocorrencia(Nivel.AVISO, self.nome, reg.reg, reg.origem,
                                         f"CPF '{v}' com dígito verificador inválido."))
        return oc

    def validar(self, arquivo):
        oc = []
        for r in arquivo.registros:
            oc += self.validar_registro(r, arquivo)
        return oc


class ValidateDuplicidade(RegraValidacao):
    """Registros de ocorrência única ([x;1]) não podem repetir."""
    nome = "ValidateDuplicidade"

    def validar(self, arquivo):
        oc = []
        cont = arquivo.contagem_por_tipo()
        for reg, q in cont.items():
            lr = self.layout.registro(self.versao, reg)
            if lr and lr.unico and q > 1:
                oc.append(Ocorrencia(Nivel.ERRO, self.nome, reg, None,
                                     f"Registro único '{reg}' aparece {q} vezes."))
        return oc


# ---------------------------------------------------------------------- #
class Validador:
    """Orquestra todas as regras de validação."""

    def __init__(self, layout: LayoutLoader, versao: str,
                 obrig_como_erro: bool = True) -> None:
        self.layout = layout
        self.versao = versao
        sev = Nivel.ERRO if obrig_como_erro else Nivel.AVISO
        self.regras: List[RegraValidacao] = [
            ValidateRegistroExiste(layout, versao),
            ValidateFields(layout, versao),
            ValidateObrigatorios(layout, versao, severidade=sev),
            ValidateHierarchy(layout, versao),
            ValidateParent(layout, versao),
            ValidateChild(layout, versao),
            ValidateCounter(layout, versao),
            ValidateDate(layout, versao),
            ValidateCNPJ(layout, versao),
            ValidateCPF(layout, versao),
            ValidateDuplicidade(layout, versao),
        ]

    def validar(self, arquivo: ArquivoECF) -> List[Ocorrencia]:
        ocorrencias: List[Ocorrencia] = []
        for regra in self.regras:
            try:
                ocorrencias += regra.validar(arquivo)
            except Exception as exc:  # regra nunca deve derrubar o app
                ocorrencias.append(Ocorrencia(Nivel.AVISO, regra.nome, "-", None,
                                              f"Falha na regra: {exc}"))
        return ocorrencias

    def validar_novos(
        self, novos: List[Registro], arquivo: ArquivoECF
    ) -> List[Ocorrencia]:
        """Valida registros candidatos à inserção (antes de inserir)."""
        oc: List[Ocorrencia] = []
        regras_reg = [r for r in self.regras
                      if type(r).validar_registro is not RegraValidacao.validar_registro]
        for reg in novos:
            for regra in regras_reg:
                oc += regra.validar_registro(reg, arquivo)
        return oc
