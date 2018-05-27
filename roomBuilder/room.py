
class Room:
    def __init__(self, surface):
        self._surface = surface

    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, surface):
        self._surface = surface


class RoomBuilder:

    def __init__(self):
        self.current_total_surface = 0.0

    def add_wall(self, width, height):
        self.current_total_surface += width * height

    def build(self):
        return Room(self.current_total_surface)
