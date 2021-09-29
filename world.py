import constants
import tile

class World:
    def __init__(self, size):
        self.size = size
        self.tile_array = self.InitTileArray()
        self.water_tile_array = []

    def InitTileArray(self):
        # Initializes the world's tiles
        world = []
        for r in range(self.size):
            for c in range(self.size):
                coords = [c, r]
                world.append(tile.Tile(coords))
        return world

    def TileAt(self, coords):
        for tile in self.tile_array:
            if tile.position == coords:
                return tile
        else:
            return None

    def AddToWaterTileArray(self, tile):
        if not tile in self.water_tile_array:
            self.water_tile_array.append(tile)
