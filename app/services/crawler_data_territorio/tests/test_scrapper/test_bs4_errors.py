import unittest
from services.crawler_data_territorio.core import get_data_from_bs4_object
from services.crawler_data_territorio.core import instantiate_bs4
from services.crawler_data_territorio.mocks.html_with_errors import html

class test_bs4_raise_errors(unittest.TestCase):
    '''
    Classe de testes para tratamento de erros quando raspagem de dados não receber valores corretos.
    '''
    # Se a tag não existe retorna um erro?
    def test_raises_error_if_tag_not_exists(self):
        with self.assertRaises(AttributeError): get_data_from_bs4_object('vvvvvvvvv', 'script', 14, "window.dataLayer =")
    
    # Se não retorna o texto que desejo retona erro? 
    def test_raises_error_if_tag_not_contain_especific_content(self):
        with self.assertRaises(AttributeError): get_data_from_bs4_object(instantiate_bs4(html), 'script', 14, "window.dataLayer =")

if __name__ == "__main__":
    unittest.main()