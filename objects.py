from animal_types import Camel
from food_types import Apple
from screen_setup import screen
import pygame
from math import sqrt
import random

animal_objects = []

food_objects = []

class Animal:
    def __init__(self, position):
        self.id = len(animal_objects)
        self.type = Camel()
        self.speed = random.randint(self.type.minspeed, self.type.maxspeed)
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


    def ActionWalkToPosition(self, endposition):
        x = self.position[0]
        y = self.position[1]

        ex = endposition[0]
        ey = endposition[1]

        x_distance = ex - x
        y_distance = ey - y

        moveamount = 5

        if x_distance != 0:
            if abs(0 < x_distance < 5):
                moveamount = x_distance
            if x_distance > 0:
                x += moveamount
                self.direction = "east"
            else:
                x -= moveamount
                self.direction = "west"

        if y_distance != 0:
            if abs(0 < y_distance < 5):
                moveamount = y_distance
            if y_distance > 0:
                y += moveamount
            else:
                y -= moveamount
        
        self.position = (x, y)


    def ActionIdle(self, moveamount):
        x = self.position[0]
        y = self.position[1]

        idle_y_actions = ["north", "south", "none", "none"]
        idle_x_actions = ["east", "west", "none", "none"]
        action_y = random.choice(idle_y_actions)
        action_x = random.choice(idle_x_actions)
        if action_x != "none":
            self.direction = action_x
        
        if action_y == "north":
            y += moveamount
        elif action_y == "south":
            y -= moveamount
        if action_x == "east":
            x += moveamount
        elif action_x == "west":
            x -= moveamount

        self.position = (x, y)

        if self.direction == "east":
            screen.blit(self.sprite_east, self.position)
        else:
            screen.blit(self.sprite_west, self.position)


    def ActionSeekFood(self):
        food_distance = []
        food_id = []
        for food in food_objects:
            if self.position == food.position:
                food_objects.remove(food)
            distance = sqrt((food.position[0] - self.position[0]) ** 2 * abs(food.position[1] - self.position[1]) ** 2) 
            food_distance.append(distance)
            food_id.append(food)

        closest_food_distance = min(food_distance)
        index = food_distance.index(closest_food_distance)
        closest_food = food_id[index]

        self.ActionWalkToPosition(closest_food.position)


class Food:
    def __init__(self, position, type):
            self.id = len(food_objects)
            self.type = type
            self.sprite = self.type.sprite
            self.position = position
            food_objects.append(self)
        
    def DrawFood(self):
        screen.blit(self.sprite, self.position)