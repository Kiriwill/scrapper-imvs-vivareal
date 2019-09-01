from unittest.mock import Mock
from services.crawler_data_territorio.mocks.html import html
import requests

# Mock para requests
def mock_get_data_from_url(url):
    response = mockResponse()
    if response.status_code != 200: raise ConnectionError("Status Code != 200!")
    if response.text == '': raise ConnectionError("Text html retornou nulo.")

    return response
class mockResponse:
    status_code = 300
    elapsed = 100
    text = ''