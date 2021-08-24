import constants
from world_generation import DrawSquare
from tile_types import Sand, Water

class Tile:
    def __init__(self, position):
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.type = Sand()


    def ChangeType(self, new_type):
        self.type = new_type
        # print("tile at coords {coords} has been changed to type {type}".format(coords = self.position, type = new_type))
        DrawSquare(self)


