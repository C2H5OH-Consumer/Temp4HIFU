def generateField(trans,medium,field):
    """
    INPUT ARG
        trans == dictionary of transducer properties
            "freq" = [Hz]
            "radius" = [m]
            "focus" = [m]
            "initPressure" = [Pa]
        medium == calls medium properties
            "speed" = [m/s]
            "density" = [kg/m^3]
            "absCoeff" = [Np/(m*MHz^2)]
        field == calls 2D field properties
            "numAxialStep"
            "numRadialStep"

    OUTPUT ARG
        pressure_field == resulting rayleigh integral pressure field


    """
    import numpy as np

    # Edit and Transform Transducer Properties
    d = trans["focus"]
    k = 2 * np.pi * trans["freq"] / medium["speed"] # Wave Number
    angularF = trans["radius"]/trans["focus"] # Angular Frequency
    abs_Coeff = medium["absCoeff"] * (pow((trans["freq"]/(1e6)),2)) # POWER LAW
    # impedance = medium["speed"]/medium["density"]
    # gain = 2 * np.pi * trans["freq"] * ((trans["radius"])^2) / (2*trans["focus"]*medium["speed"])


    # Set Axes
    axial_min = 0.001
    axial_max = 2*d
    radial_min = -trans["radius"]
    dz = (axial_max - axial_min) / field["numAxialStep"]
    numZ = np.round((axial_max - axial_min)/dz)+1
    dr = -1 * radial_min / (field["numRadialStep"]/2)
    numR = np.round((0 - radial_min)/dz)+1
    # Theta Component
    thetaMax = np.arcsin(angularF)
    numT = 100
    dtheta = thetaMax/numT


    # Preallocation
    z_values = np.zeros((numZ,1))
    r_values = np.zeros((numR,1))
    pressure_field = np.zeros((numZ,numR))

    # Rayleigh Integral
    z = axial_min
    for zz in range(0,numZ-1):
        r = radial_min
        for rr in range(0,numR-1):
            p = 0.5 * np.exp(1j * k * np.sqrt(z*z + r*r)) / np.sqrt(z*z + r*r) * dtheta
            for tt in range(1,numT-1):
                theta = tt * dtheta
                numP = (2*tt+1)
                dphi = (2*np.pi)/numP
                e1 = 0
                for pp in range(0,len(numP)-1):
                    phi = dphi * pp
                    rf = np.sqrt((pow((d*np.sin(theta)),2))+r*r-2*np.sin(theta)*np.abs(r)*d*np.cos(phi)+pow((z-d+d*np.cos(theta)),2))
                    # rf = np.sqrt(((d*np.sin(theta))^2)+r*r-2*np.sin(theta)*np.abs(r)*d*np.cos(phi)+(z-d+d*np.cos(theta))^2)
                    e1 = e1 + np.exp(1j*k*rf)/rf
                p = p + e1*np.sin(theta)/(2*tt+1)
            amplitude = abs(p)*k*d*d*dtheta*np.exp(-abs_Coeff*(z-axial_min))
            pressure_field[-(zz+1)][-(rr+1)] = amplitude
            r_values[-(rr+1)] = r
            r = r + dr
        z_values[-(zz+1)] = z
        z = z + dz 
    
    # Radial Symmetry (reflect pressure values across z-axis)
    for ii in range(1,numZ):
        for jj in range(1,numR):
            if jj != numR:
                r_values[-(2*numR-jj)] = np.abs(r_values[-jj])
                pressure_field[-ii][-(2*numR-jj)] = pressure_field[-ii][-jj]

    # Fix Dividing by 0 at the first center point
    r_CenterIdx = round((-1*radial_min/dr)+1)
    pressure_field[-1][-r_CenterIdx] = 0


    return pressure_field, z_values, r_values