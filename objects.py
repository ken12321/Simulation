from animal_types import Camel, Leopard
from entity_types import Excrement, DeadBody, Tree
from food_types import Apple
from screen_setup import screen
import pygame
from math import dist, sqrt
import random

import constants

from tile_types import Water

animal_objects = []

entity_objects = []

food_objects = []

class Animal:
    def __init__(self, position, type):
        self.id = len(animal_objects)
        self.type = type
        self.max_hunger = self.type.max_hunger
        self.max_thirst = self.type.max_thirst
        self.sprite_east = self.type.sprite_east
        self.sprite_west = self.type.sprite_west
        self.dead_sprite_east = self.type.dead_sprite_east
        self.dead_sprite_west = self.type.dead_sprite_west
        self.speed = random.randint(self.type.minspeed, self.type.maxspeed)
        self.hunger = self.max_hunger
        self.thirst = self.max_thirst
        self.max_age = self.type.max_age
        self.age = 0
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

        moveamount = self.speed

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
                self.hunger = self.max_hunger

            distance = sqrt( (self.position[0] - food.position[0]) ** 2 * (self.position[1] - food.position[1]) ** 2 ) 
            food_distance.append(distance)
            food_id.append(food)

        closest_food_distance = min(food_distance)
        index = food_distance.index(closest_food_distance)
        closest_food = food_id[index]

        self.ActionWalkToPosition(closest_food.position)


    def ActionSeekWater(self, world):
        water_distance = []
        tile_id = []
        for tile in world.water_tile_array:
            
            if (tile.real_max_x >= self.position[0] >= tile.real_x) and (tile.real_max_y >= self.position[1] >= tile.real_y):
                self.thirst = self.max_thirst

            distance = sqrt((self.position[0] - tile.real_x) ** 2 * (self.position[1] - tile.real_y) ** 2)
            water_distance.append(distance)
            tile_id.append(tile)
            
        closest_water_distance = min(water_distance)
        index = water_distance.index(closest_water_distance)
        closest_water = tile_id[index]
        self.ActionWalkToPosition(closest_water.real_position)

    def Excrete(self):
        threshold = round(self.max_hunger * 0.7)
        if self.hunger == threshold:
            x = self.position[0] + 15
            y = self.position[1] + 30
            Entity((x, y), Excrement())

    def Die(self):
        x = self.position[0]
        y = self.position[1]

        if self.direction == "east":
            Entity((x, y), DeadBody(self.dead_sprite_east, self.type))
        else:
            Entity((x, y), DeadBody(self.dead_sprite_west, self.type))
        animal_objects.remove(self)

    def ActionSeekMate(self):
        potential_mates = []
        distance_from_mate = []

        for animal in animal_objects:
            if animal.type.name == self.type.name and animal != self:
                potential_mates.append(animal)
        
        for mate in potential_mates:
            if self.position == mate.position:
                # breed function goes here
                print("bow chicka wow wow")
            
            distance = sqrt( (self.position[0] - mate.position[0]) ** 2 * (self.position[1] - mate.position[1]) ** 2 ) 
            distance_from_mate.append(distance)

        if len(potential_mates) > 0:
            closest_mate_distance = min(distance_from_mate)
            index = distance_from_mate.index(closest_mate_distance)
            closest_mate = potential_mates[index]

            self.ActionWalkToPosition(closest_mate.position)

        # if self.position == food.position:
        #         food_objects.remove(food)
        #         self.hunger = self.max_hunger

        #     distance = sqrt( (self.position[0] - food.position[0]) ** 2 * (self.position[1] - food.position[1]) ** 2 ) 
        #     food_distance.append(distance)
        #     food_id.append(food)

        # closest_food_distance = min(food_distance)
        # index = food_distance.index(closest_food_distance)
        # closest_food = food_id[index]

        # self.ActionWalkToPosition(closest_food.position)



    def PassiveStats(self, tick):
        self.hunger -= 5
        self.thirst -= 10

        if tick % 100 == 0:
            # ticks once every ~0.8s 
            self.age += 1
            if self.age == self.max_age or self.hunger == 0 or self.thirst == 0:
                self.Die()

        if self.hunger <= 0:
            self.hunger = 0
        elif self.hunger >= self.max_hunger:
            self.hunger = self.max_hunger
        if self.thirst <= 0:
            self.thirst = 0
        elif self.thirst >= self.max_thirst:
            self.thirst = self.max_thirst

        self.Excrete()

class Food:
    def __init__(self, position, type):
            self.id = len(food_objects)
            self.type = type
            self.sprite = self.type.sprite
            self.position = position
            food_objects.append(self)
        
    def DrawFood(self):
        screen.blit(self.sprite, self.position)

class Entity:
    def __init__(self, position, type):
            self.id = len(entity_objects)
            self.position = position
            self.type = type

            entity_objects.append(self)

            print(len(entity_objects))
            
    def DrawEntity(self):
        if self.type.name == constants.EXCREMENT:
            pygame.draw.rect(screen, (constants.EXCRETE_BROWN), (self.position[0], self.position[1], 5, 2))
        else:
            screen.blit(self.type.sprite, self.position)