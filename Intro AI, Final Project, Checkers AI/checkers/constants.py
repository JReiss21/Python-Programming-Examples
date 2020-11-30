# Joseph Riess U76703774
#
# File for holding all constant values related to the checkers game itself

#-------------------------------------------------------------------------------------------------------------------

#imports
import pygame

#-------------------------------------------------------------------------------------------------------------------

#width and height of screen
WIDTH, HEIGHT = 800, 800

# num rows and cols in the game board, 8x8 is standard checkers board size
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# variables for rgb colors for game
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
LIGHT_GREY = (200, 200, 200)

# variable for crown image loaded from assets folder
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44,25))

#-------------------------------------------------------------------------------------------------------------------