""" Módulo de processamento de dados """
import pandas as pd

from helpers import STATES, INDICATOR_OPTIONS,IMPORT_DATA_COLUMNS, EXPORT_DATA_COLUMNS


# todo: quando importar os dados dos três anos, refatorar isso em constantes, se necessário
import_2020_file_path = "data/IMP_2020_V2.csv"
export_2020_file_path = "data/EXP_2020.csv"
DELIMITER = ";"

def process_dataset() -> pd.DataFrame:
    """ Processamento inicial do conjunto de dados 
    
    Retorna:
        pd.DataFrame: Tabela com os dados de importação e exportação dos últimos 3 anos
    """
    # dados de importação
    import_data = pd.read_csv(import_2020_file_path, delimiter=DELIMITER)
    import_data.columns = IMPORT_DATA_COLUMNS
    import_data["MOVIMENTACAO"] = "importação"

    # dados de exportação
    export_data = pd.read_csv(export_2020_file_path, delimiter=DELIMITER)
    export_data.columns = EXPORT_DATA_COLUMNS
    export_data["MOVIMENTACAO"] = "exportação"

    # junta os dados em um único dataset
    dataset = pd.concat([export_data, import_data])

    return dataset


def calculate_percentual_contribution(dataset: pd.DataFrame) -> pd.DataFrame:
    """Caclula a contribuição percentual de cada estado
        para cada indicador

    Retorna:
        pd.DataFrame: Tabela com as contribuições percentuais por estado
    """

    # agrupa por estado e soma os totais
    total_by_state = dataset.groupby(["SG_UF"])[INDICATOR_OPTIONS].sum()
    total_by_state.reset_index(level=0, inplace=True)  # remove SG_UF como index externo

    # calcula os percentuais por estado
    for indicator in INDICATOR_OPTIONS:
        # nome da nova coluna com a contribuição percenutal
        new_col_name = f"{indicator}_CONTRIB_%"

        total = total_by_state[indicator].sum()
        total_by_state[new_col_name] = total_by_state[indicator].apply(
            lambda x: round(x / total * 100, 2)
        )

    # Substitui a sigla pelo nome do estado
    total_by_state["SG_UF"] = total_by_state["SG_UF"].apply(
        lambda x: STATES.get(x, "Exportação")
    )

    return total_by_state