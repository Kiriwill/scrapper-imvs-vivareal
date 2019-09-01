
# Mocks para os testes integrados

## -------- Endereço, numero e link para iniciar a busca dos links --------- ##

ADRESS_NULL1 = " "

ADRESS_NULL2 = ""

ADRESS_COMPLETE = "Rua+Oscar+Freire"

ADRESS_WITH_SPACE = "Rua+Oscar+Freire "

ADRESS_OTHER_THINGS1 = "JIDdfe "

NUM_COMPLETE = 1456

MOCK_URL_GOOGLE = 'https://www.google.com/search?q=site:www.vivareal.com.br/condominio+"Rua Oscar Freire, 1948"'


## -------- Define dados a serem gravados --------- ##

REQUERED_DATA_LISTINGS = ["bedrooms", "bathrooms", "parkingSpaces", "usableAreas", "pricingInfos"]
REQUERED_DATA_HEADER = ["address", "shortUuid"]


## -------- Configurações para verificação de status das paginas (duas quebradas)

LINKS_STATUS_CODE = ['https://www.vivareal.com.br/condominio/confort-suites-oscar-freire-jardim-paulista-id-7fc31aa8-aee1/',
                    'https://www.vivareal.com.br/condominio/confort-suites-oscar-freire-jardim-paulista-id-7fc31aa8-6957/',
                    'https://www.vivareal.com.br/condominio/solar-dos-onze-cerqueira-cesar-id-94fa93f4-4c04/',
                    'https://www.vivareal.com.br/condominio/telma-cerqueira-cesar-id-c8cea2e0-46ae/',
                    'https://www.vivareal.com.br/condominio/telma-cerqueira-cesar-id-c8cea2e0-45ae/',
                    'https://www.vivareal.com.br/condominio/ana-liza-pinheiros-id-f43b5aa5-f4b4/']

