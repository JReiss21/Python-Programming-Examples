#Written by Joseph Reiss U76703774
#Introduction to AI project #3, Hexagon Game

# Problem Description: The hexagon game involves two players, who gradually construct a six-vertex
# undirected graph with solid and dashed edges. Player 1 adds solid edges, whereas Player 2 uses dashes.
# The players begin with a six-vertex graph that has no edges (Figure 1), and add new edges, one by one; 
# Player 1 makes the first move. At each move, a player has to add a new edge between two vertices that 
# are not connected by any old edge. Figure 2 is an example of a mid-game position, where Player 1 
# has to make the next move.If Player 1 constructs a solid-line triangle, he loses the game; similarly,
# a dashed triangle means a loss of Player 2. For example, if the game ends as shown in Figure 3, then
# Player 2 has lost since he has constructed the dashed triangle “3-5-6.”Implement a program for playing
# the hexagon game. Your program should prompt the user to enter a player number (1 or 2), and then
# act as the specified player. For example, if the user enters “1”, the program should make the first move.

#imports
import random

#main class for the game
class hexagonGame:
#######################################################################################################################################################

    #constructor
    def __init__(self, firstTurn):
        self.turn = firstTurn   #setting the turn equal to the passed value for first turn
        self.board = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}   #Variable for the overall game board, this holds both players edges they created
        self.player1Board = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}    #Variable to hold player 1's game board, this holds just their edges created
        self.player2Board = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}    #Variable to hold player 2's game board, this holds just their edges created

#######################################################################################################################################################

    #function to display the current game graph (game state)
    def displayGraph(self):
        print("\nThe current game graph is: ")      #displaying the overall game graph
        for vertice in self.board:
            print(vertice, end = '')
            print(':', end = '')
            edges = self.board[vertice]
            print(edges)

        print("Player 1 has edges on vertices: ")       #displaying the AI's edges
        for vertice in self.player1Board:
            print(vertice, end = '')
            print(':', end = '')
            edges = self.player1Board[vertice]
            print(edges)

        print("You have edges on vertices: ")       #displaying the players edges
        for vertice in self.player2Board:
            print(vertice, end = '')
            print(':', end = '')
            edges = self.player2Board[vertice]
            print(edges)

#######################################################################################################################################################

    #function for when it is player 1's turn which is the user
    def player2Turn(self):
        print("\nIts your turn!")

        #input and looping validation check for edge vertices
        while True:
            vertice1 = input("Enter the first vertice of the edge: ")
            vertice2 = input("Enter the second vertice of the edge: ")
            try:    #checking if an integer was entered
                vertice1 = int(vertice1)
                vertice2 = int(vertice2)
                if vertice1 == vertice2:
                    print("Invalid input, Vertice 1 and Vertice 2 cannot be the same. Try Again!")
                    continue
                if (vertice1 > 6 or vertice1 < 1) or (vertice2 > 6 or vertice2 < 1):    #checking bounds 1-6
                    print("Invalid input, Input out of range! Valid integers are 1-6 only! Try Again!")
                    continue
                if vertice1 in self.board[vertice2] and vertice2 in self.board[vertice1]:  #checking to see if this edge already exists for either players (cannot overlap)
                    print("There is already an edge with those two vertices! Pick Another!")
                    continue
            except:     #exception message for when try block throws error (if non integer entered)
                print("Invalid input, Valid integers are 1-6 only! Try Again!")
                continue
            break   #break out of loop if no errors detected in input

        #adding the edge to both the player graph and game graph
        self.player2Board[vertice1].append(vertice2)
        self.player2Board[vertice2].append(vertice1)
        self.board[vertice1].append(vertice2)
        self.board[vertice2].append(vertice1)

        #checking if player 1 has lost with their last move
        if self.checkGameState() == 2:
            print("Player 1 Has WON!\n")
        else:
            self.player1Turn()

#######################################################################################################################################################

    #function for when it is player 2's turn which is the AI
    def player1Turn(self):
        print("\nIts player 1's turn!")

        #input and looping validation check for edge vertices
        while True:
            vertice1 = random.randint(1,6)
            vertice2 = random.randint(1,6)
            if vertice1 == vertice2:
                continue
            if vertice1 in self.board[vertice2] and vertice2 in self.board[vertice1]:  #checking to see if this edge already exists for either players (cannot overlap)
                continue
            break   #break out of loop if no errors detected in input
        print("Player 1 chose to add an edge with vertices " + str(vertice1) + " and " + str(vertice2))

        #adding the edge to the player board and game board
        self.player1Board[vertice1].append(vertice2)
        self.player1Board[vertice2].append(vertice1)
        self.board[vertice1].append(vertice2)
        self.board[vertice2].append(vertice1)
        
        #displaying the game boards
        self.displayGraph()

        #checking if player 2 has lost with their last move
        if self.checkGameState() == 1:
            print("YOU HAVE WON!\n")
        else:
            self.player2Turn()

#######################################################################################################################################################

    #function to check game state to see if it is over
    def checkGameState(self):
        #PLAYER 1 CASES FOR LOST GAME
        #case 1 for player 1, Triangle with vertices 1,2,3
        if 2 in self.player1Board[1] and 3 in self.player1Board[1] and 3 in self.player1Board[2]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 1,2,3.")
            return 1
        #case 2 for player 1, Triangle with vertices 1,2,4
        if 2 in self.player1Board[1] and 4 in self.player1Board[1] and 4 in self.player1Board[2]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 1,2,4.")
            return 1
        #case 3 for player 1, Triangle with vertices 1,2,5
        if 2 in self.player1Board[1] and 5 in self.player1Board[1] and 5 in self.player1Board[2]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 1,2,5.")
            return 1
        #case 4 for player 1, Triangle with vertices 1,2,6
        if 2 in self.player1Board[1] and 6 in self.player1Board[1] and 6 in self.player1Board[2]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 1,2,6.")
            return 1
        #case 5 for player 1, Triangle with vertices 1,3,4
        if 3 in self.player1Board[1] and 4 in self.player1Board[1] and 4 in self.player1Board[3]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 1,3,4.")
            return 1
        #case 6 for player 1, Triangle with vertices 1,3,5
        if 3 in self.player1Board[1] and 5 in self.player1Board[1] and 5 in self.player1Board[3]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 1,3,5.")
            return 1
        #case 7 for player 1, Triangle with vertices 1,3,6
        if 3 in self.player1Board[1] and 6 in self.player1Board[1] and 6 in self.player1Board[3]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 1,3,6.")
            return 1
        #case 8 for player 1, Triangle with vertices 1,4,5
        if 4 in self.player1Board[1] and 5 in self.player1Board[1] and 5 in self.player1Board[4]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 1,4,5.")
            return 1
        #case 9 for player 1, Triangle with vertices 1,4,6
        if 4 in self.player1Board[1] and 6 in self.player1Board[1] and 6 in self.player1Board[5]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 1,4,6.")
            return 1
        #case 10 for player 1, Triangle with vertices 1,5,6
        if 5 in self.player1Board[1] and 6 in self.player1Board[1] and 6 in self.player1Board[5]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 1,5,6.")
            return 1
        #case 11 for player 1, Triangle with vertices 2,3,4
        if 3 in self.player1Board[2] and 4 in self.player1Board[2] and 4 in self.player1Board[3]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 2,3,4.")
            return 1
        #case 12 for player 1, Triangle with vertices 2,3,5
        if 3 in self.player1Board[2] and 5 in self.player1Board[2] and 5 in self.player1Board[3]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 2,3,5.")
            return 1
        #case 13 for player 1, Triangle with vertices 2,3,6
        if 3 in self.player1Board[2] and 6 in self.player1Board[2] and 6 in self.player1Board[3]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 2,3,6.")
            return 1
        #case 14 for player 1, Triangle with vertices 2,4,5
        if 4 in self.player1Board[2] and 5 in self.player1Board[2] and 5 in self.player1Board[4]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 2,4,5.")
            return 1
        #case 15 for player 1, Triangle with vertices 2,4,6
        if 4 in self.player1Board[2] and 6 in self.player1Board[2] and 6 in self.player1Board[4]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 2,4,6.")
            return 1
        #case 16 for player 1, Triangle with vertices 2,5,6
        if 5 in self.player1Board[2] and 6 in self.player1Board[2] and 6 in self.player1Board[5]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 2,5,6.")
            return 1
        #case 17 for player 1, Triangle with vertices 3,4,5
        if 4 in self.player1Board[3] and 5 in self.player1Board[3] and 5 in self.player1Board[4]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 3,4,5.")
            return 1
        #case 18 for player 1, Triangle with vertices 3,4,6
        if 4 in self.player1Board[3] and 6 in self.player1Board[3] and 6 in self.player1Board[4]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 3,4,6.")
            return 1
        #case 19 for player 1, Triangle with vertices 3,5,6
        if 5 in self.player1Board[3] and 6 in self.player1Board[3] and 6 in self.player1Board[5]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 3,5,6.")
            return 1
        #case 20 for player 1, Triangle with vertices 4,5,6
        if 5 in self.player1Board[4] and 6 in self.player1Board[4] and 6 in self.player1Board[5]:
            self.displayGraph()
            print("\nPlayer 1 has made a triangle with vertices 4,5,6.")
            return 1

        #PLAYER 2 CASES FOR LOST GAME
        #case 1 for player 2, Triangle with vertices 1,2,3
        if 2 in self.player2Board[1] and 3 in self.player2Board[1] and 3 in self.player2Board[2]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 1,2,3.")
            return 2
        #case 2 for player 2, Triangle with vertices 1,2,4
        if 2 in self.player2Board[1] and 4 in self.player2Board[1] and 4 in self.player2Board[2]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 1,2,4.")
            return 2
        #case 3 for player 2, Triangle with vertices 1,2,5
        if 2 in self.player2Board[1] and 5 in self.player2Board[1] and 5 in self.player2Board[2]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 1,2,5.")
            return 2
        #case 4 for player 2, Triangle with vertices 1,2,6
        if 2 in self.player2Board[1] and 6 in self.player2Board[1] and 6 in self.player2Board[2]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 1,2,6.")
            return 2
        #case 5 for player 2, Triangle with vertices 1,3,4
        if 3 in self.player2Board[1] and 4 in self.player2Board[1] and 4 in self.player2Board[3]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 1,3,4.")
            return 2
        #case 6 for player 2, Triangle with vertices 1,3,5
        if 3 in self.player2Board[1] and 5 in self.player2Board[1] and 5 in self.player2Board[3]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 1,3,5.")
            return 2
        #case 7 for player 2, Triangle with vertices 1,3,6
        if 3 in self.player2Board[1] and 6 in self.player2Board[1] and 6 in self.player2Board[3]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 1,3,6.")
            return 2
        #case 8 for player 2, Triangle with vertices 1,4,5
        if 4 in self.player2Board[1] and 5 in self.player2Board[1] and 5 in self.player2Board[4]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 1,4,5.")
            return 2
        #case 9 for player 2, Triangle with vertices 1,4,6
        if 4 in self.player2Board[1] and 6 in self.player2Board[1] and 6 in self.player2Board[5]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 1,4,6.")
            return 2
        #case 10 for player 2, Triangle with vertices 1,5,6
        if 5 in self.player2Board[1] and 6 in self.player2Board[1] and 6 in self.player2Board[5]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 1,5,6.")
            return 2
        #case 11 for player 2, Triangle with vertices 2,3,4
        if 3 in self.player2Board[2] and 4 in self.player2Board[2] and 4 in self.player2Board[3]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 2,3,4.")
            return 2
        #case 12 for player 2, Triangle with vertices 2,3,5
        if 3 in self.player2Board[2] and 5 in self.player2Board[2] and 5 in self.player2Board[3]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 2,3,5.")
            return 2
        #case 13 for player 2, Triangle with vertices 2,3,6
        if 3 in self.player2Board[2] and 6 in self.player2Board[2] and 6 in self.player2Board[3]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 2,3,6.")
            return 2
        #case 14 for player 2, Triangle with vertices 2,4,5
        if 4 in self.player2Board[2] and 5 in self.player2Board[2] and 5 in self.player2Board[4]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 2,4,5.")
            return 2
        #case 15 for player 2, Triangle with vertices 2,4,6
        if 4 in self.player2Board[2] and 6 in self.player2Board[2] and 6 in self.player2Board[4]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 2,4,6.")
            return 2
        #case 16 for player 2, Triangle with vertices 2,5,6
        if 5 in self.player2Board[2] and 6 in self.player2Board[2] and 6 in self.player2Board[5]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 2,5,6.")
            return 2
        #case 17 for player 2, Triangle with vertices 3,4,5
        if 4 in self.player2Board[3] and 5 in self.player2Board[3] and 5 in self.player2Board[4]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 3,4,5.")
            return 2
        #case 18 for player 2, Triangle with vertices 3,4,6
        if 4 in self.player2Board[3] and 6 in self.player2Board[3] and 6 in self.player2Board[4]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 3,4,6.")
            return 2
        #case 19 for player 2, Triangle with vertices 3,5,6
        if 5 in self.player2Board[3] and 6 in self.player2Board[3] and 6 in self.player2Board[5]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 3,5,6.")
            return 2
        #case 20 for player 2, Triangle with vertices 4,5,6
        if 5 in self.player2Board[4] and 6 in self.player2Board[4] and 6 in self.player2Board[5]:
            self.displayGraph()
            print("\nYou have made a triangle with vertices 4,5,6.")
            return 2

        #case where no one lost yet
        return 0

#######################################################################################################################################################
        
    #function to start a new game
    def startGame(self):
        if(self.turn == 1):
            self.player1Turn()
        elif(self.turn == 2):
            self.player2Turn()
        else:
            print("Something went wrong")

#######################################################################################################################################################

    ##########  MAIN CODE   ############

#variables
playAgain = 'y'
playerTurn = 0

#main loop to execute for as many times as the user wants to play
while(playAgain == 'y' or playAgain == 'Y'):
    print("\nWELCOME TO THE HEXAGON GAME!\n")     #welcome message to indicate new game

    #getting input as well as input validation for what player takes first turn
    while True:
        print("The user is player 2 and the AI is player 1.")
        playerTurn = input("Enter who's turn is first (1/2): ")
        try:
            playerTurn = int(playerTurn)
        except:
            print("Invalid input, valid input is 1 or 2. Try again!\n")
            continue
        if(playerTurn != 1 and playerTurn != 2):
            print("Invalid input, valid input is 1 or 2. Try again!\n")
            continue
        break

    #creating a new game object and than starting the game with the passed first player turn value
    game = hexagonGame(playerTurn)
    game.startGame()

    while True:
        playAgain = input("Would you like to play again? (y/n): ")
        if(playAgain != 'y' and playAgain != 'Y' and playAgain != 'n' and playAgain != 'N'):
            print("Invalid input, valid input is 'y' or 'n' only. Try Again!\n")
            continue
        break

#End game message after user enters n or N when asked to play again
print("\nEnd Of Game! Thanks For Playing!\n")