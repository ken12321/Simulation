import constants

class Camel:
    def __init__(self):
        self.name = constants.CAMEL
        self.minspeed = 4
        self.maxspeed = 6
        self.max_hunger = 1000
        self.max_thirst = 1000
        self.sprite_east = constants.SPRITE_CAMEL_EAST
        self.sprite_west = constants.SPRITE_CAMEL_WEST

class Leopard:
    def __init__(self):
        self.name = constants.LEOPARD
        self.minspeed = 7
        self.maxspeed = 10
        self.max_hunger = 1000
        self.max_thirst = 1000
        self.sprite_east = constants.SPRITE_LEOPARD_EAST
        self.sprite_west = constants.SPRITE_LEOPARD_WEST

        