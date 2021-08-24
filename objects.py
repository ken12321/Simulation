from animal_types import Camel
from screen_setup import object_surface, screen
import pygame

class Animal:
    def __init__(self):
        self.type = Camel()
        self.sprite = self.type.sprite
    
    def DrawAnimal(self, position):
        object_surface.blit(self.sprite, position)