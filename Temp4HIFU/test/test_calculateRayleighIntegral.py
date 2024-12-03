import unittest
import numpy as np
import pandas as pd 
import sys
sys.path.append('../Temp4HIFU')
from Temp4HIFU import calculateRayleighIntegral

# Test Constants
trans = dict(freq=1*1e6, radius=0.02, focus=0.05, initPressure=1*1e6)
medium = dict(name='Water', speed=1500, density=1000, absCoeff=0.025, specHeatCap=4180, thermDiff=1.46*1e-7)
field = dict(numAxialStep = 100, numRadialStep = 100)

# Load Test Data (MATLAB)
testdataDir = 'https://raw.githubusercontent.com/C2H5OH-Consumer/Temp4HIFU/refs/heads/main/Temp4HIFU/test/testData/'
testData_z_axis = np.array(pd.read_csv(testdataDir + 'testData_z_axis.csv',header=None))
testData_pressure2D = np.array(pd.read_csv(testdataDir + 'testData_pressure2D.csv'))

print(len(testData_z_axis))
print(len(testData_pressure2D))

# Test Functions
class TestFunctions(unittest.TestCase):

    def test_calculateRayleighIntegral(self):
        """
        Test if function completes fully - iscomplete
        """
        df_pressure2D, z_axis, r_axis, iscomplete = calculateRayleighIntegral.generateField(trans,medium,field)
        self.assertTrue(iscomplete == 1)
        print('> test_calculateRayleighIntegral PASS')


# Finish
if __name__ == "__main__":
    unittest.main()

