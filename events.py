import pygame
from world_generation import DrawSquare
from tile_types import *
from screen_setup import screen
from constants import XSIZE, YSIZE, XSCREENSCALING, YSCREENSCALING

from objects import *


def onEvent(event, world):
        if event.type == pygame.KEYDOWN:
            OnKeyboardPress(event.key, world)

def OnKeyboardPress(key, world):
    if key == pygame.K_w:
        mouse_position = pygame.mouse.get_pos()
        selected_tile = GetTileAtMousePosition(mouse_position, world)
        selected_tile.ChangeType(Water())

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
        #elif animal.hunger <= round(animal.max_hunger * 0.9) and animal.thirst <= round(animal.max_thirst * 0.9) and animal.age >= animal.max_age / 10:
        #    animal.ActionSeekMate()
        else:
            animal.ActionIdle(animal.speed)

def CleanupObjects():
    # right now, just brings any animals outside of screen into the center of the screen
    for animal in animal_objects:
        xCheck = animal.position[0] < 0 or animal.position[0] > XSIZE
        yCheck = animal.position[1] < 0 or animal.position[1] > YSIZE
        if (xCheck or yCheck):
            animal.position = (round(XSIZE/2), round(YSIZE/2))
