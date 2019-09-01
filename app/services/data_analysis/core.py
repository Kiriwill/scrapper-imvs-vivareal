def make_data_analysis(data:dict, filter_key:str, filter_value):
    '''
    Efetua a analise de dados (media, mediana, max e min)
    '''
    assert (data != None and data != {}), f"Nenhum dado existente para análise. Verifique se houve alterações no html do site. Dados passados: {data}"

    from services.data_analysis.tools import filter_dict_by_key_and_value
    from services.data_analysis.data_from_listings.core import analyse_data_from_data

    try:
        # Filtra dados por tipologia
        raw = filter_dict_by_key_and_value(data, filter_key, filter_value)

        # Certifica-se que há dados a serem calculados
        if raw == 0 or raw == None or len(raw) == 0: return 0
        
        # Obtém número total de anuncios
        ads_num = len(raw)
        
        # Forma lista e analisa dados dos preços
        prices = [p['pricingInfos'][0]['price'] for p in raw if len(p['pricingInfos']) > 0]
        if len(prices) > 0:
            data_prices = analyse_data_from_data(prices, 'prices')
        else:
            data_prices = {'prices': {'mean':0, 'median':0, 'mode':0, 'max':0, 'min':0}}
        
        # Forma lista e analisa dados dos banheiros
        bathrooms = [b['bathrooms'][0] for b in raw if len(b['bathrooms']) > 0]
        if len(bathrooms) > 0:
            data_bathrooms = analyse_data_from_data(bathrooms, 'bathrooms')
        else:
            data_bathrooms = {'bathrooms': {'mean':0, 'median':0, 'mode':0, 'max':0, 'min':0}}

        # Forma lista e analisa dados das areas úteis
        usable = [u['usableAreas'][0] for u in raw if len(u['usableAreas']) > 0]
        if len(usable) > 0:
            data_usable = analyse_data_from_data(usable, 'usableAreas')
        else:
            data_usable = {'usableAreas': {'mean':0, 'median':0, 'mode':0, 'max':0, 'min':0}}

        # Forma lista e analisa dados das vagas
        parkings = [ps['parkingSpaces'][0] for ps in raw if len(ps['parkingSpaces']) > 0]
        if len(parkings) > 0:
            data_parkings = analyse_data_from_data(parkings, 'parkings')
        else:
            data_parkings = {'parkings': {'mean':0, 'median':0, 'mode':0, 'max':0, 'min':0}}

        result = {filter_value[0]: {**data_prices,**data_bathrooms,**data_usable,**data_parkings, **{'qtde_anuncios':ads_num}}}
        return result

    except Exception as expt:
        raise Exception(f"Erro na análise dos dados. {expt}")

    