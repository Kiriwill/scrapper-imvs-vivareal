'''
Variaveis e constantes utilizadas no módulo crawler_data_territorio
'''

###################### Configurações da função "get_links_from_google" #########################

# Link para o buscador
URL_GOOGLE = 'https://www.google.com/search?q=site:www.vivareal.com.br/condominio+"%s"'

# Numero maximo de links por pagina
MAX = 100

# Tag que estão os links no buscador
TAG_ATRIBUTE = 'a'

# Atributo para a tag do link no buscador
ATTRS = 'href'

# Atributo que espericifica a tag
CONDITION_GOOGLE = 'https://www.vivareal.com.br/condominio/'

# Status code que deseja obter da pesquisa
STATUS_CODE_SEARCH = 200


###################### Configurações para a função "verify_search_number_results" ###################

TAG_NUM_RESULTS = 'div'
CONDITION_NUM_RESULTS = 'Nenhum resultado encontrado'