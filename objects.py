from animal_types import Camel
from screen_setup import screen
import pygame
import random

animal_objects = []

class Animal:
    def __init__(self, position):
        self.id = len(animal_objects)
        self.type = Camel()
        self.sprite_east = self.type.sprite_east
        self.sprite_west = self.type.sprite_west
        self.position = position
        self.direction = "west"
        animal_objects.append(self)
    
    def DrawAnimal(self):
        if self.direction == "east":
            screen.blit(self.sprite_east, self.position)
        else:
            screen.blit(self.sprite_west, self.position)

    def ActionIdle(self):
        x = self.position[0]
        y = self.position[1]

        idle_y_actions = ["north", "south", "none", "none"]
        idle_x_actions = ["east", "west", "none", "none"]
        action_y = random.choice(idle_y_actions)
        action_x = random.choice(idle_x_actions)
        if action_x != "none":
            self.direction = action_x
        
        if action_y == "north":
            y += 5
        elif action_y == "south":
            y -= 5
        if action_x == "east":
            x += 5
        elif action_x == "west":
            x -= 5

        self.position = (x, y)

        if self.direction == "east":
            screen.blit(self.sprite_east, self.position)
        else:
            screen.blit(self.sprite_west, self.position)