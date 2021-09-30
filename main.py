import pygame
from constants import TOTAL_WORLD_SIZE

from events import onEvent, NextAction, CleanupObjects
import world
from world_generation import GenerateWorld


newWorld = world.World(TOTAL_WORLD_SIZE)
GenerateWorld(newWorld)

tick = 0

running = True  # if false, ends game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            onEvent(event, newWorld)

    tick += 1
    if tick % 10 == 0:
        # decides next action
        NextAction(tick, newWorld)
        # cleans up unused entities
        CleanupObjects()         

    GenerateWorld(newWorld)
    # updates the screen
    pygame.display.update()
