import pygame
from world_generation import DrawSquare
from tile_types import *
from screen_setup import screen
from constants import TOTAL_WORLD_SIZE, XSIZE, YSIZE, XSCREENSCALING, YSCREENSCALING

from objects import *


def onEvent(event, world):
        if event.type == pygame.KEYDOWN:
            OnKeyboardPress(event.key, world)

def OnKeyboardPress(key, world):
    if key == pygame.K_w:
        mouse_position = pygame.mouse.get_pos()
        selected_tile = GetTileAtMousePosition(mouse_position, world)
        selected_tile.ChangeType(Water())

        # changes tiles around water tiles to be sand

        north_coords = [selected_tile.x, selected_tile.y + 1]
        south_coords = [selected_tile.x, selected_tile.y - 1]
        east_coords = [selected_tile.x + 1, selected_tile.y]
        west_coords = [selected_tile.x - 1, selected_tile.y]

        northeast_coords = [selected_tile.x + 1, selected_tile.y + 1]
        northwest_coords = [selected_tile.x - 1, selected_tile.y + 1]
        southeast_coords = [selected_tile.x + 1, selected_tile.y - 1]
        southwest_coords = [selected_tile.x - 1, selected_tile.y - 1]

        surrounding_coords = [north_coords, south_coords, east_coords, west_coords,
                            northeast_coords, northwest_coords, southeast_coords, southwest_coords]
        surrounding_tiles = []

        for coords in surrounding_coords:
            if not OutOfBoundsTileCheck(coords):
                tile = world.TileAt(coords)
                surrounding_tiles.append(tile)

        deep_water_flag = True
        for tile in surrounding_tiles:
            if tile.type.name != constants.WATER and tile.type.name != constants.DEEP_WATER:
                deep_water_flag = False
                tile.ChangeType(Sand())

        if deep_water_flag:
            selected_tile.ChangeType(DeepWater())


    elif key == pygame.K_s:
        mouse_position = pygame.mouse.get_pos()
        selected_tile = GetTileAtMousePosition(mouse_position, world)
        selected_tile.ChangeType(Sand())

    elif key == pygame.K_g:
        mouse_position = pygame.mouse.get_pos()
        selected_tile = GetTileAtMousePosition(mouse_position, world)
        selected_tile.ChangeType(Grass())
    
    elif key == pygame.K_c:
        mouse_position = pygame.mouse.get_pos()
        corrected_mouse_position = (mouse_position[0] - 15, mouse_position[1] - 15)
        camel = Animal(corrected_mouse_position, Camel())

    elif key == pygame.K_l:
        mouse_position = pygame.mouse.get_pos()
        corrected_mouse_position = (mouse_position[0] - 15, mouse_position[1] - 15)
        leopard = Animal(corrected_mouse_position, Leopard())

    elif key == pygame.K_k:
        mouse_position = pygame.mouse.get_pos()
        corrected_mouse_position = (mouse_position[0] - 10, mouse_position[1] - 10)
        apple = Food(corrected_mouse_position, Apple())
    
    elif key == pygame.K_m:
        mouse_position = pygame.mouse.get_pos()
        corrected_mouse_position = (mouse_position[0] - 10, mouse_position[1] - 10)
        tree = Entity(corrected_mouse_position, Tree(Apple()))

def GetTileAtMousePosition(mouse_position, world):
    mouseX = mouse_position[0]
    mouseY = mouse_position[1]

    for tile in world.tile_array:
        tile_x = tile.x * XSCREENSCALING
        tile_y = tile.y * YSCREENSCALING
        if tile_y <= mouseY <= tile_y + YSCREENSCALING:  # if the tile has the same coords as the mouse
            if tile_x <= mouseX <= tile_x + XSCREENSCALING:
                return tile

def NextAction(tick, world):
    for animal in animal_objects:
        animal.PassiveStats(tick)
        if len(world.water_tile_array) > 0 and animal.thirst <= round(animal.max_thirst * 0.6):
            animal.ActionSeekWater(world)
        elif len(food_objects) > 0 and animal.hunger <= round(animal.max_hunger * 0.6):
            animal.ActionSeekFood()
        elif animal.breed_ready:
            animal.ActionSeekMate(tick)
        else:
            animal.ActionIdle(animal.speed)

def CleanupObjects():
    # right now, just brings any animals outside of screen into the center of the screen
    for animal in animal_objects:
        xCheck = animal.position[0] < 0 or animal.position[0] > TOTAL_WORLD_SIZE
        yCheck = animal.position[1] < 0 or animal.position[1] > TOTAL_WORLD_SIZE
        if (xCheck or yCheck):
            animal.position = (round(XSIZE/2), round(YSIZE/2))

def OutOfBoundsTileCheck(coords):
    x_check = coords[0] < 0 or coords[0] >= TOTAL_WORLD_SIZE
    y_check = coords[1] < 0 or coords[1] >= TOTAL_WORLD_SIZE
    if (x_check or y_check):
        return True
    else:
        return False
