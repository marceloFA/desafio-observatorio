""" Módulo para dados, constantes e métodos auxiliares """

# onde encontrar os arquivos
API_URL = "https://desafio-observatorio-api-2orasszirq-wm.a.run.app/"

INDICATOR_OPTIONS = [
    "VL_QUANTIDADE",
    "VL_PESO_KG",
    "VL_FOB",
]

OPERATION_OPTIONS = {"importação": "import", "exportação": "export"}
OPERATION_OPTIONS_REVERSER = {"import": "importação", "export":"exportação"}

VIA = {
    0: "VIA NAO DECLARADA",
    1: "MARITIMA",
    2: "FLUVIAL",
    3: "LACUSTRE",
    4: "AEREA",
    5: "POSTAL",
    6: "FERROVIARIA",
    7: "RODOVIARIA",
    8: "CONDUTO/REDE DE TRANSMISSAO",
    9: "MEIOS PROPRIOS",
    10: "ENTRADA/SAIDA FICTA",
    99: "VIA DESCONHECIDA",
    13: "POR REBOQUE",
    11: "COURIER",
    15: "VICINAL FRONTEIRICO",
    14: "DUTOS",
    12: "EM MAOS",
}


MONTHS = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]

STATES = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapá",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará",
    "PB": "Paraíba",
    "PR": "Paraná",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins",
}
