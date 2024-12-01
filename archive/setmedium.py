def setMedium(index:str,inputs:dict):
    """
    INPUT ARG
        index == [str] text to call specific preset dictionary
        inputs == [dict] for custom set dictionary

    OUTPUT ARG
        medium == [dict] dictionary of medium properties
            "name" == [str] Identifying Name for Preset Dictionaries 
            "speed" == [m/s] Speed of Sound
            "density" == [kg/m^3] Density 
            "absCoeff" == [Np/(m*MHz^2)] Absorption Coefficient
            "specHeatCap" == [J/(kg*K)] Specific Heat Capacity
            "thermDiff" == [(m^2)/s] Thermal Diffusivity 
    """
    match index:

        case 'Water':
            medium = dict(
                name = 'Water',
                speed = 1500,
                density = 1000,
                absCoeff = 0.025,
                specHeatCap = 4180,
                thermDiff = 1.46 * 1e-7,
            )
            return medium
        
        
        case 'Glycerol':
            medium = dict(
                name = 'Glycerol',
                speed = 1920,
                density = 1264,
                absCoeff = 3.6,
                specHeatCap = 2407,
                thermDiff = 0.95 * 1e-7,
            )
            return medium
        
        
        case 'Egg White':
            medium = dict(
                name = 'Egg White',
                speed = 1546,
                density = 1045,
                absCoeff = 3.5,
                specHeatCap = 4270,
                thermDiff = 1.32 * 1e-7,
            )
            return medium
            
        
        case 'Castor Oil':
            medium = dict(
                name = 'Castor Oil',
                speed = 1500,
                density = 960,
                absCoeff = 6,
                specHeatCap = 1800,
                thermDiff = 1.05 * 1e-7,
            )
            return medium
         

        case 'Custom':
            medium = dict(
                name = 'Custom',
                speed = inputs['speed'],
                density = inputs['density'],
                absCoeff = inputs['absCoeff'],
                specHeatCap = inputs['specHeatCap'],
                thermDiff = inputs['thermDiff'],
            )
            return medium