import unittest
from services.crawler_data_territorio.core import get_data_from_url
from services.crawler_data_territorio.mocks.mock_page import mock_get_data_from_url

class testRequestErrors(unittest.TestCase):
    '''
    Classe de testes para testar tratamento de erros quando requests não obtém valores corretos.
    '''
    # Se status code != 200 retorna erro?
    def test_status_code_different_from_200_raises_error(self):
        with self.assertRaises(ConnectionError): mock_get_data_from_url('https://httpstat.us/400')

    # Se for nulo retorna nulo?
    def test_raises_error_if_null_text(self):
       with self.assertRaises(ConnectionError): mock_get_data_from_url('http://www.e-try.com/black.htm')

    # Se a request demorar demais retorna erro?
    def test_raises_error_if_request_take_too_long(self):
        with self.assertRaises(Exception): get_data_from_url('http://www.e-try.com/black.htm')

if __name__ == "__main__":
    unittest.main()