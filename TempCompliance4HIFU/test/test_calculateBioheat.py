# Imports
import unittest
import numpy as np
import pandas as pd 
import sys
sys.path.append('../TempCompliance4HIFU')
from TempCompliance4HIFU import calculateBioheat

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
# testdataDir = ''
# testData_pressure2D = np.array(pd.read_csv('testData_pressure2D.csv'))


# Test Functions
class TestFunctions(unittest.TestCase):
    
    def test_calculateBioheat(self):
        """
        Test if function completes fully - iscomplete
        """
        time_axis, temp_vec, Q, iscomplete = calculateBioheat.generateVector(observeZ,observeR,trans,medium,heat,df_pressure2D,z_axis,r_axis,iscomplete=0)
        self.assertTrue(iscomplete == 1)
        print('> test_calculateBioheat PASS')



# Finish
if __name__ == "__main__":
    unittest.main()