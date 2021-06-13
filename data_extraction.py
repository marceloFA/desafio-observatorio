""" Script para extrair os dados do site 'Comércio Exterior - Governo Federal' """

"""
Requisitos:

1 - O script deve checar no site quais são os últimos 3 anos
(ou arquivos) disponíveis, e fazer o download somente desses 3
últimos anos.

O script precisa renomear as variáveis para o padrão que
utilizamos:

2 - ANO, MES, COD_NCM, COD_UNIDADE, COD_PAIS, SG_UF,
COD_VIA, COD_URF, VL_QUANTIDADE, VL_PESO_KG,
VL_FOB

3 - Preencher com zero à esquerda as seguintes variáveis
nas seguintes quantidades: COD_NCM= 8, COD_URF= 7, COD_SH4=
4, COD_PAIS=3.
Exemplo: Se o valor da coluna COD_NCM vem assim: 8796387, ele tem
que ficar assim: 08796387.

Script precisa unir todas as bases ao final (dos últimos 3
anos de importação e exportação), criando assim uma coluna para
identificar se aquilo é um registro de importação ou exportação. O
nome desta coluna deve ser MOVIMENTACAO.
"""
# chega no site

# pega os dados dos últimos tres anos para importação

# pega os dados dos últimos tres anos para exportação

#salva no diretorio de data/