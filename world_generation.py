from screen_setup import screen, background
from objects import animal_objects, food_objects, entity_objects
from tile_types import Water
import pygame
from constants import WATER, XSIZE, YSIZE, TOTAL_WORLD_SIZE, XSCREENSCALING, YSCREENSCALING


def DrawSquare(tile):
    x = tile.x * XSCREENSCALING
    y = tile.y * YSCREENSCALING
    tile_type = tile.type
    pygame.draw.rect(screen, (tile_type.color), (x, y, XSCREENSCALING, YSCREENSCALING))


def LoopTiles(world):
    world_tile_array = world.tile_array
    for tile in world_tile_array:
        DrawSquare(tile)
        if tile.type.name == WATER:
            world.AddToWaterTileArray(tile)


def DrawObjects():
    if len(entity_objects) > 0:
        for entity in entity_objects:
            entity.DrawEntity()
    if len(food_objects) > 0:
        for food in food_objects:
            food.DrawFood()
    if len(animal_objects) > 0:
        for animal in animal_objects:
            animal.DrawAnimal()

def GenerateWorld(world):
    LoopTiles(world)
    DrawObjects()