from screen_setup import screen, background, xSize, ySize
import pygame
import constants

# max rooms in x and y
TOTAL_FLOOR_LENGTH = 10

xScreenScaling = xSize / TOTAL_FLOOR_LENGTH
yScreenScaling = ySize / TOTAL_FLOOR_LENGTH


def DrawSquare(tile):
    x = tile.x * xScreenScaling
    y = tile.y * yScreenScaling
    tile_type = tile.type
    print(tile_type)
    pygame.draw.rect(screen, (tile_type.color), (x, y, xScreenScaling, yScreenScaling))
    #pygame.draw.rect(screen, (constants.GUNMETAL), (x, y, xScreenScaling, yScreenScaling), 1)


def DrawRooms(world):
    world_tile_array = world.tile_array
    for tile in world_tile_array:
        DrawSquare(tile)


def GenerateWorld(world):
    DrawRooms(world)