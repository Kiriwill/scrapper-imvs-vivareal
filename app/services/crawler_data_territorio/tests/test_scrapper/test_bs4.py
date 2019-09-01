import unittest
# Métodos
from services.crawler_data_territorio.tools.core import instantiate_bs4
from services.crawler_data_territorio.tools.core import get_data_from_url
from services.crawler_data_territorio.tools.core import get_data_from_bs4_object
from services.crawler_data_territorio.tools.core import verify_search_number_results
from services.crawler_data_territorio.tools.core import filter_pages_by_status_code

# Mocks
from services.crawler_data_territorio.scrapper_links_condominios.config import URL_GOOGLE
from services.crawler_data_territorio.mocks.html import html
from services.crawler_data_territorio.mocks import mocks_google
from services.crawler_data_territorio.mocks.configs_mock import *


class test_bs4(unittest.TestCase):
    '''
    Testes para raspagem de dados com bs4.
    '''

    # Retona um objeto?
    def test_bs4_return_bs4_object(self):
        self.assertTrue(isinstance(instantiate_bs4(html), object), "Não é um objeto")
    
    # Retorno é diferente de nulo?
    def test_get_data_from_tag_is_not_none(self):
        self.assertIsNotNone(get_data_from_bs4_object(instantiate_bs4(html), 'script', "window.dataLayer ="))
    
    # O retorno é uma lista?
    def test_get_data_from_tag_equal_string(self):
        self.assertIsInstance(get_data_from_bs4_object(instantiate_bs4(html), 'script', "window.dataLayer ="), str, "Não é uma string.")
    
    # Retorna conteúdo da tag script que contém o json?
    def test_get_data_from_tag_return_especific_script_text(self):
        if "window.dataLayer =" in get_data_from_bs4_object(instantiate_bs4(html), 'script', "window.dataLayer ="):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "Não contém camada de dados para extrair (dataLayer).")

    # Se endereço contiver links de condomíno não raise error?
    def test_if_there_is__link_in_search_dont_raise_error(self):
        bs4_obj = instantiate_bs4(get_data_from_url(MOCK_URL_GOOGLE).text)
        self.assertTrue(verify_search_number_results(bs4_obj, 'div', 'Nenhums resultado encontrado'))

    # Se endereço não contiver nenhum link de condomíno raise error?
    def test_if_there_is_no_link_in_search_raise_error(self):
        bs4_obj = instantiate_bs4(get_data_from_url(MOCK_URL_GOOGLE).text)
        with self.assertRaises(AssertionError): verify_search_number_results(bs4_obj, 'div', 'Nenhum resultado encontrado')

    # Retorna paginas cujo status é 200?
    def test_return_pages_which_status_code_equal_200(self):
        links = filter_pages_by_status_code(LINKS_STATUS_CODE, 200)
        self.assertEqual(len(links), 4)

if __name__ == "__main__":
    unittest.main()