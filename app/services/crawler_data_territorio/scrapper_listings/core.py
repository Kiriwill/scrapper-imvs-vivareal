'''
Executa a extração dos dados dos imóveis
'''

from services.crawler_data_territorio import tools as core

def get_tag_content(url:str, tag_to_find:str, condition_tag:str):
    '''
    Obtém conteudos de uma tag a partir da url.
    Parameters
        url (Url objeto da raspagem)
        tag (Tag a ser encontrada)
        condition (Texto que identifica a tag)
    Return
        str com conteudo da tag
    '''
    
    # Executa requisição de html da pagina
    html = core.get_data_from_url(url)

    # Obtém conteúdo de uma tag
    tag = core.get_data_from_bs4_object(core.instantiate_bs4(html.text), tag_to_find, condition_tag)
        
    return tag

def execute_data_treatment(tag_content:str, cut_from_here:str, cut_to_here:str):
    '''
    Executa tratamento dos dados conforme parametros estabelecidos.
    Parameters
        tag (str do conteudo de uma tag)
        cut_from_here (primeira palavra ou frase anterior ao texto que deseja capturar)
        cut_to_here (primeira palavra ou frase posterior ao texto que deseja capturar)
    Return
        json em formato dict do contéudo
    '''
    # Obtém listagem de todos os imóveis
    text_listings = core.cut_text_from_text(tag_content, cut_from_here, cut_to_here)

    # Transforma dados em json
    json_listings = core.text_to_json(text_listings)

    return json_listings

def extract_data(json_origin:dict, bussines_type:str='', requered_data_listings:list=[], requered_data_header:list=[], header=False):
    '''
    Extrai dados conforme parametros.
    Parameters
        json_origin (dict originario com dados gerais)
        bussines_type (tipo de imóvel - 'SELL' or 'RENTAL')
        requered_data (dados que deseja extrair)
        header (a origem é header? se sim = True)
    '''
    from services.crawler_data_territorio.tools import extract_data_from_dict

    # Obtém lista de imóveis conforme tipo (venda ou aluguel)
    json_filtered = core.filter_by(json_origin, bussines_type)

    # Se não encontra nenhum imóvel para venda:
    if json_filtered != 0: 
        # Extrai dados 
        data = [extract_data_from_dict(listing['listing'],requered_data_listings) for listing in json_filtered]
    else:
        data = []

    # Extrai dados da header e a inclui no json
    if header: 
        data_header = extract_data_from_dict(header,requered_data_header)
        data = dict(header=data_header, listings=data)

    return data
