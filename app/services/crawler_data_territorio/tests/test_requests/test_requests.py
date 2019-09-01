import unittest
from services.crawler_data_territorio.core import get_data_from_url
from services.crawler_data_territorio.mocks.mocks_page import mock_get_data_from_url
from services.crawler_data_territorio.scrapper_links_condominios.config import URL

class testRequest(unittest.TestCase):
    '''
    Classe de testes para requisições HTTP
    '''
    # Request retorna um html?
    def test_get_data_from_site(self):
        self.assertTrue('<!DOCTYPE' in get_data_from_url('https://www.vivareal.com.br/condominio/soul-da-lapa-centro-id-679e9058-40d9/').text)

    # Sai uma string?
    def test_return_from_site_is_str(self):
        self.assertTrue(isinstance(get_data_from_url('https://www.vivareal.com.br/condominio/soul-da-lapa-centro-id-679e9058-40d9/').text, str))
    
    # Còdigo de retorno é 200?
    def test_status_code_200_from_request(self):
        self.assertEqual(get_data_from_url('https://www.vivareal.com.br/condominio/soul-da-lapa-centro-id-679e9058-40d9/').status_code, 200)

    # Diferentes urls todos os testes resultam em correto?
    def test_differents_urls_pass_all_tests(self):
        self.assertTrue(get_data_from_url('https://www.vivareal.com.br/condominio/soul-da-lapa-centro-id-679e9058-40d9/'))
    
    # Retorno da request é diferente de nulo?
    def test_return_from_site_is_not_null(self):
        self.assertNotEqual('', get_data_from_url('https://www.vivareal.com.br/condominio/soul-da-lapa-centro-id-679e9058-40d9/'))

if __name__ == "__main__":
    unittest.main()