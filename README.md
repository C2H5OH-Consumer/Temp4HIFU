# TEMP4HIFU

Author: Gerald Lee

*Final Project, BIOEN 537: Computational System Biology. University of Washington, Seattle*

A Python package designed to estimate the temperature increase due to high intensity focused ultrasound (HIFU) excitation. 

CURRENT ACTIVE VERSION = 0.2.1

LAST UPDATED: 12/05/2024

## BACKGROUND
High Intensity Focused Ultrasound (HIFU) and Focused Ultrasound (FUS) are used for thermal treatment of cells such as for cancer treatment. The generated increase of temperature during HIFU thermal treatment must be within safety guidelines for human use (44 degrees Celsius), which is essential for FDA approval and compliance. Accurate predictions of temperature bioeffects must be demonstrated through computational simulations before applications ex vivo and in vivo. Computational simulations requires modeling for both HIFU/FUS pressure fields and then the Bioheat equation; not complicated individually, but when combined can be tricky to navigate based on initial conditions.

Provided here is a tool to estimate bioheat from HIFU, usable as a GUI or importable as functions for integration with other code. The GUI provides an entry-friendly visualization of many aspects of bioheat due to HIFU. In this package, the heat input generated by HIFU is governed by the pressure output by the ultrasound transducer defined in the cylindrical space. The bioheat model solution is governed by a Forward Time Centered Space (FTCS) finite element model. *The given assumptions are that the system is axissymetric and linear in nature, and the bioheat equation does not consider blood perfusion and assumes heat propagates instantaneously.*

## INSTALLATION AND USE

### PRE-REQUISITES
In addition to the temp4hifu Python package, ensure you have the following additional Python packages installed into your machine:
1. numpy
2. pandas
3. dash

You may choose to pip install these packages separately, or as one line as follows: 

`pip install numpy pandas dash temp4hifu`

### USING GUI 
In Terminal, type:

`python -m temp4hifu.startApp`

Then follow the server link to view the application. 
*NOTE: To kill the app in terminal, CTRL+C*

An alternate set of lines to run:

`from temp4hifu.startApp import app`

`app.run(debug=True)`

### USING INDIVIDUAL FUNCTIONS
You may choose to use one or more of the following modules, imported as follows: 

`from temp4hifu import setParam, calculateBioheat, calculateRayleighIntegral`

`setParam.setMedium(INPUT_ARG)`

`calculateRayleighIntegral.generateField(INPUT_ARG)`

`calculateBioheat.generateVector(INPUT_ARG)`


## GUI COMPONENTS AND FUNCTION NOTES
**The GUI is able to sustain the following actions:**
1) Graph a 2D Pressure Field in cylindrical coordinate space of given transducer and medium properties. 
2) Display the 2D graph as a pressure or an intensity based on a given initial pressure.
3) Graph a 1D Temperature Vector over Time for a given transducer, medium, heating scheme, and FTCS model. 
4) Load premade `.csv` or `.txt` files for graphing and computation of the above.
5) Calls on the three other module functions as listed below:

The function `setParam.setMedium` provides a small list of propagation media to select from as a preset, as well as provides custom input as needed. The export is either a preset dictionary of the properties for Water, Glycerol, Egg White, or Castor Oil, or a custom dictionary of values of the user's choosing.  

The function `calculateRayleighIntegral.generateField` allows the calculation of a pressure field using the Rayleigh Integral in cylindrical coordinate (Z,R) space, and outputs a 2D list of pressure values, a 1D list of Z-axis values, and a 1D list of R-axis values. 

Using the outputs from the first function, the function `calculateBioheat.generateVector` allows for the calculation the temperature based on a heating and cooling scheme for at a specific point in the (Z,R) space, and outputs a 1D list of temperature values and a 1D list of time values. Optionally, this function also exports the 2D list of heat Q, calculated based on the intensity from the pressure field and the parameters given previously.
*Please note that an overflow error may appear in the terminal during the heating component. Unless an error is thrown, please ignore this warning. It will not affect the output calculation.*

## Author's Notes
This package was intended to include addtional components such as different models to calculate pressure (the KZK and Westervelt equations) in the nonlinear space. Accompanying this, there are more complicated bioheat models that would better represent the temperature propagating through the human body. Due to the limited scope of the project, the package was designed for linear use only. 


## RESOURCES
Github Link [https://github.com/C2H5OH-Consumer/temp4hifu]
    
Contains Sample Scripts using Juypter Notebooks:

`sampleScript_loadFunctions.ipynb`

`sampleScript_loadGUI.ipynb`
