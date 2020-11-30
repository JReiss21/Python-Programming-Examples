# Joseph Reiss U76703774
#
# Checker class for Checkers game
# This class holds all of the functions related to each individual checker such as getting its position, making it a king,
# drawing the checker and moving it

#-------------------------------------------------------------------------------------------------------------------

#imports
import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN

#-------------------------------------------------------------------------------------------------------------------

# Checker class
class Checker:
    #variables related to drawing the checker
    PADDING = 15 # higher the padding the smaller the checker
    OUTLINE = 2 # higher the outline the bigger the outline on checker is

    #-------------------------------------------------------------------------------------------------------------------

    #constructor
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    #-------------------------------------------------------------------------------------------------------------------

    # function for getting position of a checker
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    #-------------------------------------------------------------------------------------------------------------------

    # function for making a checker a king when it reaches either end of board
    def make_king(self):
        self.king = True

    #-------------------------------------------------------------------------------------------------------------------

    # function for drawing checkers on the board
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2 ))

    #-------------------------------------------------------------------------------------------------------------------

    # repr function for checker class
    def __repr__(self):
        return str(self.color)

    #-------------------------------------------------------------------------------------------------------------------

    # function for moving a checker by changing its row/col then calc its pos
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

#-------------------------------------------------------------------------------------------------------------------