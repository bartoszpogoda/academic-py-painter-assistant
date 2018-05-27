import math

def how_many_needed(width, height, paintCanInfo):
    """Calculate number of paint cans needed to paint the wall of given dimensions.

    Keyword arguments:
    width -- wall width in meters
    height -- wall height in meters
    paintCanInfo -- PaintCanInfo object describing paint can

    """

    return math.ceil(width*height / paintCanInfo.efficiency)

