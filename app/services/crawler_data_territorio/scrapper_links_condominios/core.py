'''
Executa a extração dos links do buscador
'''
from services.crawler_data_territorio.tools.core import *
from services.crawler_data_territorio.tools import verify_search_number_results
from services.crawler_data_territorio.scrapper_links_condominios.config import *

def get_links_from_google(url:str, tag_atribute:str, attrs:str, condition_google:str):
    # Executa requisição de html da pagina (para consulta de paginas)
    html = get_data_from_url(url)

    # Verifica se existem de fato condominios no endereço
    try:
        verify_search_number_results(instantiate_bs4(html.text), TAG_NUM_RESULTS, CONDITION_NUM_RESULTS)
    except Exception as exp:
        return ''
        
    # Obtém conteúdo de uma tag
    links = get_attribute_from_tag(instantiate_bs4(html.text), tag_atribute, attrs, condition_google)

    # Filtra links que estejam funcionando
    links = filter_pages_by_status_code(links, STATUS_CODE_SEARCH)

    return links
