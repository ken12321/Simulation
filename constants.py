import pygame

# colors

GUNMETAL = (18, 44, 52)
INDIGO_DYE = (34, 72, 112)
CAROLINA_BLUE = (78, 165, 217)
MEDIUM_TURQUOISE = (68, 207, 203)
PINK_LAVENDER = (239, 189, 235)
AFRICAN_VIOLET = (182, 140, 184)
CAMEL = (187, 157, 128)
VEGAS_GOLD = (191, 174, 72)
GREEN_RYB = (95, 173, 65)
GREEN_CYAN = (45, 147, 108)

EXCRETE_BROWN = (51, 37, 23)


# tile types

SAND = "sand"
GRASS = "grass"
WATER = "water"

# food sprites
APPLE = "apple"
SPRITE_LOAD_APPLE = pygame.image.load('./sprites/apple.png')
SPRITE_APPLE = pygame.transform.scale(SPRITE_LOAD_APPLE, (20, 20))


# animal types and sprites
CAMEL = "camel"
SPRITE_LOAD_CAMEL = pygame.image.load('./sprites/camel.png')
SPRITE_CAMEL_EAST = pygame.transform.scale(SPRITE_LOAD_CAMEL, (35, 35))
SPRITE_CAMEL_WEST = pygame.transform.flip(SPRITE_CAMEL_EAST, True, False)

SPRITE_LOAD_CAMEL_DEAD = pygame.image.load('./sprites/camel_dead.png')
SPRITE_CAMEL_DEAD_EAST = pygame.transform.scale(SPRITE_LOAD_CAMEL_DEAD, (35, 35))
SPRITE_CAMEL_DEAD_WEST = pygame.transform.flip(SPRITE_CAMEL_DEAD_EAST, True, False)


LEOPARD = "leopard"
SPRITE_LOAD_LEOPARD = pygame.image.load('./sprites/leopard.png')
SPRITE_LEOPARD_EAST = pygame.transform.scale(SPRITE_LOAD_LEOPARD, (45, 30))
SPRITE_LEOPARD_WEST = pygame.transform.flip(SPRITE_LEOPARD_EAST, True, False)

SPRITE_LOAD_LEOPARD_DEAD = pygame.image.load('./sprites/leopard_dead.png')
SPRITE_LEOPARD_DEAD_EAST = pygame.transform.scale(SPRITE_LOAD_LEOPARD_DEAD, (45, 30))
SPRITE_LEOPARD_DEAD_WEST = pygame.transform.flip(SPRITE_LEOPARD_DEAD_EAST, True, False)
 

# entities
EXCREMENT = "excrement"
DEADBODY = "deadbody"