def setTransducer(freq_input, radius_input, focus_input, initPressure_input):
    """
    INPUT ARG
        frequency = [MHz]
        radius = [mm]
        focus = [m]
        initPressure = [Pa]

    OUTPUT ARG
        transducer == dictionary of transducer properties
            
    """
    transducer = dict(
        freq = freq_input,
        radius = radius_input,
        focus = focus_input,
        initPressure = initPressure_input,
    )
    return transducer