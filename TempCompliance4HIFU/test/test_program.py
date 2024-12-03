# Imports
import unittest
import numpy as np
import pandas as pd 
import sys
sys.path.append('../TempCompliance4HIFU')
from TempCompliance4HIFU import startApp

class TestFunctions(unittest.TestCase):
    
    def test_startApp(self):
        startApp()
        print('> test_calculateBioheat PASS')

# Finish
if __name__ == "__main__":
    unittest.main()