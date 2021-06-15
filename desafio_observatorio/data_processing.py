""" Módulo de processamento de dados """
import os
import requests

import pandas as pd

from helpers import STATES, INDICATOR_OPTIONS, API_URL, OPERATION_OPTIONS_REVERSER


def hit_api(endpoint: str) -> dict:
    """ Wrapper de uma requisição para pedir dados a API """
    headers = {
        "accept": "application/json",
    }

    response = requests.get(API_URL + endpoint, headers=headers)

    return response.json()


def api_get_ncm_code_listing() -> list:
    """Requisita da API a listagem de códigos NCM"""

    return hit_api("cod_ncm_listing/")


def api_get_years_listing() -> list:
    """Requisita da API a listagem de anos com dados disponíveis """

    return hit_api("year_listing/")


def api_get_state_contribution() -> dict:
    """Requisita da API dados sobre a contribuição percentual por estado"""

    response = hit_api("states_contribution/")
    return pd.DataFrame.from_dict(response)


def api_get_operation_statistics(year: int, operation: str, cod_ncm: int) -> dict:
    """Obtém estatísticas sobre operações financeiras"""

    return hit_api(f"operation_statistics/{year}/{operation}/{cod_ncm}")


def api_get_via_statistics_statistics(year: int, operation: str, cod_ncm: int) -> dict:
    """Obtém dados sobre uso da via"""

    return hit_api(f"via_statistics/{year}/{operation}/{cod_ncm}")
