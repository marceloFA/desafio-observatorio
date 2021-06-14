""" Módulo de componentes web dash """
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import pandas as pd

import data_processing
from helpers import VIA, MONTHS, INDICATOR_OPTIONS, COLUMNS_NAMES, DELIMITER

file_path = data_processing.get_dataset_path()
dataset = pd.read_csv(file_path, delimiter=DELIMITER)

# colunas que serão somadas par aobter o acumulado por mês
operation_options = dataset["MOVIMENTACAO"].unique()
# também é usado como lista de opções para o dropdown
product_options = dataset["COD_NCM"].unique()
# Preparando os dados da tabela
total_by_state = data_processing.calculate_percentual_contribution(dataset)

# instanciando um app Dash
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# Algumas configurações do app
app.title = "Dados Comércio Exterior"
pd.options.plotting.backend = "plotly"

app.layout = html.Div(
    [
        # filtros do gráfico principal
        html.Div(
            [
                # Escolha da movimentação
                dcc.Dropdown(
                    id="operation-options-dropdown",
                    options=[{"label": i, "value": i} for i in operation_options],
                    value=operation_options[0],
                ),
                # Escolha da UF
                dcc.Dropdown(
                    id="product-options-dropdown",
                    options=[{"label": i, "value": i} for i in product_options],
                    value=product_options[0],
                ),
                # escolha do indicador
                dcc.Dropdown(
                    id="indicator-options-dropdown",
                    options=[{"label": i, "value": i} for i in INDICATOR_OPTIONS],
                    value=INDICATOR_OPTIONS[0],
                ),
                # Slider de seleção do ano
                dcc.Slider(
                    id="year-slider-input",
                    min=dataset["ANO"].min(),
                    max=dataset["ANO"].max(),
                    value=dataset["ANO"].max(),
                    marks={str(year): str(year) for year in dataset["ANO"].unique()},
                    step=None,
                ),
            ],
            style={"width": "49%"},
        ),
        # Visualização principal
        html.Div(
            [dcc.Graph(id="main-scatter-plot")],
            style={},
        ),
        # Gráfico de pizza com a utilização percentual da via
        html.Div(
            [dcc.Graph(id="via-pie-plot")],
            style={},
        ),
        # Tabela com a contribuição percentual dos estados
        dash_table.DataTable(
            id="percentual-contribution-table",
            columns=[{"name": i, "id": i} for i in total_by_state.columns],
            data=total_by_state.to_dict("records"),
        ),
    ]
)


################################### CALLBACKS ###################################


@app.callback(
    dash.dependencies.Output("main-scatter-plot", "figure"),
    [
        dash.dependencies.Input("operation-options-dropdown", "value"),
        dash.dependencies.Input("indicator-options-dropdown", "value"),
        dash.dependencies.Input("product-options-dropdown", "value"),
        dash.dependencies.Input("year-slider-input", "value"),
    ],
)
def update_main_plot(
    operation: str,
    indicator: str,
    product_value: str,
    year_value: int,
):
    """Atualiza o gráfico principal

    Argumentos:
        operation (str):  [Movimentação selecionada (importação ou exportação)]
        indicator (str):  [Métrica selecionada (valor, valor por peso, etc)]
        product_value (str):   [Categoria de produto selecionado]
        year_value (int): [Ano selecionado]
    """

    # condições de filtro são o ano e o tipo de movimeentação
    filters = (
        (dataset["ANO"] == year_value)
        & (dataset["MOVIMENTACAO"] == operation)
        & (dataset["COD_NCM"] == product_value)
    )
    # agrupa por mês, e soma as colunas com as métricas de movimentação
    df = dataset[filters].groupby(by="MES")[INDICATOR_OPTIONS].sum()
    df.reset_index(level=0, inplace=True)  # remove MES como index

    fig = df.plot(
        kind="bar",
        y=indicator,
    )

    # Configurações dos axes
    # https://plotly.com/python/axes/#set-axis-title-text-with-plotly-express

    # Como formatar os ticks
    # https://plotly.com/python/tick-formatting/

    fig.update_layout(
        xaxis=dict(tickmode="array", tickvals=list(range(13)), ticktext=MONTHS)
    )

    return fig


@app.callback(
    dash.dependencies.Output("via-pie-plot", "figure"),
    [
        dash.dependencies.Input("operation-options-dropdown", "value"),
        dash.dependencies.Input("product-options-dropdown", "value"),
        dash.dependencies.Input("year-slider-input", "value"),
    ],
)
def update_via_pie_plot(
    operation: str,
    product_value: str,
    year_value: int,
):
    """Atualiza o gráfico de pizza
    com a utilização percentual da via.

    Argumentos:
        operation (str):  [Movimentação selecionada (importação ou exportação)]
        indicator (str):  [Métrica selecionada (valor, valor por peso, etc)]
        uf_value (str):   [Estado selecionada]
        year_value (int): [Ano selecionado]
    """

    title = "Utilização percentual da via"

    # condições de filtro são o ano e o tipo de movimeentação
    filters = (
        (dataset["ANO"] == year_value)
        & (dataset["MOVIMENTACAO"] == operation)
        & (dataset["COD_NCM"] == product_value)
    )

    filtered = dataset[filters]

    # Calcula o uso percentual da via
    count = pd.DataFrame(
        {
            "code": filtered["COD_VIA"].value_counts().index,
            "count": filtered["COD_VIA"].value_counts().values,
        }
    )
    total = count["count"].sum()
    count["as_percentage"] = count["count"].apply(lambda x: round(x / total * 100))

    # Personalizações do pie chart
    # https://plotly.com/python/pie-charts/
    fig = px.pie(count, values="as_percentage", names="code", title=title)

    return fig