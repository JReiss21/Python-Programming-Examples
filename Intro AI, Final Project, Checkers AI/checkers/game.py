# Joseph Reiss U76703774
#
# Game class for checkers game
# This class holds most of the general logic for the game such as moving and selecting checkers,
# changing turns, updating the game and so on.

#-------------------------------------------------------------------------------------------------------------------

#imports
import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from .board import Board

#-------------------------------------------------------------------------------------------------------------------

# game class for the purpose of interfacing with board and checkers and other parts of the game
class Game:
    #constructor
    def __init__(self, win):
        self._init()
        self.win = win

    #-------------------------------------------------------------------------------------------------------------------

    # function for initializing game
    def _init(self):
        self.selected = None    # checker selected
        self.board = Board()    # game board
        self.turn = RED         # first turn, will always be red unless changed here
        self.valid_moves = {}   # telling us what current valid moves are for current players turn

    #-------------------------------------------------------------------------------------------------------------------

    # function for updating game and board drawn to screen
    def update(self):
        self.board.draw(self.win)   # drawing game board
        self.draw_valid_moves(self.valid_moves) # drawing valid moves based on selected checker
        pygame.display.update()

    #-------------------------------------------------------------------------------------------------------------------

    # function to reset game
    def reset(self):
        self._init()

    #-------------------------------------------------------------------------------------------------------------------

    # function to select a checker based on the row and col
    def select(self, row, col):
        #logic to check if checker is already selected and if next spot clicked is valid move or not
        if self.selected:  
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        #logic for checking if selected checker actually exists and it is the current turn for them
        checker = self.board.get_checker(row, col)
        if checker != 0 and checker.color == self.turn:
            self.selected = checker
            self.valid_moves = self.board.get_valid_moves(checker)    #getting valid moves for selected checker
            return True
        return False

    #-------------------------------------------------------------------------------------------------------------------

    # function for handling a move in the game
    def _move(self, row, col):
        checker = self.board.get_checker(row, col)
        # if we select a spot and the spot is a 0 and its part of valid moves
        if self.selected and checker == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col) # move current checker to that spot
            skipped = self.valid_moves[(row, col)] # all the checkers that mightve been skipped over
            if skipped:
                self.board.remove(skipped)  # removing skipped over checkers
            self.change_turn()  # changing turns
        else:
            return False
        return True

    #-------------------------------------------------------------------------------------------------------------------

    # function for changing turns
    def change_turn(self):
        # changing valid moves to none so that way after a move the blue circles indicating valid moves stop showing
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    #-------------------------------------------------------------------------------------------------------------------

    # function for indicating valid moves on board when checker is selected
    def draw_valid_moves(self, moves):
        # drawing blue circle on each square indicating a valid move
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    #-------------------------------------------------------------------------------------------------------------------

    # function for getting winner
    def winner(self):
        return self.board.winner()

    #-------------------------------------------------------------------------------------------------------------------

    #function to return the current board for the game
    def get_board(self):
        return self.board

    #-------------------------------------------------------------------------------------------------------------------

    #function to perform the AI's turn in the game
    def ai_move(self, board):
        self.board = board
        self.change_turn()

#-------------------------------------------------------------------------------------------------------------------