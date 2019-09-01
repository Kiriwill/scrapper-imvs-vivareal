from modules import datahora

########### CONFIGURAÇÔES PARA O MODULO DATA_FROM_LISTINGS #################

# Mocks
ADRESS_COMPLETE = "Rua+Oscar+Freire"
NUM_COMPLETE = 1456

# Parametrização de dados a serem gravados (função "scrapper_data_by_url_vivareal")
REQUERED_DATA_LISTINGS = ["bedrooms", "bathrooms", "parkingSpaces", "usableAreas", "pricingInfos"]
REQUERED_DATA_HEADER = ["name"]

# Parametrização para filtragem por tipologia (função "make_data_analysis")
FILTER_KEY = 'bedrooms'

# Parametrização de dados a serem gravados no banco
TIPO_INFO = 'Automática'
TIMESTAMP = datahora.obter_datahora().strftime('%Y-%m-%dT%H:%M:%S')

