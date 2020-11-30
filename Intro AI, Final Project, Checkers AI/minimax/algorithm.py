# Joseph Reiss U76703774
#
# algorithm file for holding all of the minimax related AI portion of the program

#-------------------------------------------------------------------------------------------------------------------

#imports
from copy import deepcopy
import pygame

#-------------------------------------------------------------------------------------------------------------------

#constants
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#-------------------------------------------------------------------------------------------------------------------

# minimax function
# board: game board
# depth: how many levels of minimax algo
# max_player: bool value saying is player trying to max or minimize
# game: game object
# returns the best board aka the best move that the AI could make on its turn using minimax algorithm
def minimax(board, depth, max_player, game):
    #if at child node or if there is a winner in the game evaluate that board and return the eval with the board
    if depth == 0 or board.winner() != None:
        return board.evaluate(), board

    #considering all moves the AI could make
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(board, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]   # do not need second return (board) when just passing back up recursive stack so ignore it
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:   #considering all moves the player could make
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(board, RED, game):
            evaluation = minimax(move, depth - 1, True, game)[0]    # do not need second return (board) when just passing back up recursive stack so ignore it
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        return minEval, best_move

#-------------------------------------------------------------------------------------------------------------------

#function for getting all the possible moves on a board with the passed color (player)
def get_all_moves(board, color, game):
    moves = []
    for checker in board.get_all_checkers(color):   # for all checkers of passed color
        valid_moves = board.get_valid_moves(checker)    # get all valid moves for each checker
        for move, skip in valid_moves.items():  # while going through each possible move to make we are displaying it to the screen
            draw_moves(game, board, checker)
            temp_board = deepcopy(board)
            temp_checker = temp_board.get_checker(checker.row, checker.col)
            new_board = simulate_board(temp_checker, move, temp_board, game, skip)
            moves.append(new_board)
    return moves

#-------------------------------------------------------------------------------------------------------------------

#function for simulating a board when a specific move is made.
#This is for the purpose of not altering the original game board and still allowing us to compare different moves
def simulate_board(checker, move, board, game, skip):
    board.move(checker, move[0], move[1])
    if skip:
        board.remove(skip)
    return board

#-------------------------------------------------------------------------------------------------------------------

#function to draw the possible valid moves when considering them for the AI
def draw_moves(game, board, checker):
    valid_moves = board.get_valid_moves(checker)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (checker.x, checker.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(200) #just to see the AI's move considerations more slowly

#-------------------------------------------------------------------------------------------------------------------