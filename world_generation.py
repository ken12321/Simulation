from screen_setup import screen, background, xSize, ySize
from objects import animal_objects
import pygame
import constants

# max tilesin x and y
TOTAL_WORLD_SIZE = 10

xScreenScaling = xSize / TOTAL_WORLD_SIZE
yScreenScaling = ySize / TOTAL_WORLD_SIZE


def DrawSquare(tile):
    x = tile.x * xScreenScaling
    y = tile.y * yScreenScaling
    tile_type = tile.type
    pygame.draw.rect(screen, (tile_type.color), (x, y, xScreenScaling, yScreenScaling))


def DrawTiles(world):
    world_tile_array = world.tile_array
    for tile in world_tile_array:
        DrawSquare(tile)

def DrawObjects():
    if len(animal_objects) > 0:
        for animal in animal_objects:
            animal.DrawAnimal()

def GenerateWorld(world):
    DrawTiles(world)
    DrawObjects()