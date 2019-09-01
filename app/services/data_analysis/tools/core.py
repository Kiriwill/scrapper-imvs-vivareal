def get_mean_by_list(data:list, type_data:bool):
    '''
    Calcula a média de um conjunto de dados para um determinado tipo.
    Parameter
        data (lista com conjunto de dados do calculo)
        type_data (tipo de dado dos valores contidos em data)
    '''
    assert isinstance(data, list), "Dados a serem não estão no formato correto. Deve ser uma lista."
    assert (data not in ['', ' ', [], None, ['']]), "Produção: Dados para o calculo ausentes da média."
    import pandas as pd

    serie = pd.Series(data).astype(type_data)
    assert (serie.mean() not in ['', ' ', [], None, ['']]), f"Houve um erro na obtenção da média. Resultado do calculo: {serie.mean()}. Dados para o calculo: {serie}"
    m = serie.mean().round(decimals=1)

    return {'mean':m}

def get_median_by_list(data:list, type_data:bool):
    '''
    Calcula a mediana de um conjunto de dados para um determinado tipo.
        data (lista com conjunto de dados do calculo)
        type_data (tipo de dado dos valores contidos em data)
    '''
    assert isinstance(data, list), "Dados a serem a serem analisados para o calculo da mediana não estaõ no formato correto. Deve ser uma lista."
    assert (data not in ['', ' ', [], None, 0, ['']]), f"Produção: Dados para o calculo da mediana ausentes."

    import pandas as pd

    serie = pd.Series(data).astype(type_data)
    assert (serie.median() not in ['', ' ', [], None, ['']]), f"Houve um erro na obtenção da médiana. Resultado do calculo: {serie.mean()}. Dados para o calculo: {serie}"
    m = serie.median().round(decimals=1)

    return {'median': m}

def get_mode_by_list(data:list, type_data:bool):
    '''
    Calcula a moda de um conjunto de dados para um determinado tipo.
        data (lista com conjunto de dados do calculo)
        type_data (tipo de dado dos valores contidos em data)
    '''
    assert isinstance(data, list), "Dados a serem analisados não estão no formato correto. Deve ser uma lista."
    assert (data not in ['', ' ', [], None, ['']]), f"Produção: Dados para o calculo da moda ausentes. Dados: {data}"

    import pandas as pd

    serie = pd.Series(data).astype(type_data)
    try:
        m = serie.mode().round(decimals=1)
    except:
        raise Exception(f"Não foi possível obter a moda de uma série de dados. Resultado do calculo: {serie.mean()}. Dados para o calculo: {serie}")
    return {'mode': m[0]}

def get_max_by_list(data:list, type_data:bool):
    '''
    Calcula o valor maximo de um conjunto de dados para um determinado tipo.
        data (lista com conjunto de dados do calculo)
        type_data (tipo de dado dos valores contidos em data)
    '''
    assert isinstance(data, list), "Dados a serem analisados para o calculo do valor maximo não estaõ no formato correto. Deve ser uma lista."
    assert (data not in ['', ' ', [], None, ['']]), f"Produção: Dados para o calculo ausentes. Dados: {data}"

    import pandas as pd

    serie = pd.Series(data).astype(type_data)
    try:
        m = serie.max().round(decimals=1)
    except:
        raise Exception("Não foi possível obter o valor maximo de uma série de dados.")
    return {'max': m}

def get_min_by_list(data:list, type_data:bool):
    '''
    Calcula o valor minimo de um conjunto de dados para um determinado tipo.
        data (lista com conjunto de dados do calculo)
        type_data (tipo de dado dos valores contidos em data)
    '''
    assert isinstance(data, list), "Dados a serem analisados não estaõ no formato correto. Deve ser uma lista."
    assert (data not in ['', ' ', [], None, ['']]), f"Produção: Dados para o calculo ausentes. Dados: {data}"
    
    import pandas as pd

    serie = pd.Series(data).astype(type_data)
    try:
        m = serie.min().round(decimals=1)
    except:
        raise Exception(f"Não foi possível obter o valor minimo de uma série de dados. Resultado do calculo: {serie.mean()}. Dados para o calculo: {serie}")
    return {'min': m}

def filter_dict_by_key_and_value(origin: dict, filter_key:str, filter_value:str):
    assert (origin != None and origin != {}), f"Produção: Nenhum dado para a analise da tipologia. Verifique se houve alterações no html do site. Dados repassados: {repr(origin)}"

    r = [l for l in origin if l[filter_key] == filter_value]
    return r