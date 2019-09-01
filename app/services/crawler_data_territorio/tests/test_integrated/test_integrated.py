import unittest
from services.crawler_data_territorio.mocks.configs_mock import *
from services.crawler_data_territorio.core import *

# Mocks para testes integrados (configs na pasta mocks)
class testIntegrated(unittest.TestCase):

    '''# Se url nula deve retornar um erro
    def test_street_equal_null_raise_error(self):
        with self.assertRaises(Exception): core.scrapper_data_by_url_vivareal(ADRESS_NULL1, 132, REQUERED_DATA)
        with self.assertRaises(Exception): core.scrapper_data_by_url_vivareal(ADRESS_NULL2, 10, REQUERED_DATA)
    
    # Se endereço sem número ou/e logradouro retorna erro
    def test_there_isnt_number_or_street_raise_error_1(self):
        with self.assertRaises(Exception): core.scrapper_data_by_url_vivareal(ADRESS_COMPLETE,ADRESS_NULL2, REQUERED_DATA)
        with self.assertRaises(Exception): core.scrapper_data_by_url_vivareal(ADRESS_COMPLETE,ADRESS_NULL1, REQUERED_DATA)
    
    # Se logradouro não for string retorna erro?
    def test_adress_or_num_isnt_correct_type_raise_error(self):
        with self.assertRaises(Exception): core.scrapper_data_by_url_vivareal(1,NUM_COMPLETE, REQUERED_DATA)
        with self.assertRaises(Exception): core.scrapper_data_by_url_vivareal(ADRESS_COMPLETE,"Null", REQUERED_DATA)

    # Se dados necessários for nulo raise erro?
    def test_if_requered_data_is_null_or_not_list_raise_error(self):
        with self.assertRaises(Exception): core.scrapper_data_by_url_vivareal('Rua Oscar Freire', NUM_COMPLETE, [])
        with self.assertRaises(Exception): core.scrapper_data_by_url_vivareal('Rua Oscar Freire', NUM_COMPLETE, '')
        with self.assertRaises(Exception): core.scrapper_data_by_url_vivareal('Rua Oscar Freire', NUM_COMPLETE, None)
        with self.assertRaises(Exception): core.scrapper_data_by_url_vivareal('Rua Oscar Freire', NUM_COMPLETE, [''])'''

    def test_if_everything_ok_with_ok(self):
        data = scrapper_data_by_url_vivareal(ADRESS_COMPLETE,NUM_COMPLETE, REQUERED_DATA_LISTINGS,REQUERED_DATA_HEADER, header=True)
        with open('data.json', 'w') as file:
            file.write(str(data))
        self.assertTrue(scrapper_data_by_url_vivareal(ADRESS_COMPLETE,NUM_COMPLETE, REQUERED_DATA_LISTINGS,REQUERED_DATA_HEADER, header=True))
        self.assertTrue(scrapper_data_by_url_vivareal(ADRESS_COMPLETE,NUM_COMPLETE, REQUERED_DATA_LISTINGS))





if __name__ == "__main__":
    unittest.main()