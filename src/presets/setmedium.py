def setMedium(index, inputs):
    """
    INPUT ARG
        index == calls specific dictionary
        inputs == for custom dictionary

    OUTPUT ARG
        mediumProp == dictionary of medium properties
            mediumProp.name == string
            mediumProp.speed == [m/s]
            mediumProp.density == [kg/m^3]
            mediumProp.absCoeff == [Np/(m*MHz^2)]
            mediumProp.specHeatCap == [J/(kg*K)]
            mediumProp.thermDiff == [(m^2)/s]
    """

    match index:

        case 'Water':
            mediumProp = dict(
                name = 'Water',
                speed = 1500,
                density = 1000,
                absCoeff = 0.025,
                specHeatCap = 4180,
                thermDiff = 1.46 * 1e-7,
            )
            return mediumProp
        
        
        case 'Glycerol':
            mediumProp = dict(
                name = 'Glycerol',
                speed = 1920,
                density = 1264,
                absCoeff = 3.6,
                specHeatCap = 2407,
                thermDiff = 0.95 * 1e-7,
            )
            return mediumProp
        
        
        case 'Egg White':
            mediumProp = dict(
                name = 'Egg White',
                speed = 1546,
                density = 1045,
                absCoeff = 3.5,
                specHeatCap = 4270,
                thermDiff = 1.32 * 1e-7,
            )
            return mediumProp
            
        
        case 'Castor Oil':
            mediumProp = dict(
                name = 'Castor Oil',
                speed = 1500,
                density = 960,
                absCoeff = 6,
                specHeatCap = 1800,
                thermDiff = 1.05 * 1e-7,
            )
            return mediumProp
         

        case 'Custom':
            mediumProp = dict(
                name = 'Custom',
                speed = inputs.speed,
                density = inputs.density,
                absCoeff = inputs.absCoeff,
                specHeatCap = inputs.specHeatCap,
                thermDiff = inputs.thermDiff,
            )
            return mediumProp
        
        case _:
            print('ERROR: medium.py')

