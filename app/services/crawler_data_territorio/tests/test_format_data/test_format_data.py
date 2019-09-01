import unittest
from services.crawler_data_territorio.scrapper_listings import config

from services.crawler_data_territorio.core import text_to_json
from services.crawler_data_territorio.core import cut_text_from_text
from services.crawler_data_territorio.core import get_inneritems_from_dict
from services.crawler_data_territorio.core import filter_by
from services.crawler_data_territorio.core import extract_data_from_dict
from services.crawler_data_territorio.core import extract_data_from_list_of_dicts

from services.crawler_data_territorio.mocks.html import html
from services.crawler_data_territorio.mocks.html import tag
from services.crawler_data_territorio.mocks.html import listings
from services.crawler_data_territorio.mocks.mocks_data import mock_text_to_json
from services.crawler_data_territorio.mocks.mocks_data import mock_listing_filtered
from services.crawler_data_territorio.mocks.mocks_data import mock_listings
from services.crawler_data_territorio.mocks.mock_return_from_main import return_from_main

class testDataFormat(unittest.TestCase):
    # Dados estão em formato apropriado para ser formatado?
    def test_data_is_in_dict_format(self):
        self.assertTrue(cut_text_from_text(tag, '"result":', '},"page":{').startswith('{'))
        self.assertTrue(cut_text_from_text(tag, '"result":', '},"page":{').endswith('}'))

    # O retorno é um dict?
    def test_return_is_json(self):
        self.assertTrue(isinstance(text_to_json(listings), dict))

    # Se o parametro passado não existir raise erro?
    def test_if_key_dont_exist_raise_error(self):
        with self.assertRaises(KeyError): get_inneritems_from_dict(
            text_to_json(listings), 
            'listings',
            'tagAusente', 
            0)
    
    # Retorna dados especificos de um imóvel?
    def test_return_especific_values_from_listing(self):
        listing = ''
        self.maxDiff=None
        self.assertEqual(get_inneritems_from_dict(
            mock_text_to_json(listing),
            "id"
        ), {'id': '2436011588'})
        
        self.assertEqual(get_inneritems_from_dict(
            mock_text_to_json(listing),
            "bedrooms"
        ), {"bedrooms": [2]})

        self.assertEqual(get_inneritems_from_dict(
            mock_text_to_json(listing),
            "bathrooms"
        ), {"bathrooms": [3]})

        self.assertEqual(get_inneritems_from_dict(
            mock_text_to_json(listing),
            "parkingSpaces"
        ), {"parkingSpaces": [2]})

        self.assertEqual(get_inneritems_from_dict(
            mock_text_to_json(listing),
            "usableAreas"
        ), {"usableAreas": [112]})


        self.assertEqual(get_inneritems_from_dict(
            mock_text_to_json(listing),
            "pricingInfos"
        ), {"pricingInfos": [
                    {
                        "period": "MONTHLY",
                        "yearlyIptu": "400",
                        "price": "4000",
                        "rentalTotalPrice": "4880",
                        "businessType": "RENTAL",
                        "monthlyCondoFee": "880"
                    }
                ]})

        self.assertEqual(get_inneritems_from_dict(
            mock_text_to_json(listing),
            "address"
        ), {"address": {
                    "country": "Brasil",
                    "state": "São Paulo",
                    "city": "Barueri",
                    "neighborhood": "Alphaville 18 Forte",
                    "street": "Avenida Ômega",
                    "streetNumber": "171",
                    "unitNumber": "",
                    "zipCode": "06472005",
                    "locationId": "BR>Sao Paulo>NULL>Barueri>Barrios>Alphaville 18 Forte",
                    "zone": "Bairros",
                    "district": "",
                    "geoLocation": {
                        "location": {
                            "lat": -23.484829,
                            "lon": -46.851078
                        },
                        "precision": "ROOFTOP",
                        "optionalPrecision": "precision"
                    }
                }})

    # Retorna dict com dados que pedi no parametros?
    def test_return_especific_value_in_dict_from_dict(self):
        data = extract_data_from_dict(filter_by(mock_listings, config.B_TYPE)[0]['listing'], ["id","bedrooms", "bathrooms", "parkingSpaces", "usableAreas", "pricingInfos", "address"])
        self.assertTrue(data.get('id'))
        self.assertTrue(data.get('bedrooms'))
        self.assertTrue(data.get('bathrooms'))
        self.assertTrue(data.get('parkingSpaces'))
        self.assertTrue(data.get('usableAreas'))
        self.assertTrue(data.get('pricingInfos'))
        self.assertTrue(data.get('address'))
        
    def test_return_especific_values_from_list_of_dicts(self):
        self.assertTrue(extract_data_from_list_of_dicts(return_from_main["listings"], ["pricingInfos"]))

if __name__ == "__main__":
    unittest.main()