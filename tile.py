from constants import XSCREENSCALING, YSCREENSCALING
from world_generation import DrawSquare
from tile_types import Sand, Water, Grass

class Tile:
    def __init__(self, position):
        # The position of the tile in relation to other tiles
        self.position = position
        self.x = position[0]
        self.y = position[1]
        
        # The coordinates of the tile in the world
        self.real_x = self.x * XSCREENSCALING
        self.real_y = self.y * YSCREENSCALING
        self.real_position = (self.real_x, self.real_y)
        # The maximum value that the tile occupies in the world
        self.real_max_x = self.real_x + XSCREENSCALING
        self.real_max_y = self.real_y + YSCREENSCALING

        self.type = Grass()

    def ChangeType(self, new_type):
        self.type = new_type
        DrawSquare(self)


