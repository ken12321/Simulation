import pygame

import constants

from events import onEvent, NextAction, CleanupObjects
import world
from world_generation import GenerateWorld


newWorld = world.World(10)
GenerateWorld(newWorld)

frame = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            onEvent(event, newWorld)

    # camels will idle animation every 10 ticks
    frame += 1
    if frame % 10 == 0:
        NextAction(frame)
        CleanupObjects()         

    GenerateWorld(newWorld)
    # updates the screen
    pygame.display.update()
