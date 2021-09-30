import constants

class Camel:
    def __init__(self):
        self.name = constants.CAMEL
        self.sprite_east = constants.SPRITE_CAMEL_EAST
        self.sprite_west = constants.SPRITE_CAMEL_WEST
        self.dead_sprite_east = constants.SPRITE_CAMEL_DEAD_EAST
        self.dead_sprite_west = constants.SPRITE_CAMEL_DEAD_WEST
        self.minspeed = 4
        self.maxspeed = 8
        self.max_hunger = 1000
        self.max_thirst = 1000
        self.max_age = 150 # in approx milliseconds

class Leopard:
    def __init__(self):
        self.name = constants.LEOPARD
        self.sprite_east = constants.SPRITE_LEOPARD_EAST
        self.sprite_west = constants.SPRITE_LEOPARD_WEST
        self.dead_sprite_east = constants.SPRITE_LEOPARD_DEAD_EAST
        self.dead_sprite_west = constants.SPRITE_LEOPARD_DEAD_WEST
        self.minspeed = 5
        self.maxspeed = 8
        self.max_hunger = 1000
        self.max_thirst = 1000
        self.max_age = 150 # in approx milliseconds
        

        