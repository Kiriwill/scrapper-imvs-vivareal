import sys
import os

import unittest
from config import *

import core
from config import *

class testDataAnalysis(unittest.TestCase):
    def test_core_its_ok(self):
        self.assertTrue(core.record_analysed_listing_data_on_imv(ADRESS_COMPLETE, NUM_COMPLETE, 1))
    

if __name__ == "__main__":
    unittest.main()