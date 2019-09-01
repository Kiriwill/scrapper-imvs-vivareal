import unittest
from services.data_analysis.tools import *
from services.data_analysis.mocks.configs_mock import *

from services.crawler_data_territorio.mocks.mock_return_from_main import return_from_main

class testDataAnalysis(unittest.TestCase):
    '''# Transforma todos os valores de uma coluna em inteiros?
    def test_get_mean_by_list_return_int(self):
        self.assertIsInstance(get_mean_by_list([p['pricingInfos'][0]['price'] for p in prices], int), float or int)
        self.assertIsInstance(get_mean_by_list([b['bathrooms'][0] for b in bathrooms], int), float or int)
        self.assertIsInstance(get_mean_by_list([b['usableAreas'][0] for b in usable_areas], int), float or int)
        self.assertIsInstance(get_mean_by_list([b['parkingSpaces'][0] for b in parking_spaces], int), float or int)

    def test_get_median_by_list_return_int(self):
        self.assertIsInstance(get_median_by_list([p['pricingInfos'][0]['price'] for p in prices], int), float or int)
        self.assertIsInstance(get_median_by_list([b['bathrooms'][0] for b in bathrooms], int), float or int)
        self.assertIsInstance(get_median_by_list([b['usableAreas'][0] for b in usable_areas], int), float or int)
        self.assertIsInstance(get_median_by_list([b['parkingSpaces'][0] for b in parking_spaces], int), float or int)

    def test_get_max_by_list_return_int(self):
        self.assertTrue(get_max_by_list([p['pricingInfos'][0]['price'] for p in prices], int))
        self.assertTrue(get_max_by_list([b['bathrooms'][0] for b in bathrooms], int))
        self.assertTrue(get_max_by_list([b['usableAreas'][0] for b in usable_areas], int))
        self.assertTrue(get_max_by_list([b['parkingSpaces'][0] for b in parking_spaces], int))
    
    def test_get_min_by_list_return_int(self):
        self.assertTrue(isinstance(get_min_by_list([p['pricingInfos'][0]['price'] for p in prices], int),int or float))
        self.assertTrue(isinstance(get_min_by_list([b['bathrooms'][0] for b in bathrooms], int), int or float))
        self.assertTrue(isinstance(get_min_by_list([b['usableAreas'][0] for b in usable_areas], int), int or float))
        self.assertTrue(isinstance(get_min_by_list([b['parkingSpaces'][0] for b in parking_spaces], int), int or float))'''

    def test_filter_dict_by_key_and_value_return_listings_with_especific_num_of_bedrooms(self):
        filtered = filter_dict_by_key_and_value(return_from_main['listings'], "bedrooms", [2])
        wish = [l for l in return_from_main['listings'] if l['bedrooms'] == [2]]
        self.assertEqual(len(wish), len(filtered))

        
if __name__ == "__main__":
    unittest.main()