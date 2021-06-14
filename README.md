# desafio-observatorio
Desafio técnico para a vaga de desenvolvedor Python na Observatório da Indústria

### Executando o projeto localmente
- 1. Instale os pacotes requeridos usando `pip3 install -r requirements.txt`
- 2. Obtenha os dados para a máquina local com ``python3 data_extraction.py`
- 3. Execute o app com `python3 app.py` então acesse http://127.0.0.1:8050

### Deploy no Heroku
Para acessar este app no Heroku, acesse https://desafio-observatorio.herokuapp.com/

### TODO:
 - Formata os dados da tabela pra ficarem com pontos nos milhares
 - Formata os dados da tabela para terem '%' nos valores percentuais
 - Encontra nomes fictícios mais bonitinhos para as colunas da tabela
 - FAZ OS ESTILOS DA PÀGINA VEIO
 - Pegar as categorias dos produtos para o primeiro plot fazendo join com a tabela de produtos
 - descorbre sobre a coluna COD_SH4 e adiciona 4 zeros no início de cada valor desta coluna
