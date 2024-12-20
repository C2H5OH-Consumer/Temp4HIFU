
# COMPONENT SPECIFICATIONS

Last Updated 12/05/2024 by Gerald Lee

## Imported Python Packages

### numpy
Used as a base for Pandas and computational functions listed below (calculateRayleighIntegral.py and calculateBioheat.py)

### pandas
Used to load .CSV or .TXT files into the GUI. Used to write .CSV file output from GUI. 
Used by Dash to load data frames for 2D plotting.  
Data frames have no headers. 

### dash
startApp.py
    - Provides Graphical User Interface (GUI)
        - User interface to mouse over a point of interest on the pressure field.
        - User interface to mouse over a point of interest on temperature graph.
        - Allows change of variables through inputs and dropdown menus
        - Graphs figures using Plotly express and graph-objects
        - Provides callbacks to initiate large functions and calculations

Dash provides a link to an online web based GUI service run from the machine. This, however, freezes the terminal. 
CTRL+C kills the command, but once the script stops running then the webpage will also fail to return any callbacks called after killing the app. 
Use instructions include to 1. open the link and 2. when ready to kill app, kill app in terminal.


## Added Python Modules and Functions

#### [This function returns a preset dictionary or combines values into a custom set dictionary.]

setParam
    .setMedium
        INPUT ARG
            index == [str] text to call specific preset dictionary
            speed_in == [float][m/s] Speed of Sound
            density_in == [float][kg/m^3] Density 
            absCoeff_in == [float][Np/(m*MHz^2)] Absorption Coefficient
            specHeatCap_in == [float][J/(kg*K)] Specific Heat Capacity
            thermDiff_in == [float][(m^2)/s] Thermal Diffusivity 

        OUTPUT ARG
            medium == [dict] dictionary of medium properties
                "name" == [str] Identifying Name for Preset Dictionaries 
                "speed" == [float][m/s] Speed of Sound
                "density" == [float][kg/m^3] Density 
                "absCoeff" == [float][Np/(m*MHz^2)] Absorption Coefficient
                "specHeatCap" == [float][J/(kg*K)] Specific Heat Capacity
                "thermDiff" == [float][(m^2)/s] Thermal Diffusivity 

Output arguments are used in the GUI for the dropdown menu and as a preset for input into the below functions. 
Users may call this function to load in preset medium properties. 


#### [This function outputs a pressure field and its respective axes based on the given inputs.]

calculateRayleighIntegral
    .generateField
        INPUT ARG
            trans == [dict] dictionary of transducer properties
                "freq" == [float][Hz] Transmit Frequency of transducer
                "radius" == [float][m] Radius of transducer probe
                "focus" == [float][m] Focal point in space 
                "initPressure" == [float][Pa] Initial Pressure output by transducer

            medium == [dict] dictionary of medium properties
                "speed" == [float][m/s] Speed of Sound
                "density" == [float][kg/m^3] Density 
                "absCoeff" == [float][Np/(m*MHz^2)] Absorption Coefficient

            field == [dict] 2D field parameters
                "numAxialStep" == [int] Number of Axial Steps
                "numRadialStep" == [int] Number of Radial Steps

        OUTPUT ARG
            pressure_field == [2D list][p/p0] Resulting Rayleigh Integral Pressure Field
            z_axis == [1D list][m] Axial axis of Pressure Field
            r_axis == [1D list][m] Radial axis of Pressure Field 

Output arguments are lists that get converted into a .CSV using the pandas package. 
The GUI then reads these .CSV files to create the 2D plot and to input into calculateBioheat.generateVector. 
This also allows the user to manipulate the 2D plot without having to run the rayleigh integral. 
Created files are saved to the directory in which the session of Python is being run. 


#### [This function outputs a temperature vector and its respective time axis based on the given inputs.]

calculateBioheat
    .generateVector
        INPUT ARG
            axial_loc == [float][m] Coordinate Z of Interest Location
            radial_loc == [float][m] Coordinate R of Interest Location

            trans == [dict] dictionary of transducer properties
                "freq" == [float][Hz] Transmit Frequency of transducer
                "radius" == [float][m] Radius of transducer probe
                "focus" == [float][m] Focal point in space 
                "initPressure" == [float][Pa] Initial Pressure output by transducer

            medium == [dict] dictionary of medium properties
                "speed" == [float][m/s] Speed of Sound
                "density" == [float][kg/m^3] Density 
                "absCoeff" == [float][Np/(m*MHz^2)] Absorption Coefficient
                "specHeatCap" == [float][J/(kg*K)] Specific Heat Capacity
                "thermDiff" == [float][(m^2)/s] Thermal Diffusivity 

            heat == [dict] dictionary of heating parameters
                "numTime" == [float][s] Time Step aka Delta Time
                "HeatTime" == [int][s] Amount of Time for Heating
                "CoolTime" == [int][s] Amount of Time for Cooling
                "DutyCycle" == [int][%] Ratio of On vs Off Time during Heating

            pressure2D == [2D list][p/p0] Rayleigh Integral Pressure Field
            z_values == [1D list][m] Axial axis of Pressure Field
            r_values == [1D list][m] Radial axis of Pressure Field 
        
        OUTPUT ARG
            time_axis == [1D list][s] Time Axis
            temp_vec == [1D list][Celsius] Temperature Vector over Time
            Q == [2D list][Joules] Heat Map 

Output arguments are not saved as .CSV file. 
Instead, the GUI returns a figure plot using the output lists. 
This displays the temperature at a specific location in space, allowing the user to identify the approximate temperature being output by the given parameters. 


## Tentative Project Plan

- Week 6 (11/04/2024 - 11/08/2024)
    Planning Initial Plan for Functions, Inputs, Outputs

- Week 7 (11/11/2024 - 11/15/2024)
    Explore the use of Dash for GUI
    GUI draft and core functions completed
        - Locations to input parameters
            - Heating Pulse Regime
            - Transducer Properties
            - Medium Properties
        - Locations to mouse over data
            - 2D map
            - 1D graph

- Week 8 (11/18/2024 - 11/22/2024)
    Create functions
        - Popup Boxes
        - Bioheat Equation
        - Temperature Compliance
        - Acoustic Intensity

- Week 9 (11/25/2024 - 11/29/2024)
    Bug Fixes
    Finalize Presentation

- Week 10 (12/02/2024 - 12/06/2024)
    Package Preparation
    Present Work


## Future Work 

No future work is intended to be applied to this package. However, additional modules regarding nonlinear physics and heat transfer can be created and easily added to this package to support more comprehensive HIFU-Bioheat models. 