## --------------- Request ---------------- ##

# Executa requisição de html da pagina
def get_data_from_url(url):
    '''
    Executa requisição HTTP para uma URL.
    return 
        objeto de resposta da requisição
    '''
    import requests
    from .config_core import random_headers

    response = requests.get(url, headers=random_headers(), timeout=10.0)
    if response.status_code != 200: raise ConnectionError(f"Erro ao fazer a requisição da pagina {url}. Status Code != 200! Status:{response.status_code} Razão: {response.reason}")
    if response.text == '': raise ConnectionError(f"Texto html retornou nulo! Verifique se não houve alterações na pagina: {url}")

    return response

## --------------- Scrapper --------------- ##

# Cria objeto do bs4
def instantiate_bs4(html:str):
    '''
    Cria objeto bs4 do html
    return
        object
    '''
    assert (isinstance(html, str)), f"HTML não é uma string. Impossível iniciar a raspagem de dados. HTML recebido: {html}"

    from bs4 import BeautifulSoup as bs
    return bs(html, 'html.parser')

# Obtém atributo de um tag
def get_attribute_from_tag(site_bs4_object:object, tag:str, attrs:str, condition_attrs:str):
    '''
    Faz raspagem de dados do(s) "attribute(s)" de uma tag
    Parameters
        site_bs4_object (objeto resultado da função instantiate_bs4)
        tag (string html, ex: 'script')
        attrs: (str dos atributos: ex: 'href')
        condition (texto ou parte de, que identifica o attributo)
    Return
        lista com strs dos atributos
    '''
    import re
    try:
        a_tags_with_href = site_bs4_object.findAll(tag, href=re.compile('^'+condition_attrs))
        content = [item.attrs['href'] for item in a_tags_with_href]
        return content
    except:
        raise AttributeError(f"Produção: Tag - {tag} - não encontrada. Verifique se não houve alterações na página.")
    

# Obtém conteúdo de uma tag
def get_data_from_bs4_object(site_bs4_object:object, tag:str, condition_content=''):
    '''
    Faz raspagem dos dados do "content" de uma tag específica.
    parameters
        SiteBs4Object (objeto resultado da função instantiate_bs4)
        tag (string html, ex: 'script')
        position (numero da posição da tag no html)
        condition (texto interno que identifica a tag ser encontrada)
    return
        string com texto do conteúdo da tag
    '''
    try:
        for t in site_bs4_object.find_all(tag):
            if condition_content in t.text:
                return t.text
        raise AttributeError(f"Produção: Tag - '{tag}' com o conteudo '{condition_content}' - não encontrada. Verifique se não houve alterações na página (vivareal/condominio).")
    except:
        raise AttributeError(f"Produção: Tag - '{tag}' com o conteudo '{condition_content}' - não encontrada. Verifique se não houve alterações na página (vivareal/condominio).")

## --------------- Tratamento dos dados --------------- ##

# Recorta texto para o formato que seja legível por json.loads
def cut_text_from_text(text:str, startswith:str, endswith:str):
    ''' 
    Recorta parte de um texto desejado
    Parameters
        text (texto a ser transformado)
        startswith (primeira palavra ou frase anterior ao texto que deseja capturar)
        endswith (primeira palavra ou frase posterior ao texto que deseja capturar)
    return
        string recortada
    '''
    assert (text not in ['', ' ', [], None, ['']]), "Produção: Nenhum dado a ser extraído da pagina. Verifique se não houve alterações na página (vivareal/condominio)."
    r = text.split(startswith,1)[1].split(endswith, 1)[0]
    return r

# Transforma texto em dicionario legivel
def text_to_json(data:str):
    '''
    Transforma texto em tipo json
    Parameters
        data (texto pronto para formatar)
    '''
    import json
    try:
        assert (data not in ['', ' ', [], None, ['']] and isinstance(data, str))
        resulted_data = json.loads(data)
    except: raise TypeError("Produção: Conversão dos dados para json não realizada. Nenhum dado recebido da página. Verifique se não houve alterações na página (vivareal/condominio).")
    return resulted_data

# Filtra dados por tipo (aluguel ou venda)
def filter_by(resource:dict, b_type:str):
    '''
    Filtra dados de um imóvel
    Parameters
        resource (listing de imóveis)
        b_type (SALE ou RENTAL)
    return
        lista com imóveis
    '''
    try:

        d = [listing for listing in resource['listings']
        if listing['listing']['pricingInfos'][0]['businessType'] == b_type 
        or listing['listing']['pricingInfos'][1]['businessType'] == b_type]
    except:
        if len([listing for listing in resource['listings'] if listing['listing']['pricingInfos'][0]['businessType'] == b_type]) == 0:
            return 0 
        d = [listing for listing in resource['listings'] if listing['listing']['pricingInfos'][0]['businessType'] == b_type]
    return d

# Obtém um dado de um dicionário
def get_inneritems_from_dict(d:dict, upperkey:str, lowerkey:str = False, position:int = False):
    '''
    Obtém dado de um dicionário, retorna um novo dicionário
    Parameters
        d: origem do dado
        upperkey: key acima da key a ser buscada ou key a ser buscada (caso dict de um só nivel)
        lowerkey: key a ser buscada
        position: posição na lista (se houver)
    return
        novo dicionario com dados escolhidos
    '''
    try:
        if lowerkey != False and position != None:
            return d[upperkey][position][lowerkey]
        else:
            return {upperkey: d[upperkey]}
    except: raise KeyError(f"Produção: Ambas ou uma das keys ({upperkey} e {lowerkey}) não foi encontrada.")

# Extrai dados de UM dicionario
def extract_data_from_dict(origin:dict, items:list):
    '''
    Extrai dados de um dicionário e forma um novo com os dados requeridos
    (somente para keys do primeiro nível)
    Parameters
        origin (dado a ser extraido)
        items (lista de itens desejados)
    '''
    import traceback
    try: 
        assert {k:v for (k,v) in origin.items() if k in items} != {}
        return {k:v for (k,v) in origin.items() if k in items}
    except AttributeError as expt:
        raise TypeError(f"Origem da extração é de tipo incorreto. {repr(expt)}")
    except AssertionError:
        raise KeyError("Produção: Nenhum dado dos condominios encontrado para extração. Verifique se houve alterações na forma que a pagina apresenta os dados (json ao final da pagina)")

# Extrai dados de uma lista de dicionários
def extract_data_from_list_of_dicts(origin:list, requered_data:list):
    '''
    Extrai dados desejados de dicionários que estão dentro de uma lista.
    (só pra primeiro nível)
    Parameters
        origin (lista originaria com os dicionários)
        requered_data (dados a serem extraidos)
    return
        lista com dicionários filtrados
    '''
    assert (origin not in ['', ' ', None, []]), "Produção: Dados de origem da extração inválidos. Não podem ser nulos."
    assert isinstance(origin,list) and isinstance(requered_data,list), "Origem da extração é de tipo incorreto."

    try:
        result = [extract_data_from_dict(i,requered_data) for i in origin]
    except AttributeError as expt:
        raise TypeError(f"Origem da extração é de tipo incorreto. {repr(expt)}")
    except AssertionError:
        raise KeyError("Produção: Nenhum condominio encontrado para extração. Verifique se houve mudanças na página dos condominio.")

    return result
    
# Verifica se existem condominios em uma rua
def verify_search_number_results(site_bs4_object:object, tag:str, condition_content=''):
    import re
    text_tags = [t.text for t in site_bs4_object.findAll(tag) if condition_content in t.text]
    assert (len(text_tags) == 0), "Produção: Nenhum condominio encontrado no endereço fornecido. Verifique se houve mudanças na página dos condominio."
    return True

# Atesta que paginas dos links existam
def filter_pages_by_status_code(links:list, status_code:int):
    import requests
    responses = [l for l in links if requests.get(l, timeout=10.0).status_code == 200]
    return responses