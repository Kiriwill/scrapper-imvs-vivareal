# Readme 

> Aplicação para raspagem de dados e calculo dos dados dos condominios e imóveis do site Vivareal a partir da busca no Google. 

### Funcionamento

A aplicação se divide em etapas:

1) Lê logradouros, numeros e idCondominios do banco
Para cada endereço:
    a) Busca links do condominio no Google a partir do endereço
    b) Faz raspagem dos dados do site e transforma-os em um json
    c) Executa analise dos dados (obtém moda, media, mediana, max e min)
    d) Grava o resultado da análise dos dados no banco
    e) Grava os dados gerais do condominio (header) no banco

### Organização das pastas

/app/services/crawler_data_territorio*: subitens a e b;
/app/services/data_analysis*: subitem c;
/app**

*contém `config.py` com constantes de parametros
**contém `config.py` com constantes de parametros gerais