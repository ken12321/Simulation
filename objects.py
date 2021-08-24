from animal_types import Camel
from screen_setup import screen
import pygame

animal_objects = []

class Animal:
    def __init__(self, position):
        self.id = len(animal_objects)
        self.type = Camel()
        self.sprite = self.type.sprite
        self.position = position
        animal_objects.append(self)
    
    def DrawAnimal(self):
        screen.blit(self.sprite, self.position)

    def ActionIdle(self):
        x = self.position[0]
        y = self.position[1]
        x+= 1
        screen.blit(self.sprite, (x + 1, y))
        self.position = (x, y)