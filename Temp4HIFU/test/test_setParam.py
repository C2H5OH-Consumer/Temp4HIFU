# Imports
import unittest
import sys
sys.path.append('../Temp4HIFU')
from Temp4HIFU import setParam

# Test Constants
medium = dict(name='Water', speed=1500, density=1000, absCoeff=0.025, specHeatCap=4180, thermDiff=1.46*1e-7)

# Test Functions
class TestFunctions(unittest.TestCase):
    
    def test_setParam_egg(self):
        """
        Test if Output for Egg White is Maintained
        """
        D1 = setParam.setMedium('Egg White',0,0,0,0,0)
        D2 = dict(
            name = 'Egg White',
            speed = 1546,
            density = 1045,
            absCoeff = 3.5,
            specHeatCap = 4270,
            thermDiff = 1.32 * 1e-7,
        )
        self.assertDictEqual(D1, D2)
        print('> test_setParam_egg PASS')


    def test_setParam_water(self):
        """
        Test if Output for Water is Maintained
        """
        D1 = setParam.setMedium('Water',0,0,0,0,0)
        self.assertDictEqual(D1, medium)
        print('> test_setParam_water PASS')

# Finish
if __name__ == "__main__":
    unittest.main()