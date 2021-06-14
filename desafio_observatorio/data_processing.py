""" Módulo de processamento de dados """
import os

import pandas as pd

from helpers import STATES, INDICATOR_OPTIONS, DATASET_FILNAME, S3_BUCKET_URL, LOCAL_FILES_DIR


def get_dataset_path():
    """ Determina se os dados estão locais ou no s3 bucket """

    where_ = LOCAL_FILES_DIR if os.path.isfile(LOCAL_FILES_DIR+DATASET_FILNAME) else S3_BUCKET_URL
    return where_ + DATASET_FILNAME


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