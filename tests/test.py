from painterAssistant import paintCanCalculator


def test_number_of_paint_cans_calculated_correctly_1():
    """
    make sure number of paint cans needed is calculated corectly
    """

    assert paintCanCalculator.how_many_needed(5, 5, 5) == 5, \
        'Result for 5x5 wall and 5m^2 paint can efficiency should should be 5!'
