# Readme 

> Aplicação para raspagem de dados dos condominios e imóveis do site Vivareal a partir da busca no Google. 

### Funcionamento

A aplicação se divide em etapas:

1) busca lista de condominios no google pela rua;
2) obtém links dos condominios;
3) verifica quais estão funcionando;
4) requisita conteúdo do site do condominio;
5) obtém dados do condominio e dos imóveis;
6) transforma dados em json;
7) filtra dados dos imóveis e do condominio.

### Organização das pastas

/scrapper_links_condominios: etapas 1, 2 e 3*
/scrapper_listings: etapas 4 a 7*
/tools: funções úteis para todos os módulos*
/tests: testes divididos por módulos
/mocks: mocks gerais

*contém `config.py` com constantes de parametros
