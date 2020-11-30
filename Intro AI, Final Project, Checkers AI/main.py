# Joseph Reiss U76703774
#
# This is my final project for Intro to AI
# It is an AI that uses the minimax algorithm to player against the user in a game of checkers.
# Written in python primarily using pygame 

#-------------------------------------------------------------------------------------------------------------------

#imports
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

# constant for rendering/drawing game
FPS = 60

# constant for getting window of the game as well as changing the text for the window
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Joseph Reiss Final Project - Checkers AI')

#-------------------------------------------------------------------------------------------------------------------

# function to get the row and col that the mouse position is at by using a method of integer division
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE  # kind of breaking the board into grid with integer divide in order to tell what pos mouse is at
    col = x // SQUARE_SIZE
    return row, col

#-------------------------------------------------------------------------------------------------------------------

# main function
def main():
    #variables
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)    # main game class object

    # game loop to iterate until game is over
    while run:
        clock.tick(FPS)

        #if it is the AI's turn we are getting the best move aka the best board that the AI can choose using minimax algorithm
        #and passing that to the function to perform the move
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 2, WHITE, game)
            game.ai_move(new_board)

        # checking if there is a winner and if so ending game
        if game.winner() != None:
            if game.winner() == RED:
                print("\n\nRed has won the game!\n\nProgram ending now!\n\n")
            else:
                print("White has won the game!\n\nProgram ending now!\n\n")
            run = False
            
        
        # event handler loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # if user clicks x arrow
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:    # event for if user clicks mouse
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)  
                game.select(row, col)   # selecting checker at row and col of mouse
        game.update()   # updating game every loop
    pygame.quit()
    return 0

main()
#-------------------------------------------------------------------------------------------------------------------