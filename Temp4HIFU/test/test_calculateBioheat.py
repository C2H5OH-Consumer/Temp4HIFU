import unittest
import numpy as np
import pandas as pd 
import sys
sys.path.append('../Temp4HIFU')
from Temp4HIFU import calculateBioheat

# Test Constants
trans = dict(freq=1*1e6, radius=0.02, focus=0.05, initPressure=1*1e6)
medium = dict(name='Water', speed=1500, density=1000, absCoeff=0.025, specHeatCap=4180, thermDiff=1.46*1e-7)
heat = dict(numTime = 5e-3, HeatTime = float(30), CoolTime = float(30), DutyCycle = int(100))
observeZ = 0.05
observeR = 0

# Load Sample Data (PYTHON)
sampledataDir = 'https://raw.githubusercontent.com/C2H5OH-Consumer/TempCompliance4HIFU/refs/heads/main/TempCompliance4HIFU/sampledata/'
placeholder_df = sampledataDir + '/df_pressure2D_placeholder.csv'
placeholder_z = sampledataDir + '/z_axis_placeholder.csv'
placeholder_r =  sampledataDir + '/r_axis_placeholder.csv'
df_pressure2D = np.array(pd.read_csv(placeholder_df))[:,1:]
z_axis = np.array(pd.read_csv(placeholder_z))[:,1]
r_axis = np.array(pd.read_csv(placeholder_r))[:,1]

# Load Test Data (MATLAB)
testdataDir = 'https://raw.githubusercontent.com/C2H5OH-Consumer/Temp4HIFU/refs/heads/main/Temp4HIFU/test/testData/'
testData_time_axis = (pd.read_csv(testdataDir + 'testData_timeVec.csv',header=None))
testData_temp_Vec = (pd.read_csv(testdataDir + 'testData_tempVec.csv',header=None))
# Convert to Lists
testData_t_axis = testData_time_axis[0].tolist()
testData_temp_Vec = np.array(testData_temp_Vec)


##### ---- ##### ---- ##### ---- TESTING ---- ##### ---- ##### ---- #####


# FUNCTION TO TEST AGAINST
time_axis, temp_vec, Q, iscomplete = calculateBioheat.generateVector(observeZ,observeR,trans,medium,heat,df_pressure2D,z_axis,r_axis,iscomplete=0)


# Test Functions
class TestFunctions(unittest.TestCase):
    """
    1. Assert True for Completion
    2. Assert Equal Length Check for Time Axis
    3. XX Assert Equal Check for Time Axis
    4. Assert Equal Length Check for Temp
    5. XX Assert Almost Equal Check for Temp
    """
    def test_calBioheat_tempVec(self):
        """
        Assert Equal Length Check for Temp
            XX Assert Almost Equal Check for Temp
        """
        # Assert Equal Length Check for Pressure2D
        self.assertEqual(len(testData_temp_Vec),len(temp_vec))
        # Assert Almost Equal Output for Pressure2D
        # self.assertAlmostEqual(df_pressure2D,testData_pressure2D)
        print('> test_calBioheat_tempVec PASS')


    def test_calBioheat_timeAxis(self):
        """
        Assert Equal Length Check for Time Axis
            XX Assert Almost Equal Check for Time Axis
        """
        self.assertEqual(len(testData_time_axis),len(time_axis))
        # Assert Almost Equal Output for R Axis (since zero component is a float on the order of 1e-19 or smaller)
        # self.assertAlmostEqual(r_axis, testData_r_axis) 
        print('> test_calBioheat_timeAxis PASS')


    def test_calBioheat_complete(self):
        """
        Assert True for Completion
        """
        self.assertTrue(iscomplete)
        print('> test_calBioheat_complete PASS')


# Finish
if __name__ == "__main__":
    unittest.main()