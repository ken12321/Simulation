from animal_types import Camel
from screen_setup import screen
import pygame

class Animal:
    def __init__(self):
        self.type = Camel()
        self.sprite = self.type.sprite
    
    def DrawAnimal(self, position):
        screen.blit(self.sprite, position)