# Editor Inteligente de SPED ECF

Software desktop para **edição inteligente de arquivos SPED ECF** (Escrituração
Contábil Fiscal). Importa a ECF original, permite inserir novos registros ou
blocos completos, valida toda a estrutura, **recalcula automaticamente todos os
totalizadores** e exporta um novo `.txt` compatível com o PVA da Receita
Federal — sem que o usuário edite o arquivo manualmente.

> O motor de totalizadores foi validado byte a byte contra uma ECF real de
> ~28 mil linhas: importar → exportar reproduz o arquivo **idêntico**; e após
> inserções os contadores (`X990`, `9900`, `9990`, `9999`) permanecem
> consistentes e idempotentes.

---

## Principais recursos

- **Importação** com detecção automática de encoding (latin-1/ISO-8859-1) e
  quebra de linha (CRLF), identificando empresa, CNPJ, período, versão do
  leiaute, blocos e contagens.
- **Árvore da ECF** (ECF → Blocos → Registros) com quantidade por tipo e
  detalhe de campos/descrição/ocorrências ao clicar.
- **Reclassificação de códigos (M300/M350)**: importe uma planilha De→Para e o
  sistema troca o `CODIGO` dos lançamentos no e-Lalur e no e-Lacs. A coluna de
  relacionamento define o vínculo: `PARTE B` casa pelo `COD_CTA_B` do M305/M355;
  um número de conta casa pelo `COD_CTA` do M310/M360. Duas regras apontando o
  mesmo lançamento para códigos diferentes geram **conflito** e a operação é
  interrompida — o sistema não escolhe por você.
- **Assistente em português**: descreva em linguagem natural o que precisa
  (`inserir M310 com COD_CTA = 1.01.01.001`, `no 0000, alterar NOME para ...`,
  `quantos M350 existem?`). O assistente consulta o leiaute do manual, monta o
  registro com o número de campos correto, mostra uma **prévia** (linha antes →
  linha depois) e só aplica após sua confirmação. Ele **nunca inventa valores**:
  se faltar um campo obrigatório, ele pergunta.
- **Correção automática segura**: remove duplicatas de registros de ocorrência
  única e recalcula todos os totalizadores; erros de conteúdo são listados para
  decisão do usuário, nunca preenchidos por conta própria.
- **Inserção inteligente**: cole registros (`|M310|...|`) ou importe um `.txt`;
  o sistema **localiza sozinho a posição correta** (ex.: `M310` entre `M001` e
  `M990`, respeitando a ordem canônica do leiaute) — nunca pede a linha ao
  usuário. Blocos ausentes são criados com seus registros de abertura e
  encerramento.
- **Validação** por regras independentes (classes): existência no leiaute,
  quantidade de campos, obrigatórios, hierarquia, pai/filho, duplicidade,
  datas, CNPJ, CPF e totalizadores, com relatório de erros/avisos.
- **Totalizadores automáticos** recalculados a cada operação.
- **Exportação** fiel: preserva encoding, quebras de linha, ordem e layout.
- **Painel/Dashboard** com KPIs, blocos presentes e indicadores coloridos.
- **Log** de operações com tempo de processamento, gravado em `logs/`.
- **Tema Dark/Light** corporativo.

## Tecnologia

Python 3.13+, **PySide6**, arquitetura **MVC**, orientação a objetos,
`dataclasses`, type hints, `logging` e `QThread` para operações pesadas.

## Estrutura

```
editor_ecf/
├── main.py                # ponto de entrada (QApplication)
├── controller.py          # Controlador (fachada MVC) — UI/CLI falam só com ele
├── core/                  # Motores (Model/serviços)
│   ├── parser.py          # leitura fiel do .txt → ArquivoECF
│   ├── layout_loader.py   # carrega os JSON de leiaute
│   ├── hierarchy.py       # níveis, pai/filho, árvore de exibição
│   ├── validator.py       # regras de validação (uma classe por regra)
│   ├── insertion.py       # inserção inteligente / posicionamento
│   ├── counter.py         # recálculo dos totalizadores (X990/9900/9990/9999)
│   └── exporter.py        # geração byte-fiel do .txt
├── models/                # registro.py, bloco.py, arquivo.py (dataclasses)
├── ui/                    # View (PySide6): janela, diálogos e tema
├── layouts/               # ecf_0012.json (regras dirigidas por dados)
├── tests/                 # pytest (round-trip, contador, inserção, validadores)
└── logs/                  # editor_ecf.log
```

## Instalação

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   |   Linux/Mac: source .venv/bin/activate
pip install -r editor_ecf/requirements.txt
```

## Execução

### Opção A — Streamlit (recomendada, mais simples)

```bash
pip install streamlit pandas
streamlit run editor_ecf/app.py
```

Abre no navegador. Envie o `.txt` da ECF na barra lateral e use as abas
Painel, Estrutura, Inserir, Validar e Exportar.

> Dica de Windows: no `cmd`, **cole apenas o comando**, não as linhas que
> começam com `#` (são comentários) nem dois comandos na mesma linha.

### Opção B — Desktop (PySide6)

```bash
python -m editor_ecf.main
# ou
python editor_ecf/main.py
```

## Testes

```bash
pip install pytest
pytest editor_ecf/tests -q
# round-trip byte-exato contra um arquivo real (opcional):
ECF_REAL=/caminho/para/SpedEcf.txt pytest editor_ecf/tests -q
```

## Motor de layout dirigido por dados

Nenhuma regra de estrutura é fixada em código. Cada versão da ECF é descrita
por um JSON em `layouts/` (`ecf_0012.json`, `ecf_0013.json`, …) contendo, por
registro: bloco, nível hierárquico, obrigatoriedade, ocorrência, se é abertura
ou encerramento, número e definição dos campos, além da ordem canônica dos
registros. **Para suportar uma nova versão, basta adicionar o JSON** — sem
tocar no código. O leiaute ativo é escolhido em *Configurações*.

O `ecf_0012.json` foi gerado a partir do *Manual de Orientação do Leiaute 12*
(Tabela de Registros + Leiaute dos Registros) e reconciliado com a contagem de
campos observada em arquivos reais.

## Como os totalizadores funcionam (resumo verificado)

- `X990` = quantidade de **todos** os registros do bloco *X*, incluindo o
  próprio abridor (`X001`/`0000`) e o encerrador (`X990`).
- `9900` = uma linha por tipo de registro existente no arquivo, com a
  contagem; ordenadas na **ordem canônica do leiaute**, seguidas da cauda fixa
  do bloco 9 (`9001`, `9100`*, `9990`, `9999`) e, por fim, o próprio `9900`.
- `9990` = total de registros do bloco 9.
- `9999` = total de linhas do arquivo inteiro.
- Registros `9100` (mensagens do PVA), quando presentes, são **preservados** e
  apenas contabilizados.

## Roadmap (preparado para evoluir)

Editor visual de registros, pesquisa inteligente, comparação entre duas ECFs,
importação da ECD/ECF anterior, exportação para Excel/PDF, histórico de
versões, undo/redo e modo auditor.
