import math


class PaintCanNeededCalculator:

    def __init__(self):
        self.minExcess = 0.0
        self.efficiency = None

    def set_min_excess(self, min_excess):
        self.minExcess = min_excess

    def set_paint_can_efficiency(self, efficiency):
        self.efficiency = efficiency

    def calculate(self, room):
        if self.efficiency is None:
            raise ValueError('Paint can efficiency wasn\'t set before calling calculate method')

        exact_need = room.surface / self.efficiency
        ceiled_need = math.ceil(exact_need)
        actual_excess = exact_need/ceiled_need

        while actual_excess < self.minExcess:
            ceiled_need = ceiled_need + 1
            actual_excess = exact_need/ceiled_need

        return ceiled_need, actual_excess

