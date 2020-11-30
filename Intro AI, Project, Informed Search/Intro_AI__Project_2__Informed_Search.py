#Written by Joseph Reiss U76703774
#Introduction to AI project #2, Informed Search Problem

#Problem Description: Suppose that the cost of a move in the 8-puzzle is equal to 
#the number of the moved tile. That is, the cost of moving tile 1 is $1, the cost 
#of moving tile 2 is $2, and so on. Calculate the heuristics, the number of 
#displaced tiles, for each states and implement the algorithm A* that finds a 
#cheapest solution; it should read a start state from a file, and print out a 
#cheapest sequence of moves that leads to the goal state given 

#imports
import copy

### FILE NAME ###
#fileName = 'test.txt'
fileName = input("Enter the file name with the extension: ")

class eightPuzzle:

    #constructor
    def __init__(self, startingState):
        self.board = startingState
        self.goalGraph = [[1,2,3],[8,0,4],[7,6,5]]

#####################################################################################################################################################

    #Heuristic function to calculate the h value for the passed state, h value is calculated as number of tiles not the same as goal graph
    def calcHeuristic(self, curr):
        h = 0
        for i in range(3):
            for j in range(3):
                if curr[i][j] != self.goalGraph[i][j]:
                    h = h + 1
        return h

#####################################################################################################################################################

    #function to calculate f value
    def calcFVal(self, nextState, tileMoved):
        f = 0
        g = tileMoved
        h = self.calcHeuristic(nextState)
        f = g + h
        return f

#####################################################################################################################################################

    #function to calculate the total cost of the path up until the current state
    def calcTotalCost(self, totalCost, tileMoved):
        totalCost = totalCost + tileMoved
        print('The total cost so far is: ' + str(totalCost))
        return totalCost

#####################################################################################################################################################
    
    #function to display the current state/graph to the console
    def displayBoard(self, curr_board):
        print('The current graph is: ')
        for n in curr_board:
            print(str(n) + ' ')
        print('\n')

#####################################################################################################################################################

    #function to decide the best move based on the f value of all possible moves
    def calcBestMove(self, fValU, fValD, fValL, fValR, prevMove):
        #case where best move is up
        if fValU <= fValD and fValU <= fValL and fValU <= fValR and prevMove!= 'D':
            return 'U'
        #case where best move is down
        if fValD < fValU and fValD < fValL and fValD < fValR and prevMove != 'U':
            return 'D'
        #case where best move is left
        if fValL <= fValU and fValL <= fValD and fValL <= fValR and prevMove!= 'R':
            return 'L'
        #case where best move is right
        if fValR <= fValU and fValR <= fValD and fValR <= fValL and prevMove != 'L':
            return 'R'

#####################################################################################################################################################
    
    #function to complete the next move of the puzzle
    def moveFunction(self, curr_state, prevMove, totalCost):
        #displaying the current state/board
        self.displayBoard(curr_state)

        #end conditions
        if curr_state == self.goalGraph:
            print('The total path cost was: ' + str(totalCost))
            print('End of Puzzle! Done!')
            return
        if totalCost > 1000:
            print('Their is no solution or it takes too many steps')
            return

        #getting the x and y value of the 0 in the graph
        currBoard = curr_state
        for i in range(3):
            for j in range(3):
                if currBoard[i][j] == 0:
                    x, y = i, j
                    break

        #arbitrary useless values for the purpose of variable declarations
        fValU = 100
        fValD = 100
        fValL = 100
        fValR = 100
        tempGraphU = [[1,2,3],[4,5,6],[7,8,0]]
        tempGraphD = [[1,2,3],[4,5,6],[7,8,0]]
        tempGraphL = [[1,2,3],[4,5,6],[7,8,0]]
        tempGraphR = [[1,2,3],[4,5,6],[7,8,0]]
        
        #case where you can move up
        if x-1 >= 0 and prevMove != 'D':
            tempGraphU = copy.deepcopy(currBoard)
            tempGraphU[x][y] = currBoard[x-1][y]
            tempGraphU[x-1][y] = 0
            fValU = self.calcFVal(tempGraphU, tempGraphU[x][y])

        #case where you can move down
        if x+1 <= 2 and prevMove != 'U':
            tempGraphD = copy.deepcopy(currBoard)
            tempGraphD[x][y] = currBoard[x+1][y]
            tempGraphD[x+1][y] = 0
            fValD = self.calcFVal(tempGraphD, tempGraphD[x][y])

        #case where you can move left
        if y-1 >= 0 and prevMove != 'R':
            tempGraphL = copy.deepcopy(currBoard)
            tempGraphL[x][y] = currBoard[x][y-1]
            tempGraphL[x][y-1] = 0
            fValL = self.calcFVal(tempGraphL, tempGraphL[x][y])

        #case where you can move right
        if y+1 <= 2 and prevMove != 'L':
            tempGraphR = copy.deepcopy(currBoard)
            tempGraphR[x][y] = currBoard[x][y+1]
            tempGraphR[x][y+1] = 0
            fValR = self.calcFVal(tempGraphR, tempGraphR[x][y])
        
        #figuring out the best move
        bestMove = self.calcBestMove(fValU, fValD, fValL, fValR, prevMove)
        print("The best move chosen was: " + bestMove)

        #picking which recursive call to do based on best move and also calculating the new total path cost
        if bestMove == 'U':
            nextState = eightPuzzle(tempGraphU)
            totalCost = self.calcTotalCost(totalCost, tempGraphU[x][y])
            nextState.moveFunction(tempGraphU, bestMove, totalCost)
        elif bestMove == 'D':
            nextState = eightPuzzle(tempGraphD)
            totalCost = self.calcTotalCost(totalCost, tempGraphD[x][y])
            nextState.moveFunction(tempGraphD, bestMove, totalCost)
        elif bestMove == 'L':
            nextState = eightPuzzle(tempGraphL)
            totalCost = self.calcTotalCost(totalCost, tempGraphL[x][y])
            nextState.moveFunction(tempGraphL, bestMove, totalCost)
        elif bestMove == 'R':
            nextState = eightPuzzle(tempGraphR)
            totalCost = self.calcTotalCost(totalCost, tempGraphR[x][y])
            nextState.moveFunction(tempGraphR, bestMove, totalCost)
        else:
            totalCost = 0
            return


#####################################################################################################################################################

    #function to call to solve a puzzle
    def solvePuzzle(self):
        currState = self.board
        goalState = self.goalGraph
        self.moveFunction(currState, ' ', 0)

#####################################################################################################################################################
    
#variable declarations
startingGraph = []
goalGraph = [[1,2,3],[8,0,4],[7,6,5]]

#opening the file and parsing data
with open(fileName, 'r') as file:
    for line in file:
        splitLine = line.split(' ')
        val1 = int(splitLine[0])
        val2 = int(splitLine[1])
        val3 = int(splitLine[2])
        tempGraph = [val1,val2,val3]
        startingGraph.append(tempGraph)

#displaying the graphs to console
print('The graph read in from the file is: ')
for number in startingGraph:
    print(str(number) + ' ')
print('\n')

print('The goal graph is: ')
for number in goalGraph:
    print(str(number) + ' ')
print('\n')

#creating puzzle object and calling the solver function
startingPuzzle = eightPuzzle(startingGraph)
startingPuzzle.solvePuzzle()