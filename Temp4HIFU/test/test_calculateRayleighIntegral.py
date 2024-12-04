import unittest
import numpy as np
import pandas as pd 
import sys
sys.path.append('../Temp4HIFU')
from temp4hifu import calculateRayleighIntegral

# Test Constants
trans = dict(freq=1*1e6, radius=0.02, focus=0.05, initPressure=1*1e6)
medium = dict(name='Water', speed=1500, density=1000, absCoeff=0.025, specHeatCap=4180, thermDiff=1.46*1e-7)
field = dict(numAxialStep = 100, numRadialStep = 100)

# Load Test Data (MATLAB)
testdataDir = 'https://raw.githubusercontent.com/C2H5OH-Consumer/Temp4HIFU/refs/heads/main/Temp4HIFU/test/testData/'
testData_z_axis = (pd.read_csv(testdataDir + 'testData_z_axis.csv',header=None))
testData_r_axis = (pd.read_csv(testdataDir + 'testData_r_axis.csv',header=None))
testData_pressure2D = (pd.read_csv(testdataDir + 'testData_pressure2D.csv',header=None))
# Convert to Lists
testData_z_axis = testData_z_axis[0].tolist()
testData_r_axis = testData_r_axis[0].tolist()
testData_pressure2D = np.array(testData_pressure2D)


##### ---- ##### ---- ##### ---- TESTING ---- ##### ---- ##### ---- #####


# FUNCTION TO TEST AGAINST
df_pressure2D, z_axis, r_axis, iscomplete = calculateRayleighIntegral.generateField(trans,medium,field)


# Test Functions
class TestFunctions(unittest.TestCase):
    """
    1. Assert True for Completion
    2. Assert Equal Length Check for Z Axis
    3. XX Assert Equal Check for Z Axis
    4. Assert Equal Length Check for R Axis
    5. XX Assert Almost Equal Check for R Axis
    6. Assert Equal Length Check for Pressure2D
    7. XX Assert Almost Equal Check for Pressure2D
    """
    def test_calRayInt_press2D(self):
        """
        Assert Equal Length Check for Pressure2D
            XX Assert Almost Equal Check for Pressure2D
        """
        # Assert Equal Length Check for Pressure2D
        self.assertEqual(len(df_pressure2D),len(testData_pressure2D))
        # Assert Almost Equal Output for Pressure2D
        # self.assertAlmostEqual(df_pressure2D,testData_pressure2D)
        print('> test_calRayInt_press2D PASS')


    def test_calRayInt_rAxis(self):
        """
        Assert Equal Length Check for R Axis
            XX Assert Almost Equal Check for R Axis
        """
        self.assertEqual(len(r_axis),len(testData_r_axis))
        # Assert Almost Equal Output for R Axis (since zero component is a float on the order of 1e-19 or smaller)
        # self.assertAlmostEqual(r_axis, testData_r_axis) 
        print('> test_calRayInt_rAxis PASS')


    def test_calRayInt_zAxis(self):
        """
        Assert Equal Length Check for Z Axis
            XX Assert Equal Check for Z Axis
        """
        self.assertEqual(len(z_axis),len(testData_z_axis))
        # Assert Almost Equal Output for Z Axis
        # self.assertAlmostEqual(z_axis, testData_z_axis)
        print('> test_calRayInt_zAxis PASS')


    def test_calRayInt_complete(self):
        """
        Assert True for Completion
        """
        self.assertTrue(iscomplete)
        print('> test_calRayInt_complete PASS')


# Finish
if __name__ == "__main__":
    unittest.main()