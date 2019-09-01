# Modulos
from config import * 
import logging as logger
import traceback

# Serviços secundários
from services.data_analysis.core import make_data_analysis
from services.crawler_data_territorio.core import scrapper_data_by_url_vivareal
from services.data_analysis.tools.core import get_max_by_list

def record_analysed_listing_data(place:str, num:str, id_condominio:int):
    '''
    Faz raspagem e grava dados de todos os imóveis no condominio.
    ------
    Parameters
    place: logradouro (str)
    num: numero (int)
    ------
    return
        bool de mensagem de gravação com sucesso.
    '''
    
    # Certique-se que não há parametros inválidos
    assert (place not in ['', ' ', [], None, ['']]), f"Logradouro para busca inválido. Não preenchido ou nulo. Logradouro recebido: {place}"
    assert (num not in ['', ' ', [], None, [''], 0]), f"Num para busca inválido. Não preenchido ou nulo. Numero recebido: {num}"
    assert (id_condominio not in ['', ' ', [], None, [''], 0]), f"idCondominio para busca inválido. Não preenchido ou nulo. idCondominio recebido: {id_condominio}"
    assert (isinstance(place,str) and isinstance(num,str)), f"Logradouro ou número não são dos tipos correto (string e inteiro). São {type(place)} e {type(num)}"
    assert (isinstance(id_condominio,int)), f"idCondominio não é do tipo correto (int), é {type(id_condominio)}"

    logger.info("Executando raspagem de dados.")

    # Executa raspagem dos dados do site e transforma-os em um json
    raw_data = scrapper_data_by_url_vivareal(place,num, REQUERED_DATA_LISTINGS, REQUERED_DATA_HEADER, header=True)

    # Se não obtém nenhum link da pesquisa grava como "não encontrada"
    if raw_data == 0:
        return False
    
    # Se não há conteudo na pagina do condominio 
    if len(raw_data.get('listings')) == 0:
        return False

    # Obtém numero maximo de tipologia
    typology = [b['bedrooms'][0] for b in raw_data['listings'] if len(b['bedrooms']) > 0]
    max_num_typology = get_max_by_list(typology, int)['max']

    # Se não há tipologias
    if max_num_typology == 0:
        return False

    for n in range(1, max_num_typology+1):
        # Executa analise dos dados
        analysed_data = make_data_analysis(raw_data['listings'], FILTER_KEY, [n])

        # Se não existir nenhum imóvel com esta tipologia
        if analysed_data == 0: continue

        # Grava resultado das análises
        #############################

        logger.info(f"Dados da tipologia gravados com sucesso.")

