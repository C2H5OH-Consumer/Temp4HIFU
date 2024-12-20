# Functional Specifications

Last Updated 12/05/2024 by Gerald Lee

## Introduction

High Intensity Focused Ultrasound (HIFU) and Focused Ultrasound (FUS) are used for thermal treatment of cells such as for cancer treatment. 
The generated increase of temperature during HIFU thermal treatment must be within safety guidelines for human use (44 degrees Celsius), which is essential for FDA approval and compliance.
Accurate predictions of temperature bioeffects must be demonstrated through computational simulations before applications ex vivo and in vivo. 
Computational simulations requires modeling for both HIFU/FUS pressure fields and then the Bioheat equation; not complicated individually, but when combined can be tricky to navigate based on initial conditions.

This package serves to act as a quick and dirty program to easily estimate temperature compliance given the design of the therapy and the properties of the medium. 

Provided is a Graphical User Interface (GUI) based in Dash and Plotly (startApp.py) as well as three functions able to be used independently of the application:
    1 = The Rayleigh Integral (calculateRayleighIntegral.generateField)
        Necessary to calculate pressure fields, based on a cylindrical axis system (Z,R) [m]. 
        Assumes linear propagation, radial symmetry, and no scattering effects. 
    2 = The Bioheat Equation: (calculateBioheat.generateVector)
        A Forward Time Centered Space finite element scheme to solve Penne's Bioheat Equation. 
        Identifies temperature change over one location in (Z,R) [m] space for a given heat and cool time. 
        Assumes linear propagation, instantaneous heat transfer, and ignores blood perfusion and porous attributes of the medium.
        CAUTION: prone to numerical instability if time step is too large. Recommended time step == 5e-3 [s].
    3 = A set of preset medium properties (setParam.setMedium) is also provided. Presets include Water, Glycerol, Egg White, and Castor Oil. 

The most basic use cases for the above functions includes identifing pressure and intensity output based on a given initial pressure, calculate and graph a pressure field, observe temperature over time for a given location in (Z,R) [m] space, and load in pre-calculated .CSV files to observe the same thing. 
Ideal use cases can be expanded to testing transducer designs in the linear regime, observe if temperature at point of interest is within FDA compliance for medical human tissue temperature increase, and as a learning tool. 

The package is designed for users with some knowledge of therapeutic ultrasound design; however, this tool provides a unique entry point to learning about bioheat and ultrasound therapeutics in general. 
The GUI provides users a clean interface to visualize the important condition specifications required to perform therapeutic ultrasound and introduce the complexity of its experimental design. 
Its ability to load pre-calculated data also allows researchers to input their own data for visualization and calculation of bioheat at a specific location in (Z,R) [m] space. 
Users that do not have access to MATLAB or COMSOL would be able to take advantage of this package to begin exploring therapeutic ultrasound design structures in Python instead of spending excessively for a computational program (although suggested to get MATLAB or COMSOL for more complex applications).


## Intended Users 
    1. Persons who have some knowledge of therapeutic ultrasound.
    2. Persons who would prefer to use Python for the above use cases specified above.
    3. Persons who would prefer a GUI layout for the above use cases specified above. 
    4. Persons who want a visual introduction to the required parameters that are involved in bioheat calculations.


## Specific Information Supported
    - Pressure Fields in cylindrical coordinate systems (Z,R) relative to a given initial pressure. 
    - Temperature generated over heating and cooling scheme at a single point in space (Z,R).
    - How the pressure field changes given different transducer and medium parameters.
    - How the temperature at a location in space (Z,R) changes given different heating and cooling schemes
    - How the pressure output by HIFU and the generated bioheat are related in a linear model.  


## Presented Use Cases
    - To use the linear Rayleigh Integral for an axisymetric HIFU transducer design. 
    - To use the linear 1D Pennes' Bioheat Equation solved using a FTCS finite element scheme.
    - To approximate temperature output based on the above calculations at a specific location.
    - Visualize the bioheat components easily and simply in an online web browser. 


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