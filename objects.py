from animal_types import Camel
from screen_setup import screen
import pygame

animal_objects = []

class Animal:
    def __init__(self):
        self.id = len(animal_objects)
        self.type = Camel()
        self.sprite = self.type.sprite
        animal_objects.append(self)
    
    def DrawAnimal(self, cursor_position):
        self.position = cursor_position
        screen.blit(self.sprite, cursor_position)

    def ActionIdle(self, positioin):
        screen.blit(self.sprite, position + 1)