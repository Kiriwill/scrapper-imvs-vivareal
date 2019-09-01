# Procedures
from services.crawler_data_territorio.scrapper_links_condominios import *
from services.crawler_data_territorio.scrapper_listings import *

# Configs
from services.crawler_data_territorio.scrapper_links_condominios.config import *
from services.crawler_data_territorio.scrapper_listings.config import *

def scrapper_data_by_url_vivareal(adress:str, num:str, requered_data:list, requered_data_header:list=False, header=False):
    try:
        # Certica-se que não há valores errados
        assert (adress not in ['', ' ', None]), f"Endereço inválido. Logradouro não pode ser nulo. Logradouro recebido: {adress}"
        assert (num not in ['', ' ', None]), f"Endereço inválido. Número não pode ser nulo.  Numero recebido: {num}"
        assert (isinstance(adress,str) and isinstance(num,str)), f"Número ou logradouro não são dos tipos corretos. Número precisa ser uma sentença (int) e logradouro uma sentença (string). Recebidos: {num} e {adress}"
        assert (requered_data not in ['', ' ', [], None, ['']] and isinstance(requered_data,list)), f"Dados necessários inválidos para raspagem dos dados inválidos. Dados a serem extraidos dos imóveis não foram passados. Endereço: {adress},{num}"
       
        # Cria URL da pesquisa.
        url = URL_GOOGLE % (adress.strip().replace(' ', '+')+','+num)

        # Obtém links do condominio do google.
        links = get_links_from_google(url,TAG_ATRIBUTE,ATTRS,CONDITION_GOOGLE)

        # Se não obtém nenhum link return flag
        if links in ['', ' ', [], None, [''], {}]: return 0

        # Obtém conteudos de uma tag a partir da url.
        tag_content = get_tag_content(links[0],TAG, CONDITION_TAG)

        # Executa tratamento dos dados (imóveis)
        json_listings = execute_data_treatment(tag_content,FROM_LISTINGS,TO_LISTINGS)
        
        if header:
            assert (requered_data_header not in ['', ' ', [], None, ['']] and isinstance(requered_data,list)), "Dados necessários inválidos. Dados a serem extraidos DO CONDOMINIO não foram passados."
            # Executa tratamento dos dados (header)
            json_header = execute_data_treatment(tag_content,FROM_HEADER,TO_HEADER)
            # Extrai dados (imoveis ou header + imoveis)
            data = extract_data(json_listings,B_TYPE,requered_data, requered_data_header, header=json_header)
        else:
            data = extract_data(json_listings,B_TYPE,requered_data)

        return data

    except Exception as expt:
        import traceback
        raise Exception(f"Houve um erro durante a raspagem de dados. Motivo do erro: {expt}.")