import pygame

import constants

from events import onEvent
import world
from world_generation import GenerateWorld

newWorld = world.World(10)
GenerateWorld(newWorld)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            onEvent(event, newWorld)
                

    GenerateWorld(newWorld)
    # updates the screen
    pygame.display.update()
