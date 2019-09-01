'''
Variaveis e constantes utilizadas no módulo crawler_data_territorio
'''

# Url Mock a ser encontrada
URL = 'https://www.vivareal.com.br/condominio/ouro-velho-pinheiros-id-9ff9c061-4436'

## -------- Obter conteúdo da tag --------##
# Tag a ser encontrada
TAG = 'script'
# Posição da tag
POS = 14
# Texto que identifica a tag
CONDITION_TAG = "window.dataLayer ="

## -------- Delimitações do contéudo da tag (header) --------##
FROM_HEADER = '},"condominium":'
TO_HEADER = ',"listings":{'

## -------- Delimitações do contéudo da tag (todos os imóveis) --------##
FROM_LISTINGS = '"result":'
TO_LISTINGS = '},"page":{'

## -------- Define tipo de imóveis ("SALE" ou "RENTAL") --------##
B_TYPE = 'SALE'

