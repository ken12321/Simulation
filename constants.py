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



# tile types

SAND = "sand"
GRASS = "grass"
WATER = "water"


# animal types and sprites
CAMEL = "camel"
SPRITE_LOAD_CAMEL = pygame.image.load('./sprites/camel.png')
SPRITE_CAMEL = pygame.transform.scale(SPRITE_LOAD_CAMEL, (35, 35))
 