import math

def how_many_needed(width, height, canEfficiency):
    """Calculate number of paint cans needed to paint the wall of given dimensions.

    Keyword arguments:
    width -- wall width in meters
    height -- wall height in meters
    canEfficiency -- how many m^2 of wall can be painted with one wall

    """

    return math.ceil(width*height / canEfficiency)

