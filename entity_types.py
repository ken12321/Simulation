import constants

class Excrement:
    def __init__(self):
        self.name = constants.EXCREMENT

class DeadBody:
    def __init__(self, sprite, animal):
        self.name = constants.DEADBODY
        self.animal = animal
        self.sprite = sprite

class Tree:
    def __init__(self, fruit):
        self.name = constants.TREE
        self.sprite = constants.SPRITE_TREE
        self.fruit = fruit
