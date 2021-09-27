import pygame
from world_generation import DrawSquare, xScreenScaling, yScreenScaling
from tile_types import *
from screen_setup import screen, xSize, ySize

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

    elif key == pygame.K_k:
        mouse_position = pygame.mouse.get_pos()
        corrected_mouse_position = (mouse_position[0] - 10, mouse_position[1] - 10)
        apple = Food(corrected_mouse_position, Apple())

def GetTileAtMousePosition(mouse_position, world):
    mouseX = mouse_position[0]
    mouseY = mouse_position[1]

    for tile in world.tile_array:
        tile_x = tile.x * xScreenScaling
        tile_y = tile.y * yScreenScaling
        if tile_y <= mouseY <= tile_y + yScreenScaling:  # if the room has the same coords as the mouse click
            if tile_x <= mouseX <= tile_x + xScreenScaling:
                return tile

def NextAction(frame, world):
    for animal in animal_objects:
        animal.PassiveStats()
        if animal.thirst <= 60:
            animal.ActionSeekWater(world)
        elif len(food_objects) > 0 and animal.hunger <= 60:
            animal.ActionSeekFood()
        else:
            animal.ActionIdle(animal.speed)

def CleanupObjects():
    for animal in animal_objects:
        xCheck = animal.position[0] < 0 or animal.position[0] > xSize
        yCheck = animal.position[1] < 0 or animal.position[1] > ySize
        if (xCheck or yCheck):
            animal.position = (round(xSize/2), round(ySize/2))
