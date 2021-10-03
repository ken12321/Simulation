import pygame

XSIZE = 700
YSIZE = XSIZE

#max tiles in x and y
TOTAL_WORLD_SIZE = 20

XSCREENSCALING = int(XSIZE / TOTAL_WORLD_SIZE)
YSCREENSCALING = int(YSIZE / TOTAL_WORLD_SIZE)

# colors
GUNMETAL = (18, 44, 52)
INDIGO_DYE = (34, 72, 112)
SHALLOW_WATER_COLOR = (78, 165, 217)
DEEP_WATER_COLOR = (78, 140, 207)
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
DEEP_WATER = "deepwater"

# food sprites
APPLE_X_SIZE = int(0.5 * XSCREENSCALING)
APPLE_Y_SIZE = int(0.5 * YSCREENSCALING)
APPLE = "apple"
SPRITE_LOAD_APPLE = pygame.image.load('./sprites/apple.png')
SPRITE_APPLE = pygame.transform.scale(SPRITE_LOAD_APPLE, (APPLE_X_SIZE, APPLE_Y_SIZE))


# animal types and sprites
CAMEL_Y_SIZE = int(1.75 * XSCREENSCALING)
CAMEL_X_SIZE = int(1.75 * YSCREENSCALING)

CAMEL = "camel"
SPRITE_LOAD_CAMEL = pygame.image.load('./sprites/camel.png')
SPRITE_CAMEL_EAST = pygame.transform.scale(SPRITE_LOAD_CAMEL, (CAMEL_X_SIZE, CAMEL_Y_SIZE))
SPRITE_CAMEL_WEST = pygame.transform.flip(SPRITE_CAMEL_EAST, True, False)

SPRITE_LOAD_CAMEL_DEAD = pygame.image.load('./sprites/camel_dead.png')
SPRITE_CAMEL_DEAD_EAST = pygame.transform.scale(SPRITE_LOAD_CAMEL_DEAD, (CAMEL_X_SIZE, CAMEL_Y_SIZE))
SPRITE_CAMEL_DEAD_WEST = pygame.transform.flip(SPRITE_CAMEL_DEAD_EAST, True, False)


LEOPARD_Y_SIZE = int(1.5 * XSCREENSCALING)
LEOPARD_X_SIZE = int(1.75 * YSCREENSCALING)

LEOPARD = "leopard"
SPRITE_LOAD_LEOPARD = pygame.image.load('./sprites/leopard.png')
SPRITE_LEOPARD_EAST = pygame.transform.scale(SPRITE_LOAD_LEOPARD, (LEOPARD_X_SIZE, LEOPARD_Y_SIZE))
SPRITE_LEOPARD_WEST = pygame.transform.flip(SPRITE_LEOPARD_EAST, True, False)

SPRITE_LOAD_LEOPARD_DEAD = pygame.image.load('./sprites/leopard_dead.png')
SPRITE_LEOPARD_DEAD_EAST = pygame.transform.scale(SPRITE_LOAD_LEOPARD_DEAD, (LEOPARD_X_SIZE, LEOPARD_Y_SIZE))
SPRITE_LEOPARD_DEAD_WEST = pygame.transform.flip(SPRITE_LEOPARD_DEAD_EAST, True, False)
 

# entities and sprites
EXCREMENT = "excrement"

DEADBODY = "deadbody"

TREE = "tree"
SPRITE_LOAD_TREE = pygame.image.load('./sprites/tree.png')
SPRITE_TREE = pygame.transform.scale(SPRITE_LOAD_TREE, (20, 40))