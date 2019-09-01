import unittest
from services.crawler_data_territorio.core import text_to_json
from services.crawler_data_territorio.mocks.html import html
from services.crawler_data_territorio.core import get_inneritems_from_dict
from services.crawler_data_territorio.core import extract_data_from_dict

class testDataFormatErrors(unittest.TestCase):
    # Se não retorna dict raises error?
    def test_if_return_not_dict_raise_error(self):
        with self.assertRaises(TypeError): text_to_json()

    # Se tipo dos parametros for errado
    def test_if_type_parameter_not_dict(self):
        with self.assertRaises(TypeError): extract_data_from_dict('', ['ffff'])
        with self.assertRaises(TypeError): extract_data_from_dict('sss', ['ffff'])

    # Se não encontrar dados desejados retorna erro?
    def test_if_type_parameter_not_dict(self):
        with self.assertRaises(KeyError): extract_data_from_dict({'dfssdfd':1}, ['dddd'])

if __name__ == "__main__":
    unittest.main()