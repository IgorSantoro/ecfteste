{
  "versao": "0012",
  "descricao": "Leiaute 12 da ECF - ADE Cofis 02/2026 (AC 2025 / Sit.Esp. 2026)",
  "blocos": [
    "0",
    "9",
    "C",
    "E",
    "J",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y"
  ],
  "ordem_registros": [
    "0000",
    "0001",
    "0010",
    "0020",
    "0021",
    "0030",
    "0035",
    "0930",
    "0990",
    "C001",
    "C040",
    "C050",
    "C051",
    "C053",
    "C100",
    "C150",
    "C155",
    "C157",
    "C350",
    "C355",
    "C990",
    "E001",
    "E010",
    "E015",
    "E020",
    "E030",
    "E155",
    "E355",
    "E990",
    "J001",
    "J050",
    "J051",
    "J053",
    "J100",
    "J990",
    "K001",
    "K030",
    "K155",
    "K156",
    "K355",
    "K356",
    "K915",
    "K935",
    "K990",
    "L001",
    "L030",
    "L100",
    "L200",
    "L210",
    "L300",
    "L990",
    "M001",
    "M010",
    "M030",
    "M300",
    "M305",
    "M310",
    "M312",
    "M315",
    "M350",
    "M355",
    "M360",
    "M362",
    "M365",
    "M410",
    "M415",
    "M500",
    "M510",
    "M990",
    "N001",
    "N030",
    "N500",
    "N600",
    "N605",
    "N610",
    "N615",
    "N620",
    "N630",
    "N650",
    "N660",
    "N670",
    "N990",
    "P001",
    "P030",
    "P100",
    "P130",
    "P150",
    "P200",
    "P230",
    "P300",
    "P400",
    "P500",
    "P990",
    "Q001",
    "Q100",
    "Q990",
    "S001",
    "S030",
    "S100",
    "S150",
    "S200",
    "S300",
    "S500",
    "S700",
    "S990",
    "T001",
    "T030",
    "T120",
    "T150",
    "T170",
    "T181",
    "T990",
    "U001",
    "U030",
    "U100",
    "U150",
    "U180",
    "U182",
    "U990",
    "V001",
    "V010",
    "V020",
    "V030",
    "V100",
    "V990",
    "W001",
    "W100",
    "W200",
    "W250",
    "W300",
    "W990",
    "X001",
    "X280",
    "X292",
    "X340",
    "X350",
    "X351",
    "X352",
    "X353",
    "X354",
    "X355",
    "X356",
    "X357",
    "X360",
    "X365",
    "X366",
    "X370",
    "X371",
    "X375",
    "X390",
    "X400",
    "X410",
    "X420",
    "X430",
    "X450",
    "X451",
    "X460",
    "X470",
    "X480",
    "X485",
    "X490",
    "X500",
    "X510",
    "X990",
    "Y001",
    "Y520",
    "Y570",
    "Y590",
    "Y600",
    "Y612",
    "Y620",
    "Y630",
    "Y640",
    "Y650",
    "Y660",
    "Y672",
    "Y680",
    "Y681",
    "Y682",
    "Y720",
    "Y730",
    "Y750",
    "Y800",
    "Y990",
    "9001",
    "9099",
    "9100",
    "9900",
    "9990",
    "9999"
  ],
  "registros": {
    "0000": {
      "registro": "0000",
      "bloco": "0",
      "nivel": 0,
      "nome": "Abertura do Arquivo Digital e Identificação da Pessoa Jurídica",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 15,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "NOME_ESC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_VER",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "CNPJ",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NOME",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "IND_SIT_INI_PER",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "SIT_ESPECIAL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "PAT_REMAN_CIS",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 9,
          "nome": "DT_SIT_ESP",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 10,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 12,
          "nome": "RETIFICADORA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 13,
          "nome": "NUM_REC",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 14,
          "nome": "TIP_ECF",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 15,
          "nome": "COD_SCP",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "0001": {
      "registro": "0001",
      "bloco": "0",
      "nivel": 1,
      "nome": "Abertura do Bloco 0",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "0010": {
      "registro": "0010",
      "bloco": "0",
      "nivel": 2,
      "nome": "Parâmetros de Tributação",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 13,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "HASH_ECF_ANTERIOR",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 3,
          "nome": "OPT_REFIS",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "FORMA_TRIB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "FORMA_APUR",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "COD_QUALIF_PJ",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "FORMA_TRIB_PER",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "MES_BAL_RED",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 9,
          "nome": "TIP_ESC_PRE",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 10,
          "nome": "TIP_ENT",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 11,
          "nome": "FORMA_APUR_I",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 12,
          "nome": "APUR_CSLL",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 13,
          "nome": "IND_REC_RECEITA",
          "tipo": "N",
          "obrigatorio": "Não"
        }
      ]
    },
    "0020": {
      "registro": "0020",
      "bloco": "0",
      "nivel": 2,
      "nome": "Parâmetros Complementares",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 32,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_ALIQ_CSLL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "IND_QTE_SCP",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_ADM_FUN_CLU",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_PART_CONS",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "IND_OP_EXT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "IND_OP_VINC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "IND_PJ_ENQUAD",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "IND_PART_EXT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "IND_ATIV_RURAL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "IND_LUC_EXP",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 12,
          "nome": "IND_RED_ISEN",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 13,
          "nome": "IND_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 14,
          "nome": "IND_PART_COLIG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 15,
          "nome": "IND_",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 16,
          "nome": "IND_ATIV_EXT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 17,
          "nome": "IND_PGTO_EXT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 18,
          "nome": "IND_E",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 19,
          "nome": "IND_ROY_REC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 20,
          "nome": "IND_ROY_PAG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 21,
          "nome": "IND_REND_SERV",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 22,
          "nome": "IND_PGTO_REM",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 23,
          "nome": "IND_INOV_TEC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 24,
          "nome": "IND_CAP_INF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 25,
          "nome": "IND_PJ_HAB",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 26,
          "nome": "IND_POLO_AM",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 27,
          "nome": "IND_ZON_EXP",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 28,
          "nome": "IND_AREA_COM",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 29,
          "nome": "IND_PAIS_A_PAIS",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 30,
          "nome": "IND_DEREX",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 31,
          "nome": "POSSUI_CEBRAS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 32,
          "nome": "CEBAS",
          "tipo": "C",
          "obrigatorio": ""
        }
      ]
    },
    "0021": {
      "registro": "0021",
      "bloco": "0",
      "nivel": 2,
      "nome": "Parâmetros de Identificação dos Tipos de Programa",
      "obrig_entrada": "F",
      "ocorrencia": "[0;1]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 13,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_REPES",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 3,
          "nome": "IND_RECAP",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "IND_PADIS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "IND_REIDI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "IND_RECINE",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "IND_RETID",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "IND_OLEO_BUNKER",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "IND_REPORTO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 10,
          "nome": "IND_RET_II",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 11,
          "nome": "IND_RET_PMCMV",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 12,
          "nome": "IND_RET_EEI",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 13,
          "nome": "IND_EBAS",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "0030": {
      "registro": "0030",
      "bloco": "0",
      "nivel": 2,
      "nome": "Dados Cadastrais",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 12,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_NAT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "CNAE_FISCAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "ENDERECO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NUM",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "COMPL",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "BAIRRO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "UF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "COD_MUN",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "CEP",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "NUM_TEL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 12,
          "nome": "EMAIL",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "0035": {
      "registro": "0035",
      "bloco": "0",
      "nivel": 2,
      "nome": "Identificação das SCP",
      "obrig_entrada": "F",
      "ocorrencia": "[0:N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 3,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_SCP",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NOME_SCP",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "0930": {
      "registro": "0930",
      "bloco": "0",
      "nivel": 2,
      "nome": "Identificação dos Signatários da ECF F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 7,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IDENT_NOM",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "IDENT_CPF_CNPJ",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IDENT_QUALIF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_CRC",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "EMAIL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "FONE",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "0990": {
      "registro": "0990",
      "bloco": "0",
      "nivel": 1,
      "nome": "Encerramento do Bloco 0",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "9001": {
      "registro": "9001",
      "bloco": "9",
      "nivel": 1,
      "nome": "Abertura do Bloco 9",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "9099": {
      "registro": "9099",
      "bloco": "9",
      "nivel": 1,
      "nome": "Encerramento do Bloco 9",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 1,
      "campos": [
        {
          "seq": 1,
          "nome": "CAMPO_1",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "9100": {
      "registro": "9100",
      "bloco": "9",
      "nivel": 2,
      "nome": "Avisos da Escrituração F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 17,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "NOM_REGRA",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 3,
          "nome": "MSG_REGRA",
          "tipo": "C",
          "obrigatorio": ""
        },
        {
          "seq": 4,
          "nome": "REGISTRO",
          "tipo": "C",
          "obrigatorio": ""
        },
        {
          "seq": 5,
          "nome": "CAMPO",
          "tipo": "C",
          "obrigatorio": ""
        },
        {
          "seq": 6,
          "nome": "CAMPO_6",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 7,
          "nome": "CAMPO_7",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 8,
          "nome": "CAMPO_8",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 9,
          "nome": "CAMPO_9",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 10,
          "nome": "CAMPO_10",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 11,
          "nome": "CAMPO_11",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 12,
          "nome": "CAMPO_12",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 13,
          "nome": "CAMPO_13",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 14,
          "nome": "CAMPO_14",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 15,
          "nome": "CAMPO_15",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 16,
          "nome": "CAMPO_16",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 17,
          "nome": "CAMPO_17",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "9900": {
      "registro": "9900",
      "bloco": "9",
      "nivel": 2,
      "nome": "Registros do Arquivo",
      "obrig_entrada": "O",
      "ocorrencia": "[1;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 5,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "REG_BLC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "QTD_REG_BLC",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "VERSAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "ID_TAB_DIN",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "9990": {
      "registro": "9990",
      "bloco": "9",
      "nivel": 1,
      "nome": "Encerramento do Bloco 9",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "9999": {
      "registro": "9999",
      "bloco": "9",
      "nivel": 1,
      "nome": "Encerramento do Arquivo Digital",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "C001": {
      "registro": "C001",
      "bloco": "C",
      "nivel": 1,
      "nome": "Abertura do Bloco C – Informações Recuperadas da ECD",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "C040": {
      "registro": "C040",
      "bloco": "C",
      "nivel": 2,
      "nome": "Identificador da ECD",
      "obrig_entrada": "N",
      "ocorrencia": "[0;12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 16,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "HASH_ECD",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_SIT_ESP",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "CNPJ",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "NUM_ORD",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "NIRE",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 9,
          "nome": "NAT_LIVR",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "COD_VER_LC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "IND_ESC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 12,
          "nome": "IDENT_MF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 13,
          "nome": "CAMPO_13",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 14,
          "nome": "CAMPO_14",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 15,
          "nome": "CAMPO_15",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 16,
          "nome": "CAMPO_16",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "C050": {
      "registro": "C050",
      "bloco": "C",
      "nivel": 3,
      "nome": "Plano de Contas da ECD",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 8,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_ALT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "CAMPO_5",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 6,
          "nome": "CAMPO_6",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 7,
          "nome": "CAMPO_7",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 8,
          "nome": "CAMPO_8",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "C051": {
      "registro": "C051",
      "bloco": "C",
      "nivel": 4,
      "nome": "Plano de Contas Referencial Preenchido na ECD",
      "obrig_entrada": "N",
      "ocorrencia": "[0:N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 3,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 3,
          "nome": "COD_CTA_REF",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "C053": {
      "registro": "C053",
      "bloco": "C",
      "nivel": 4,
      "nome": "Subcontas Correlatas",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_IDT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CNT_CORR",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "NAT_SUB_CNT",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "C100": {
      "registro": "C100",
      "bloco": "C",
      "nivel": 3,
      "nome": "Centro de Custos",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_ALT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "CCUS",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "C150": {
      "registro": "C150",
      "bloco": "C",
      "nivel": 3,
      "nome": "Identificação do Período dos Saldos Periódicos das Contas",
      "obrig_entrada": "N",
      "ocorrencia": "[0;13]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 3,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "C155": {
      "registro": "C155",
      "bloco": "C",
      "nivel": 4,
      "nome": "Detalhes dos Saldos Contábeis das Contas",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 10,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VL_SLD_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_VL_SLD_INI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_DEB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "VL_CRED",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "VL_SLD_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "IND_VL_SLD_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "LINHA_ECD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "C157": {
      "registro": "C157",
      "bloco": "C",
      "nivel": 5,
      "nome": "Transferência de Saldos do Plano de Contas Anterior",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 6,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VL_SLD_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_VL_SLD_FIN",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "LINHA_ECD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "C350": {
      "registro": "C350",
      "bloco": "C",
      "nivel": 3,
      "nome": "Identificação da Data dos Saldos das Contas de Resultado Antes do Encerramento",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_RES",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "C355": {
      "registro": "C355",
      "bloco": "C",
      "nivel": 4,
      "nome": "Detalhes dos Saldos das Contas de Resultado Antes do Encerramento",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 6,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VL_CTA",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_VL_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "LINHA_ECD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "C990": {
      "registro": "C990",
      "bloco": "C",
      "nivel": 1,
      "nome": "Encerramento do Bloco C",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "E001": {
      "registro": "E001",
      "bloco": "E",
      "nivel": 1,
      "nome": "ECF Anterior e Cálculo Fiscal dos Dados Recuperados",
      "obrig_entrada": "O",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "E010": {
      "registro": "E010",
      "bloco": "E",
      "nivel": 2,
      "nome": "Saldos Finais Recuperados da ECF Anterior",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 6,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CTA_REF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "DESC_CTA_REF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "VAL_CTA_REF",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "IND_VAL_CTA_REF",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "E015": {
      "registro": "E015",
      "bloco": "E",
      "nivel": 3,
      "nome": "Contas Contábeis Mapeadas",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 6,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "DESC_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "VAL_CTA",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "IND_VAL_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "E020": {
      "registro": "E020",
      "bloco": "E",
      "nivel": 2,
      "nome": "Saldos Finais das Contas na Parte B do e-Lalur da ECF Imediatamente Anterior",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 9,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA_B",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESC_CTA_LAL",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "DT_AP_LAL",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "DT_LIM_LAL",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "TRIBUTO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "VL_SALDO_FIN",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "IND_VL_SALDO_FIN",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 9,
          "nome": "COD_PB_RFB",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "E030": {
      "registro": "E030",
      "bloco": "E",
      "nivel": 2,
      "nome": "Identificação do Período",
      "obrig_entrada": "N",
      "ocorrencia": "[0;13]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "E155": {
      "registro": "E155",
      "bloco": "E",
      "nivel": 3,
      "nome": "Detalhes dos Saldos Contábeis Calculados com Base nas ECD",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 9,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VL_SLD_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_VL_SLD_INI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_DEB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "VL_CRED",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "VL_SLD_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "IND_VL_SLD_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "E355": {
      "registro": "E355",
      "bloco": "E",
      "nivel": 3,
      "nome": "Detalhes dos Saldos das Contas de Resultado Antes do Encerramento",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 5,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VL_SLD_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_VL_SLD_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "E990": {
      "registro": "E990",
      "bloco": "E",
      "nivel": 1,
      "nome": "Encerramento do Bloco E N",
      "obrig_entrada": "N",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "J001": {
      "registro": "J001",
      "bloco": "J",
      "nivel": 1,
      "nome": "Abertura do Bloco J – Plano de Contas e Mapeamento F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "J050": {
      "registro": "J050",
      "bloco": "J",
      "nivel": 2,
      "nome": "Plano de Contas do Contribuinte",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 8,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_ALT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NIVEL",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 6,
          "nome": "CAMPO_6",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 7,
          "nome": "CAMPO_7",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 8,
          "nome": "CAMPO_8",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "J051": {
      "registro": "J051",
      "bloco": "J",
      "nivel": 3,
      "nome": "Plano de Contas Referencial",
      "obrig_entrada": "F",
      "ocorrencia": "[1:N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 3,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 3,
          "nome": "COD_CTA_REF",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "J053": {
      "registro": "J053",
      "bloco": "J",
      "nivel": 3,
      "nome": "Subcontas Correlatas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_IDT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CNT_CORR",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "NAT_SUB_CNT",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "J100": {
      "registro": "J100",
      "bloco": "J",
      "nivel": 2,
      "nome": "Centro de Custos",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_ALT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "CCUS",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "J990": {
      "registro": "J990",
      "bloco": "J",
      "nivel": 1,
      "nome": "Encerramento do Bloco J F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "K001": {
      "registro": "K001",
      "bloco": "K",
      "nivel": 1,
      "nome": "Abertura do Bloco K – Saldos das Contas Contábeis e Referencial",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "K030": {
      "registro": "K030",
      "bloco": "K",
      "nivel": 2,
      "nome": "Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário",
      "obrig_entrada": "F",
      "ocorrencia": "[0;13]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "K155": {
      "registro": "K155",
      "bloco": "K",
      "nivel": 3,
      "nome": "Detalhes dos Saldos Contábeis (Depois do Encerramento do Resultado do Período)",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 9,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VL_SLD_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_VL_SLD_INI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_DEB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "VL_CRED",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "VL_SLD_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "IND_VL_SLD_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "K156": {
      "registro": "K156",
      "bloco": "K",
      "nivel": 4,
      "nome": "Mapeamento Referencial do Saldo",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 8,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA_REF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "VL_SLD_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_VL_SLD_INI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "VL_DEB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_CRED",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "VL_SLD_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "IND_VL_SLD_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "K355": {
      "registro": "K355",
      "bloco": "K",
      "nivel": 3,
      "nome": "Saldos Finais das Contas Contábeis de Resultado antes do Encerramento",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 5,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VL_SLD_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_VL_SLD_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "K356": {
      "registro": "K356",
      "bloco": "K",
      "nivel": 4,
      "nome": "Mapeamento Referencial dos Saldos Finais das Contas Contábeis de Resultado Antes do Encerramento",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA_REF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "VL_SLD_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_VL_SLD_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "K915": {
      "registro": "K915",
      "bloco": "K",
      "nivel": 2,
      "nome": "Justificativa para Divergência nas Contas Patrimoniais",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 18,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "ID_REGRA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_SLD_INI_ESP",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 7,
          "nome": "IND_VL_SLD_INI_ESP",
          "tipo": "C",
          "obrigatorio": ""
        },
        {
          "seq": 8,
          "nome": "VL_DEB_ESP",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 9,
          "nome": "VL_CRED_ESP",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 10,
          "nome": "VL_SLD_FIN_ESP",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 11,
          "nome": "IND_VL_SLD_FIN_ESP",
          "tipo": "C",
          "obrigatorio": ""
        },
        {
          "seq": 12,
          "nome": "SLD_INI_PRE",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 13,
          "nome": "IND_SLD_INI_PRE",
          "tipo": "C",
          "obrigatorio": ""
        },
        {
          "seq": 14,
          "nome": "VL_DEB_PRE",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 15,
          "nome": "VL_CRED_PRE",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 16,
          "nome": "SLD_FIN_PRE",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 17,
          "nome": "IND_SLD_FIN_PRE",
          "tipo": "C",
          "obrigatorio": ""
        },
        {
          "seq": 18,
          "nome": "JUSTIFICATIVA",
          "tipo": "C",
          "obrigatorio": ""
        }
      ]
    },
    "K935": {
      "registro": "K935",
      "bloco": "K",
      "nivel": 2,
      "nome": "Justificativa para Divergência nas Contas de Resultado",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 10,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "ID_REGRA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_SLD_FIN_ESP",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 7,
          "nome": "IND_VL_SLD_FIN_ESP",
          "tipo": "C",
          "obrigatorio": ""
        },
        {
          "seq": 8,
          "nome": "SLD_FIN_PRE",
          "tipo": "N",
          "obrigatorio": ""
        },
        {
          "seq": 9,
          "nome": "IND_SLD_FIN_PRE",
          "tipo": "C",
          "obrigatorio": ""
        },
        {
          "seq": 10,
          "nome": "JUSTIFICATIVA",
          "tipo": "C",
          "obrigatorio": ""
        }
      ]
    },
    "K990": {
      "registro": "K990",
      "bloco": "K",
      "nivel": 1,
      "nome": "Encerramento do Bloco K F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "L001": {
      "registro": "L001",
      "bloco": "L",
      "nivel": 1,
      "nome": "Abertura do Bloco L – Lucro Real F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "L030": {
      "registro": "L030",
      "bloco": "L",
      "nivel": 2,
      "nome": "Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL no Ano-Calendário",
      "obrig_entrada": "F",
      "ocorrencia": "[0;13]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "L100": {
      "registro": "L100",
      "bloco": "L",
      "nivel": 3,
      "nome": "Balanço Patrimonial",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 13,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "TIPO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NIVEL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "COD_CTA_SUP",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VAL_CTA_REF_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "IND_VAL_CTA_REF_INI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "VAL_CTA_REF_DEB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "VAL_CTA_REF_CRED",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 12,
          "nome": "VAL_CTA_REF_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 13,
          "nome": "CAMPO_13",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "L200": {
      "registro": "L200",
      "bloco": "L",
      "nivel": 3,
      "nome": "Método de Avaliação do Estoque Final",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_AVAL_ESTOQ",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "L210": {
      "registro": "L210",
      "bloco": "L",
      "nivel": 3,
      "nome": "Informativo da Composição de Custos",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "L300": {
      "registro": "L300",
      "bloco": "L",
      "nivel": 3,
      "nome": "Demonstração do Resultado Líquido no Período Fiscal",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 9,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "TIPO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NIVEL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "COD_CTA_SUP",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VALOR",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "CAMPO_9",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "L990": {
      "registro": "L990",
      "bloco": "L",
      "nivel": 1,
      "nome": "Encerramento do Bloco L F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M001": {
      "registro": "M001",
      "bloco": "M",
      "nivel": 1,
      "nome": "do Lucro Real (e-Lalur) e Livro Eletrônico de F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M010": {
      "registro": "M010",
      "bloco": "M",
      "nivel": 2,
      "nome": "Identificação da Conta na Parte B e-Lalur e do e-Lacs",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 10,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA_B",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESC_CTA_LAL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "DT_AP_LAL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "COD_PB_RFB",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "DT_LIM_LAL",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "COD_TRIBUTO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "VL_SALDO_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "IND_VL_SALDO_INI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "CNPJ_SIT_ESP",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "M030": {
      "registro": "M030",
      "bloco": "M",
      "nivel": 2,
      "nome": "Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real",
      "obrig_entrada": "F",
      "ocorrencia": "[0;13]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M300": {
      "registro": "M300",
      "bloco": "M",
      "nivel": 3,
      "nome": "Demonstração do Lucro Real",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 7,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "TIPO_LANCAMENTO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "IND_RELACAO",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "VALOR",
          "tipo": "",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "HIST_LAN_LAL",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "M305": {
      "registro": "M305",
      "bloco": "M",
      "nivel": 4,
      "nome": "Conta da Parte B do e-Lalur",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA_B",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "VL_CTA",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M310": {
      "registro": "M310",
      "bloco": "M",
      "nivel": 4,
      "nome": "Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lalur",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M312": {
      "registro": "M312",
      "bloco": "M",
      "nivel": 5,
      "nome": "Números dos Lançamentos Relacionados à Conta Contábil",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "NUM_LCTO",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M315": {
      "registro": "M315",
      "bloco": "M",
      "nivel": 4,
      "nome": "Identificação de Processos Judiciais e Administrativos referente à Adição",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 3,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_PROC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NUM_PROC",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M350": {
      "registro": "M350",
      "bloco": "M",
      "nivel": 3,
      "nome": "Demonstração da Base de Cálculo da CSLL",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 7,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "TIPO_LANCAMENTO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "IND_RELACAO",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "VALOR",
          "tipo": "",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "HIST_LAN_LAL",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "M355": {
      "registro": "M355",
      "bloco": "M",
      "nivel": 4,
      "nome": "Conta da Parte B do e-Lacs",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA_B",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "VL_CTA",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M360": {
      "registro": "M360",
      "bloco": "M",
      "nivel": 4,
      "nome": "Contas Contábeis Relacionadas ao Lançamento da Parte A do e-Lacs",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M362": {
      "registro": "M362",
      "bloco": "M",
      "nivel": 5,
      "nome": "Números dos Lançamentos Relacionados à Conta Contábil",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "NUM_LCTO",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M365": {
      "registro": "M365",
      "bloco": "M",
      "nivel": 4,
      "nome": "Identificação de Processos Judiciais e Administrativos referente à Exclusão",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 3,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_PROC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NUM_PROC",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M410": {
      "registro": "M410",
      "bloco": "M",
      "nivel": 3,
      "nome": "Lançamentos na Conta da Parte B do e-Lalur e do e-Lacs Sem Reflexo na Parte A",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA_B",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 3,
          "nome": "COD_TRIBUTO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "VAL_LAN_LALB_PB",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M415": {
      "registro": "M415",
      "bloco": "M",
      "nivel": 4,
      "nome": "Identificação de Processos Judiciais e Administrativos Referentes ao Lançamento",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 3,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_PROC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NUM_PROC",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "M500": {
      "registro": "M500",
      "bloco": "M",
      "nivel": 3,
      "nome": "Controle de Saldos das Contas da Parte B do e-Lalur e do e-Lacs",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 11,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA_B",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_TRIBUTO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "SD_INI_LAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "CAMPO_5",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 6,
          "nome": "CAMPO_6",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 7,
          "nome": "CAMPO_7",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 8,
          "nome": "CAMPO_8",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 9,
          "nome": "CAMPO_9",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 10,
          "nome": "CAMPO_10",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 11,
          "nome": "CAMPO_11",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "M510": {
      "registro": "M510",
      "bloco": "M",
      "nivel": 3,
      "nome": "Controle de Saldos das Contas Padrão da Parte B do e-Lalur e do e-Lacs",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 12,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_PB_RFB",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO_PB_RFB",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "COD_TRIBUTO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "SD_INI_LAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "CAMPO_6",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 7,
          "nome": "CAMPO_7",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 8,
          "nome": "CAMPO_8",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 9,
          "nome": "CAMPO_9",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 10,
          "nome": "CAMPO_10",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 11,
          "nome": "CAMPO_11",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 12,
          "nome": "CAMPO_12",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "M990": {
      "registro": "M990",
      "bloco": "M",
      "nivel": 1,
      "nome": "Encerramento do Bloco M N",
      "obrig_entrada": "N",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "N001": {
      "registro": "N001",
      "bloco": "N",
      "nivel": 1,
      "nome": "Abertura do bloco",
      "obrig_entrada": "N",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "N030": {
      "registro": "N030",
      "bloco": "N",
      "nivel": 2,
      "nome": "Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Tributadas pelo Lucro Real",
      "obrig_entrada": "F",
      "ocorrencia": "[0;13]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "N500": {
      "registro": "N500",
      "bloco": "N",
      "nivel": 3,
      "nome": "Base de Cálculo do IRPJ Sobre o Lucro Real Após as Compensações de Prejuízos",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "N600": {
      "registro": "N600",
      "bloco": "N",
      "nivel": 3,
      "nome": "Demonstração do Lucro da Exploração",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "N605": {
      "registro": "N605",
      "bloco": "N",
      "nivel": 3,
      "nome": "Contas Contábeis Utilizadas na Apuração do Lucro da Exploração",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 5,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_VALOR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "N610": {
      "registro": "N610",
      "bloco": "N",
      "nivel": 3,
      "nome": "Cálculo da Isenção e Redução do Imposto Sobre o Lucro Real",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "N615": {
      "registro": "N615",
      "bloco": "N",
      "nivel": 3,
      "nome": "Informações da Base de Cálculo de Incentivos Fiscais",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 7,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "BASE_CALC",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "PER_INCEN_FINOR",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 4,
          "nome": "VL_LIQ_INCEN_",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 5,
          "nome": "PER_INCEN_",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 6,
          "nome": "VL_LIQ_INCEN_",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 7,
          "nome": "VL_TOTAL",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "N620": {
      "registro": "N620",
      "bloco": "N",
      "nivel": 3,
      "nome": "Apuração do IRPJ Mensal por Estimativa",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "N630": {
      "registro": "N630",
      "bloco": "N",
      "nivel": 3,
      "nome": "Apuração do IRPJ Com Base no Lucro Real",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "N650": {
      "registro": "N650",
      "bloco": "N",
      "nivel": 3,
      "nome": "Base de Cálculo da CSLL Após as Compensações da Base de Cálculo Negativa",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "",
          "obrigatorio": "Não"
        }
      ]
    },
    "N660": {
      "registro": "N660",
      "bloco": "N",
      "nivel": 3,
      "nome": "Apuração da CSLL Mensal por Estimativa",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "",
          "obrigatorio": "Não"
        }
      ]
    },
    "N670": {
      "registro": "N670",
      "bloco": "N",
      "nivel": 3,
      "nome": "Apuração da CSLL Com Base no Lucro Real",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "",
          "obrigatorio": "Não"
        }
      ]
    },
    "N990": {
      "registro": "N990",
      "bloco": "N",
      "nivel": 1,
      "nome": "Encerramento do Bloco",
      "obrig_entrada": "N",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "P001": {
      "registro": "P001",
      "bloco": "P",
      "nivel": 1,
      "nome": "Abertura do Bloco P – Lucro Presumido F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "P030": {
      "registro": "P030",
      "bloco": "P",
      "nivel": 2,
      "nome": "IRPJ e da CSLL das Empresas Tributadas pelo Lucro",
      "obrig_entrada": "F",
      "ocorrencia": "[0;4]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "P100": {
      "registro": "P100",
      "bloco": "P",
      "nivel": 3,
      "nome": "Balanço Patrimonial",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 12,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "TIPO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NIVEL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "COD_CTA_SUP",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VAL_CTA_REF_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "IND_VAL_CTA_REF_INI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "VAL_CTA_REF_DEB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "VAL_CTA_REF_CRED",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 12,
          "nome": "VAL_CTA_REF_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "P130": {
      "registro": "P130",
      "bloco": "P",
      "nivel": 3,
      "nome": "Demonstração das Receitas Incentivadas do Lucro Presumido",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "P150": {
      "registro": "P150",
      "bloco": "P",
      "nivel": 3,
      "nome": "Demonstração do Resultado",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 8,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "TIPO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NIVEL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "COD_CTA_SUP",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VALOR",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "P200": {
      "registro": "P200",
      "bloco": "P",
      "nivel": 3,
      "nome": "Apuração da Base de Cálculo do Lucro Presumido F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "P230": {
      "registro": "P230",
      "bloco": "P",
      "nivel": 3,
      "nome": "Cálculo da Isenção e Redução do Lucro Presumido",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "P300": {
      "registro": "P300",
      "bloco": "P",
      "nivel": 3,
      "nome": "Cálculo do IRPJ com Base no Lucro Presumido F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "P400": {
      "registro": "P400",
      "bloco": "P",
      "nivel": 3,
      "nome": "Apuração da Base de Cálculo da CSLL com Base no Lucro Presumido",
      "obrig_entrada": "F",
      "ocorrencia": "[1;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "P500": {
      "registro": "P500",
      "bloco": "P",
      "nivel": 3,
      "nome": "Cálculo da CSLL com Base no Lucro Líquido F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "P990": {
      "registro": "P990",
      "bloco": "P",
      "nivel": 1,
      "nome": "Encerramento do Bloco P F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Q001": {
      "registro": "Q001",
      "bloco": "Q",
      "nivel": 1,
      "nome": "Abertura do Bloco Q – Livro Caixa F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Q100": {
      "registro": "Q100",
      "bloco": "Q",
      "nivel": 2,
      "nome": "Demonstrativo do Livro Caixa",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 7,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DATA",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NUM_DOC",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "HIST",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "VL_ENTRADA",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "VL_SAIDA",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "SLD_FIN",
          "tipo": "",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Q990": {
      "registro": "Q990",
      "bloco": "Q",
      "nivel": 1,
      "nome": "Encerramento do Bloco Q F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "S001": {
      "registro": "S001",
      "bloco": "S",
      "nivel": 1,
      "nome": "Abertura do Bloco S -TEF/SAF F",
      "obrig_entrada": "F",
      "ocorrencia": "[1:1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "S030": {
      "registro": "S030",
      "bloco": "S",
      "nivel": 2,
      "nome": "IRPJ e da CSLL das Empresas Tributadas pelo",
      "obrig_entrada": "F",
      "ocorrencia": "[0:12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "S100": {
      "registro": "S100",
      "bloco": "S",
      "nivel": 3,
      "nome": "Balanço Patrimonial das entidades TEF/SAF.",
      "obrig_entrada": "F",
      "ocorrencia": "[0:12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 12,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "TIPO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NIVEL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "COD_CTA_SUP",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VAL_CTA_REF_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "IND_VAL_CTA_REF_INI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "VAL_CTA_REF_DEB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "VAL_CTA_REF_CRED",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 12,
          "nome": "VAL_CTA_REF_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "S150": {
      "registro": "S150",
      "bloco": "S",
      "nivel": 3,
      "nome": "Demonstrativo do Resultado Líquido no Período Fiscal",
      "obrig_entrada": "F",
      "ocorrencia": "[0:12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 8,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "TIPO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NIVEL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "COD_CTA_SUP",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VALOR",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "S200": {
      "registro": "S200",
      "bloco": "S",
      "nivel": 3,
      "nome": "Apuração dos Tributos a Pagar Incidentes em TEF/SAF",
      "obrig_entrada": "F",
      "ocorrencia": "[0:12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "S300": {
      "registro": "S300",
      "bloco": "S",
      "nivel": 3,
      "nome": "Cálculo do IRPJ",
      "obrig_entrada": "F",
      "ocorrencia": "[0:12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "S500": {
      "registro": "S500",
      "bloco": "S",
      "nivel": 3,
      "nome": "Cálculo da CSLL",
      "obrig_entrada": "F",
      "ocorrencia": "[0:12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "S700": {
      "registro": "S700",
      "bloco": "S",
      "nivel": 3,
      "nome": "Cálculo dos Demais Tributos",
      "obrig_entrada": "F",
      "ocorrencia": "[0:12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "S990": {
      "registro": "S990",
      "bloco": "S",
      "nivel": 1,
      "nome": "Encerramento do Bloco S",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "CAMPO_1",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 2,
          "nome": "CAMPO_2",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "T001": {
      "registro": "T001",
      "bloco": "T",
      "nivel": 1,
      "nome": "Abertura do Bloco T – Lucro Arbitrado F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "T030": {
      "registro": "T030",
      "bloco": "T",
      "nivel": 2,
      "nome": "IRPJ e CSLL das Empresas Tributadas pelo Lucro",
      "obrig_entrada": "F",
      "ocorrencia": "[0;4]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "T120": {
      "registro": "T120",
      "bloco": "T",
      "nivel": 3,
      "nome": "Apuração da Base de Cálculo do IRPJ com Base no Lucro Arbitrado",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "T150": {
      "registro": "T150",
      "bloco": "T",
      "nivel": 3,
      "nome": "Cálculo do IRPJ com Base no Lucro Arbitrado",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "T170": {
      "registro": "T170",
      "bloco": "T",
      "nivel": 3,
      "nome": "Apuração da Base de Cálculo da CSLL com Base no Lucro Arbitrado",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "T181": {
      "registro": "T181",
      "bloco": "T",
      "nivel": 3,
      "nome": "Cálculo da CSLL com Base no Lucro Arbitrado",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "T990": {
      "registro": "T990",
      "bloco": "T",
      "nivel": 1,
      "nome": "Encerramento do Bloco T F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "U001": {
      "registro": "U001",
      "bloco": "U",
      "nivel": 1,
      "nome": "Abertura do Bloco U – Imunes e Isentas F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "U030": {
      "registro": "U030",
      "bloco": "U",
      "nivel": 2,
      "nome": "Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;4]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PER_APUR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "U100": {
      "registro": "U100",
      "bloco": "U",
      "nivel": 3,
      "nome": "Balanço Patrimonial",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 12,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "TIPO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NIVEL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "COD_CTA_SUP",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VAL_CTA_REF_INI",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "IND_VAL_CTA_REF_INI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "VAL_CTA_REF_DEB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "VAL_CTA_REF_CRED",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 12,
          "nome": "VAL_CTA_REF_FIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "U150": {
      "registro": "U150",
      "bloco": "U",
      "nivel": 3,
      "nome": "Demonstração do Resultado",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 8,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "TIPO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NIVEL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "COD_NAT",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "COD_CTA_SUP",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VALOR",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "U180": {
      "registro": "U180",
      "bloco": "U",
      "nivel": 3,
      "nome": "Cálculo do IRPJ das Empresas Imunes ou Isentas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "U182": {
      "registro": "U182",
      "bloco": "U",
      "nivel": 3,
      "nome": "Cálculo da CSLL das Empresas Imunes ou Isentas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "U990": {
      "registro": "U990",
      "bloco": "U",
      "nivel": 1,
      "nome": "Encerramento do Bloco U F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "V001": {
      "registro": "V001",
      "bloco": "V",
      "nivel": 1,
      "nome": "Abertura do Bloco V – DEREX F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "V010": {
      "registro": "V010",
      "bloco": "V",
      "nivel": 2,
      "nome": "DEREX – Instituição",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "NOME_INSTITUICAO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "PAIS",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "TIP_MOEDA",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "V020": {
      "registro": "V020",
      "bloco": "V",
      "nivel": 3,
      "nome": "DEREX - Responsável pela Movimentação",
      "obrig_entrada": "F",
      "ocorrencia": "[1;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 6,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "NOME",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "ENDERECO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "TIPO_DO_C",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "IDENT_CONTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "V030": {
      "registro": "V030",
      "bloco": "V",
      "nivel": 3,
      "nome": "DEREX - Período – Mês",
      "obrig_entrada": "F",
      "ocorrencia": "[1;12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "MES",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "V100": {
      "registro": "V100",
      "bloco": "V",
      "nivel": 4,
      "nome": "Demonstrativo dos Recursos em Moeda Estrangeira Decorrentes do Recebimento de Exportações",
      "obrig_entrada": "F",
      "ocorrencia": "[1;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": ""
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": ""
        }
      ]
    },
    "V990": {
      "registro": "V990",
      "bloco": "V",
      "nivel": 1,
      "nome": "Encerramento do Bloco V",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN_M",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "W001": {
      "registro": "W001",
      "bloco": "W",
      "nivel": 1,
      "nome": "Abertura do Bloco W - Declaração País-a-País F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "W100": {
      "registro": "W100",
      "bloco": "W",
      "nivel": 2,
      "nome": "Informações sobre o Grupo Multinacional e a Entidade Declarante – Declaração País-a-País",
      "obrig_entrada": "F",
      "ocorrencia": "[0;1]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 15,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "NOME_MULTINACIONAL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "IND_CONTROLADORA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "NOME_CONTROLADORA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "JURISDICAO_CONTROLADORA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "TIN_CONTROLADORA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "IND_ENTREGA",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "IND_MODALIDADE",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "NOME_SUBSTITUTA",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 10,
          "nome": "JURISDICAO_SUBSTITUTA",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 11,
          "nome": "TIN_SUBSTITUTA",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 12,
          "nome": "DT_INI",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 13,
          "nome": "DT_FIN",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 14,
          "nome": "TIP_MOEDA",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 15,
          "nome": "IND_IDIOMA",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "W200": {
      "registro": "W200",
      "bloco": "W",
      "nivel": 3,
      "nome": "Declaração País a País",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 21,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "JURISDICAO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "VL_REC_NAO_REL_EST",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VL_REC_NAO_REL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "VL_REC_REL_EST",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "VL_REC_REL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "VL_REC_TOTAL_EST",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VL_REC_TOTAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "VL_LUC_PREJ_ANTES_IR_EST",
          "tipo": "",
          "obrigatorio": "Não"
        },
        {
          "seq": 10,
          "nome": "VL_LUC_PREJ_ANTES_IR",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "VL_IR_PAGO_EST",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 12,
          "nome": "VL_IR_PAGO",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 13,
          "nome": "VL_IR_DEVIDO_EST",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 14,
          "nome": "VL_IR_DEVIDO",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 15,
          "nome": "VL_CAP_SOC_EST",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 16,
          "nome": "VL_CAP_SOC",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 17,
          "nome": "VL_LUC_ACUM_EST",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 18,
          "nome": "VL_LUC_ACUM",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 19,
          "nome": "VL_ATIV_TANG_EST",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 20,
          "nome": "VL_ATIV_TANG",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 21,
          "nome": "NUM_EMP",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "W250": {
      "registro": "W250",
      "bloco": "W",
      "nivel": 4,
      "nome": "Declaração País a País - Entidades Integrantes",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 9,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "JUR_DIFERENTE",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 3,
          "nome": "NOME",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "TIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "JURISDICAO_TIN",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "NI",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "JURISDICAO_NI",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "TIPO_NI",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 9,
          "nome": "TIP_END",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "W300": {
      "registro": "W300",
      "bloco": "W",
      "nivel": 2,
      "nome": "Observações Adicionais",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 12,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "JURISDICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 3,
          "nome": "IND_REC_NAO_REL",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "IND_REC_REL",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "IND_REC_TOTAL",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "IND_LUC_PREJ_ANTES_IR",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "IND_IR_PAGO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "IND_IR_DEVIDO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 9,
          "nome": "IND_CAP_SOC",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 10,
          "nome": "IND_LUC_ACUM",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 11,
          "nome": "IND_ATIV_TANG",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 12,
          "nome": "IND_NUM_EMP",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "W990": {
      "registro": "W990",
      "bloco": "W",
      "nivel": 1,
      "nome": "Encerramento do Bloco W F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X001": {
      "registro": "X001",
      "bloco": "X",
      "nivel": 1,
      "nome": "Abertura do Bloco X – Informações Econômicas F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X280": {
      "registro": "X280",
      "bloco": "X",
      "nivel": 2,
      "nome": "Atividades Incentivadas - PJ em Geral",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 11,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_ATIV",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "IND_CONCEDENTE",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_PROJ",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "ATO_CONC",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VIG_INI",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "VIG_FIM",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "CNPJ_INCENTIVO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "NCM_INCENTIVO",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 10,
          "nome": "REC_LIQ_INCENTIVO",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "VL_INCENTIVO",
          "tipo": "N",
          "obrigatorio": "Não"
        }
      ]
    },
    "X292": {
      "registro": "X292",
      "bloco": "X",
      "nivel": 2,
      "nome": "Operações com o Exterior – Pessoa Não Vinculada/Não Interposta/País sem Tributação Favorecida",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X340": {
      "registro": "X340",
      "bloco": "X",
      "nivel": 2,
      "nome": "Identificação da Participação no Exterior",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 10,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "RAZ_SOCIAL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NIF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_CONTROLE",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "PAIS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "IND_ISEN_PETR",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "IND_CONSOL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "MOT_NAO_CONSOL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 9,
          "nome": "CNPJ",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 10,
          "nome": "TIP_MOEDA",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X350": {
      "registro": "X350",
      "bloco": "X",
      "nivel": 3,
      "nome": "Participações no Exterior – Resultado do Período de Apuração",
      "obrig_entrada": "N",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 14,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "REC_LIQ",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "CUSTOS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "LUC_BRUTO",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "REC_AUFERIDAS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "REC_OUTRAS_OPER",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "DESP_BRASIL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "DESP_OPER",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "LUC_OPER",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "REC_PARTIC",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "REC_OUTRAS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 12,
          "nome": "DESP_OUTRAS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 13,
          "nome": "LUC_LIQ_ANT_IR",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 14,
          "nome": "LUC_ARB_ANT_IR",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "X351": {
      "registro": "X351",
      "bloco": "X",
      "nivel": 3,
      "nome": "Demonstrativo de Resultados e de Imposto Pago no Exterior",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 16,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "RES_INV_PER",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "RES_INV_PER_REAL",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "RES_ISEN_PETR_PER",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "RES_ISEN_PETR_PER_REAL",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "RES_NEG_ACUM",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "RES_NEG_ACUM_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "RES_POS_TRIB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "RES_POS_TRIB_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "IMP_LUCR",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "IMP_LUCR_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 12,
          "nome": "IMP_PAG_REND",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 13,
          "nome": "IMP_PAG_REND_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 14,
          "nome": "IMP_RET_EXT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 15,
          "nome": "IMP_RET_EXT_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 16,
          "nome": "IMP_RET_BR",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X352": {
      "registro": "X352",
      "bloco": "X",
      "nivel": 3,
      "nome": "Demonstrativo de Resultados no Exterior Auferidos por Intermédio de Coligadas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 5,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "RES_PER",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "RES_PER_REAL",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "LUC_DISP",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "LUC_DISP_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X353": {
      "registro": "X353",
      "bloco": "X",
      "nivel": 3,
      "nome": "Demonstrativo de Consolidação",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 7,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "RES_NEG_UTIL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "RES_NEG_UTIL_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "SALDO_RES_NEG_NAO_UTIL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "SALDO_RES_NEG_NAO_UTIL_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "RES_PROP",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "RES_PROP_REAL",
          "tipo": "",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X354": {
      "registro": "X354",
      "bloco": "X",
      "nivel": 3,
      "nome": "Demonstrativo de Prejuízos Acumulados",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "RES_NEG_ANT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "RES_NEG_ANT_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "SALDO_NEG_ACUM",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X355": {
      "registro": "X355",
      "bloco": "X",
      "nivel": 3,
      "nome": "Demonstrativo de Rendas Ativas e Passivas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 8,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "REND_PASS_PROP",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "REND_PASS_PROP_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "REND_TOTAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "REND_TOTAL_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "REND_ATIV_PROP",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "REND_ATIV_PROP_REAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "PERCENTUAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X356": {
      "registro": "X356",
      "bloco": "X",
      "nivel": 3,
      "nome": "Demonstrativo de Estrutura Societária",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "PERC_PART",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "ATIVO_TOTAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PAT_LIQUIDO",
          "tipo": "",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X357": {
      "registro": "X357",
      "bloco": "X",
      "nivel": 3,
      "nome": "Investidoras Diretas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 5,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "PAIS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NIF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "RAZAO_SOCIAL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "PERCENTUAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X360": {
      "registro": "X360",
      "bloco": "X",
      "nivel": 2,
      "nome": "Informações Gerais sobre Preços de Transferência",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X365": {
      "registro": "X365",
      "bloco": "X",
      "nivel": 2,
      "nome": "Informações Sobre as Contrapartes nas Transações Controladas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 3,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IDENTIFICADOR",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NOME_ENT",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X366": {
      "registro": "X366",
      "bloco": "X",
      "nivel": 3,
      "nome": "Entidades Com as Quais Realiza Transações Controladas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X370": {
      "registro": "X370",
      "bloco": "X",
      "nivel": 2,
      "nome": "Informações Sobre as Transações Controladas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 20,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IDENTIFICADOR",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "TIPO_TRANSACAO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "NOME_ENT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "PAIS",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "COD_NCM",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "TIPO_DEMAIS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "DESCR_BSDI",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "VL_TRANSACAO",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "IND_AJUSTES",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "VL_ESPONTANEO",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 12,
          "nome": "VL_COMPENSATORIO",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 13,
          "nome": "TIP_AJ_COMPENSATORIO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 14,
          "nome": "METODO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 15,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 16,
          "nome": "COMP_INTENCIONAL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 17,
          "nome": "SINERGIA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 18,
          "nome": "IND_TRANS_COMBINADAS",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 19,
          "nome": "IND_DADOS_MULTIP",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 20,
          "nome": "IND_SIMPLIFIC",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X371": {
      "registro": "X371",
      "bloco": "X",
      "nivel": 3,
      "nome": "Informações Sobre Ajustes Compensatórios",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 5,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "COD_CTA",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COD_CCUS",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_VALOR",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X375": {
      "registro": "X375",
      "bloco": "X",
      "nivel": 3,
      "nome": "Informações Relacionadas aos Métodos",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X390": {
      "registro": "X390",
      "bloco": "X",
      "nivel": 2,
      "nome": "Origem e Aplicação de Recursos - Imunes ou Isentas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X400": {
      "registro": "X400",
      "bloco": "X",
      "nivel": 2,
      "nome": "Comércio Eletrônico e Tecnologia da Informação – Informações das Vendas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X410": {
      "registro": "X410",
      "bloco": "X",
      "nivel": 2,
      "nome": "Comércio Eletrônico.",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "PAIS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "IND_HOME_DISP",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_SERV_DISP",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X420": {
      "registro": "X420",
      "bloco": "X",
      "nivel": 2,
      "nome": "Royalties Recebidos ou Pagos a Beneficiários do Brasil e do Exterior",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 10,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "TIP_ROY",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "PAIS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "VL_EXPL_DIR_SW",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "VL_EXPL_DIR_AUT",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "VL_EXPL_MARCA",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "VL_EXPL_PAT",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VL_EXPL_KNOW",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 9,
          "nome": "VL_EXPL_FRANQ",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 10,
          "nome": "VL_EXPL_INT",
          "tipo": "N",
          "obrigatorio": "Não"
        }
      ]
    },
    "X430": {
      "registro": "X430",
      "bloco": "X",
      "nivel": 2,
      "nome": "“Rendimentos Relativos a Serviços, Juros e Dividendos",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 8,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "PAIS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "VL_SERV_ASSIST",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VL_SERV_SEM_ASSIST",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "VL_SERV_SEM_ASSIST_EXT",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "VL_JURO",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "VL_DEMAIS_JUROS",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VL_DIVID",
          "tipo": "N",
          "obrigatorio": "Não"
        }
      ]
    },
    "X450": {
      "registro": "X450",
      "bloco": "X",
      "nivel": 2,
      "nome": "Pagamentos ou Remessas a Título de Serviços, Juros e Dividendos a Beneficiários do Brasil e do Exterior",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "PAIS",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "X451": {
      "registro": "X451",
      "bloco": "X",
      "nivel": 2,
      "nome": "e Dividendos a Beneficiários do Brasil e do Exterior –",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X460": {
      "registro": "X460",
      "bloco": "X",
      "nivel": 2,
      "nome": "Inovação Tecnológica e Desenvolvimento Tecnológico",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X470": {
      "registro": "X470",
      "bloco": "X",
      "nivel": 2,
      "nome": "Capacitação de Informática e Inclusão Digital",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X480": {
      "registro": "X480",
      "bloco": "X",
      "nivel": 2,
      "nome": "Benefícios Fiscais – Parte I",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "",
          "obrigatorio": "Não"
        }
      ]
    },
    "X485": {
      "registro": "X485",
      "bloco": "X",
      "nivel": 2,
      "nome": "Benefícios Fiscais – Parte II",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 11,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "TIPO_BENEF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "ATO_DECL",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "CNPJ_INCORP",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "ID_OBRA_2018",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "ID_OBRA_2020",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "ID_OBRA_EEI",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "PORT_CEBAS",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 9,
          "nome": "DT_DOU_PORT_CEBAS",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 10,
          "nome": "DT_INI_PORT_CEBAS",
          "tipo": "",
          "obrigatorio": ""
        },
        {
          "seq": 11,
          "nome": "DT_FIN_PORT_CEBAS",
          "tipo": "",
          "obrigatorio": ""
        }
      ]
    },
    "X490": {
      "registro": "X490",
      "bloco": "X",
      "nivel": 2,
      "nome": "Polo Industrial de Manaus e Amazônia Ocidental",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X500": {
      "registro": "X500",
      "bloco": "X",
      "nivel": 2,
      "nome": "Zonas de Processamento de Exportação (ZPE)",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X510": {
      "registro": "X510",
      "bloco": "X",
      "nivel": 2,
      "nome": "Áreas de Livre Comércio (ALC)",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "X990": {
      "registro": "X990",
      "bloco": "X",
      "nivel": 1,
      "nome": "Encerramento do Bloco X F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Y001": {
      "registro": "Y001",
      "bloco": "Y",
      "nivel": 1,
      "nome": "Abertura do Bloco Y – Informações Gerais F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": true,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "IND_DAD",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Y520": {
      "registro": "Y520",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Pagamentos/Recebimentos do Exterior ou de Não Residentes",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 6,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "TIP_EXT",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "PAIS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "FORMA",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "NAT_OPER",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_PERIODO",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Y570": {
      "registro": "Y570",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Demonstrativo do Imposto de Renda e CSLL Retidos na Fonte",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 8,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CNPJ_FON",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NOM_EMP",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "IND_ORG_PUB",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "COD_REC",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_REND",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "IR_RET",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "CSLL_RET",
          "tipo": "N",
          "obrigatorio": "Não"
        }
      ]
    },
    "Y590": {
      "registro": "Y590",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Ativos no Exterior",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 6,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "TIP_ATIVO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "PAIS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "DISCRIMINACAO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "VL_ANT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_ATUAL",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Y600": {
      "registro": "Y600",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Identificação e Remuneração de Sócios, Titulares, Dirigentes e Conselheiros",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 17,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_ALT_SOC",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_FIM_SOC",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "PAIS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "IND_QUALIF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "CPF_CNPJ",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "NOM_EMP",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "QUALIF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "PERC_CAP_TOT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "PERC_CAP_VOT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "CPF_REP_LEG",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 12,
          "nome": "QUALIF_REP_LEG",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 13,
          "nome": "VL_REM_TRAB",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 14,
          "nome": "VL_LUC_DIV",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 15,
          "nome": "VL_JUR_CAP",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 16,
          "nome": "VL_DEM_REND",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 17,
          "nome": "VL_IR_RET",
          "tipo": "N",
          "obrigatorio": "Não"
        }
      ]
    },
    "Y612": {
      "registro": "Y612",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Identificação e Rendimentos de Dirigentes e Conselheiros – Imunes ou Isentas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 7,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CPF",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NOME",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "QUALIF",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "VL_REM_TRAB",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_DEM_REND",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "VL_IR_RET",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Y620": {
      "registro": "Y620",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Participações Avaliadas Pelo Método de Equivalência Patrimonial",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 17,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DT_EVENTO",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "IND_RELAC",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PAIS",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "CNPJ",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "NOM_EMP",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "VALOR_REAIS",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "VALOR_ESTR",
          "tipo": "",
          "obrigatorio": "Sim"
        },
        {
          "seq": 9,
          "nome": "PERC_CAP_TOT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 10,
          "nome": "PERC_CAP_VOT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 11,
          "nome": "RES_EQ_PAT",
          "tipo": "",
          "obrigatorio": "Não"
        },
        {
          "seq": 12,
          "nome": "DATA_AQUIS",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 13,
          "nome": "IND_PROC_CART",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 14,
          "nome": "NUM_PROC_CART",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 15,
          "nome": "NOME_CART",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 16,
          "nome": "IND_PROC_RFB",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 17,
          "nome": "NUM_PROC_RFB",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "Y630": {
      "registro": "Y630",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Fundos/Clubes de Investimento",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 7,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CNPJ",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "QTE_QUOT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "QTE_QUOTA",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "PATR_FIN_PER",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "DAT_ABERT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "DAT_ENCER",
          "tipo": "N",
          "obrigatorio": "Não"
        }
      ]
    },
    "Y640": {
      "registro": "Y640",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Participações em Consórcios de Empresas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 6,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CNPJ",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "COND_DECL",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "VL_CONS",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "CNPJ_LID",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "VL_DECL",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Y650": {
      "registro": "Y650",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Participantes do Consórcio",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 3,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CNPJ",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "VL_PART",
          "tipo": "N",
          "obrigatorio": "Não"
        }
      ]
    },
    "Y660": {
      "registro": "Y660",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Dados de Sucessoras",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CNPJ",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "NOM_EMP",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "PERC_PAT_LIQ",
          "tipo": "N",
          "obrigatorio": "Não"
        }
      ]
    },
    "Y672": {
      "registro": "Y672",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Outras Informações (Lucro Presumido ou Lucro Arbitrado)",
      "obrig_entrada": "F",
      "ocorrencia": "[0;1]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 18,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "VL_CAPITAL_ANT",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 3,
          "nome": "VL_CAPITAL",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VL_ESTOQUE_ANT",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 5,
          "nome": "VL_ESTOQUES",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 6,
          "nome": "VL_CAIXA_ANT",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 7,
          "nome": "VL_CAIXA",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 8,
          "nome": "VL_APLIC_FIN_ANT",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 9,
          "nome": "VL_APLIC_FIN",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 10,
          "nome": "VL_CTA_REC_ANT",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 11,
          "nome": "VL_CTA_REC",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 12,
          "nome": "VL_CTA_PAG_ANT",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 13,
          "nome": "VL_CTA_PAG",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 14,
          "nome": "VL_COMPRA_MERC",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 15,
          "nome": "VL_COMPRA_ATIVO",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 16,
          "nome": "VL_RECEITAS",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 17,
          "nome": "TOT_ATIVO",
          "tipo": "N",
          "obrigatorio": "Não"
        },
        {
          "seq": 18,
          "nome": "IND_AVAL_ESTOQ",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "Y680": {
      "registro": "Y680",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Mês das Informações de Optantes pelo Refis (Lucro Real, Presumido e Arbitrado)",
      "obrig_entrada": "F",
      "ocorrencia": "[0;12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "MES",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Y681": {
      "registro": "Y681",
      "bloco": "Y",
      "nivel": 3,
      "nome": "Informações de Optantes pelo Refis (Lucros Real, Presumido e Arbitrado)",
      "obrig_entrada": "F",
      "ocorrencia": "[0;12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "Y682": {
      "registro": "Y682",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Informações de Optantes pelo Refis – Imunes ou Isentas",
      "obrig_entrada": "F",
      "ocorrencia": "[0;12]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 3,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "MES",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "ACRES_PATR",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Y720": {
      "registro": "Y720",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Informações de Períodos Anteriores",
      "obrig_entrada": "F",
      "ocorrencia": "[0;1]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 6,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "LUC_LIQ",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DT_LUC_LIQ",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "REC_BRUT_ANT",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "INTIMACAO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "INT_ATRASO",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Y730": {
      "registro": "Y730",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Identificação de donatários/destinatários de deduções do IRPJ/CSLL",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 8,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "DEDUCAO",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "TIPO",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "DATA",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "TIPO_DESTINATARIO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "DESTINATARIO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 7,
          "nome": "VALOR",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 8,
          "nome": "OBSERVACAO",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "Y750": {
      "registro": "Y750",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Informações da ECF Calculadas pelo PGE F",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 4,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "CODIGO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Não"
        },
        {
          "seq": 4,
          "nome": "VALOR",
          "tipo": "C",
          "obrigatorio": "Não"
        }
      ]
    },
    "Y800": {
      "registro": "Y800",
      "bloco": "Y",
      "nivel": 2,
      "nome": "Outras Informações",
      "obrig_entrada": "F",
      "ocorrencia": "[0;N]",
      "abertura": false,
      "encerramento": false,
      "num_campos": 6,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "TIPO_DOC",
          "tipo": "N",
          "obrigatorio": "Sim"
        },
        {
          "seq": 3,
          "nome": "DESCRICAO",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 4,
          "nome": "HASH",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 5,
          "nome": "ARQ_RTF",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 6,
          "nome": "IND_FIM_RTF",
          "tipo": "C",
          "obrigatorio": "Sim"
        }
      ]
    },
    "Y990": {
      "registro": "Y990",
      "bloco": "Y",
      "nivel": 1,
      "nome": "Encerramento do Bloco Y F",
      "obrig_entrada": "F",
      "ocorrencia": "[1;1]",
      "abertura": false,
      "encerramento": true,
      "num_campos": 2,
      "campos": [
        {
          "seq": 1,
          "nome": "REG",
          "tipo": "C",
          "obrigatorio": "Sim"
        },
        {
          "seq": 2,
          "nome": "QTD_LIN",
          "tipo": "N",
          "obrigatorio": "Sim"
        }
      ]
    }
  }
}