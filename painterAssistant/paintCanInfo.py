class PaintCanInfo:
    def __init__(self, efficiency):
        self._efficiency = efficiency

    @property
    def efficiency(self):
        return self._efficiency

    @efficiency.setter
    def efficiency(self, efficiency):
        self._efficiency = efficiency

