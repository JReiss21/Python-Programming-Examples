# Joseph Reiss U76703774
#
# Board class for Checkers game
# This class contains functions related to the board obj such as drawing it, creating the two dimension array
# that will represent the board and hold the checkers on it. Also holds the logic for getting all valid moves
# which is arguably the most complex part of the game. 

#-------------------------------------------------------------------------------------------------------------------

#imports
import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, LIGHT_GREY
from .checker import Checker

#-------------------------------------------------------------------------------------------------------------------

# Board class
class Board:
    #constructor
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12    # number of checkers left on board
        self.red_kings = self.white_kings = 0   # number of kings for each color
        self.create_board()

    #-------------------------------------------------------------------------------------------------------------------

    # draw squares function to draw red squares on black background for the game board
    # need to pass the window
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, LIGHT_GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    #-------------------------------------------------------------------------------------------------------------------

    # Function for creating the initial state game board
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])   #interior list that correpsonds to each row
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):  # math for only drawing on odd/even alternating columns to generate first board
                    if row < 3:
                        self.board[row].append(Checker(row, col, WHITE)) # adding white checkers for top part of board
                    elif row > 4:
                       self.board[row].append(Checker(row, col, RED)) # adding red checkers at bottom of board
                    else:
                        self.board[row].append(0)   # all other spots on the board get 0 to represent nothing being there
                else:
                    self.board[row].append(0)   # all other spots on the board get 0 to represent nothing being there

    #-------------------------------------------------------------------------------------------------------------------

    # function for drawing each of the checkers on the game board
    def draw(self, win):
        self.draw_squares(win)  # drawing game board
        for row in range(ROWS): # nested loop to draw checkers
            for col in range(COLS):
                checker = self.board[row][col]
                if checker != 0:
                    checker.draw(win)

    #-------------------------------------------------------------------------------------------------------------------

    # function to handle moving on the board aka the two dimensional array that represents the game board
    def move(self, checker, row, col):
        # swapping positions of checkers which would be a checker to an empty spot
        self.board[checker.row][checker.col], self.board[row][col] = self.board[row][col], self.board[checker.row][checker.col]
        checker.move(row, col)

        # if checker moves to either end of board then make it a king 
        if row == ROWS - 1 or row == 0:
            checker.make_king()
            if checker.color == RED and checker.king == False:
                self.red_kings += 1
            elif checker.color == WHITE and checker.king == False:
                self.white_kings += 1

    #-------------------------------------------------------------------------------------------------------------------

    # function for getting the current checker at a specific row and col if there exists one
    def get_checker(self, row, col):
        return self.board[row][col]

    #-------------------------------------------------------------------------------------------------------------------

    # function for getting a dictionary containing all the valid moves for a selected checker
    def get_valid_moves(self, checker):
        # will be a dictionary where keys are all valid moves and the values pertaining to those keys are 
        # any other checker that was jumped so we know to remove it afterwards
        moves = {}
        left = checker.col - 1
        right = checker.col + 1
        row = checker.row

        # allowing moves upwards only if checker is red or if it is a king
        if checker.color == RED or checker.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, checker.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, checker.color, right))
        # allowing moves downwards only if checker is white or if it is a king
        if checker.color == WHITE or checker.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, checker.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, checker.color, right))

        #returning dictionary containing all valid moves
        return moves

    #-------------------------------------------------------------------------------------------------------------------

    # function to look on left diagonal
    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []

        # what row are we starting at, stoping at, and how much to step by passed by parameters
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, skipped = last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
            
        #returning dictionary of moves on left diagonal
        return moves

    #-------------------------------------------------------------------------------------------------------------------

    # function to look on right diagonal
    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []

        # what row are we starting at, stoping at, and how much to step by passed by parameters
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    if step == -1:
                        row = max(r - 3, -1)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, skipped = last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1

        #returning dictionary of moves on right diagonal
        return moves

    #-------------------------------------------------------------------------------------------------------------------

    # function for removing a checker from the board
    def remove(self, checkers):
        for checker in checkers:    
            self.board[checker.row][checker.col] = 0    # setting it equal to 0 aka removing it
            if checker != 0:
                if checker.color == RED:
                    self.red_left -= 1  # if checker was red then decrementing red count
                else:
                    self.white_left -= 1    # if checker was white then decrementing white count

    #-------------------------------------------------------------------------------------------------------------------

    # function for getting winner of game by checking count for each
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        return None

    #-------------------------------------------------------------------------------------------------------------------

    #function to get the current score of the game board
    #used by the AI portion of the program
    def evaluate(self):
        return self.white_left - self.red_left + (self.white_kings * 1/2 - self.red_kings * 1/2)

    #-------------------------------------------------------------------------------------------------------------------

    #function for getting all checkers of the passed color in the current game board
    #used by the AI portion of the program
    def get_all_checkers(self, color):
        checkers = []
        for row in self.board:
            for checker in row:
                if checker != 0 and checker.color == color:
                    checkers.append(checker)
        return checkers

#-------------------------------------------------------------------------------------------------------------------