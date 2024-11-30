def setTransducer(freq_in, radius_in, focus_in, initPressure_in):
    """
    INPUT ARG
        freq_in == [Hz] Transmit Frequency of transducer
        radius_in == [m] Radius of transducer probe
        focus_in == [m] Focal point in space 
        initPressure_in == [Pa] Initial Pressure output by transducer

    OUTPUT ARG
        trans == dictionary of transducer properties
            "freq" == [Hz] Transmit Frequency of transducer
            "radius" == [m] Radius of transducer probe
            "focus" == [m] Focal point in space 
            "initPressure" == [Pa] Initial Pressure output by transducer
    """
    trans = dict(
        freq = freq_in,
        radius = radius_in,
        focus = focus_in,
        initPressure = initPressure_in,
    )
    return trans