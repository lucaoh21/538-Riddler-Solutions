"""
Solution to the 538 Riddler July.27.2018 
Author: Luca Ostertag-Hill

To run the algorithm use "puzzleSolver(5, 5)".
"""


class DoodlePuzzle:
    """This is a class for solving the 538 DoodlePuzzle Riddle.
    
    Attributes:
        numRows (int): The number of rows in the board.
        numCols (int): The number of columns in the board.
        board ([][]): 2d list that simulates the gameboard.
        stack ([]): List that stores moves required to reach current position.
        currCount (int): The number of visited cells.
        numAnswers (int): The number of solutions found.
    """
    
    def __init__(self, numRows, numCols):
        """The constructor for the DoodlePuzzle class.
        
        Parameters:
            numRows (int): The number of rows in the board.
            numCols (int): The number of columns in the board.
        """
        self.numRows = numRows
        self.numCols = numCols
        self.board = self.gameboard()
        self.stack = []
        self.currCount = 0
        self.numAnswers = 0        
        
    def gameboard(self):
        """Function that constructs the gameboard as a 2d list (matrix)."""
        board = [0] * self.numRows
        for i in range(self.numRows):
            board[i] = [0] * self.numCols
        return board
    
    def addMove(self, row, col):
        """Function that adds a move onto the gameboard and tracks it."""        
        self.board[row][col] = 1
        self.stack.append([row, col])
        self.currCount += 1
        
    def deleteMove(self, row, col):
        """Function that deletes a move off the gameboard and tracks it."""        
        self.board[row][col] = 0
        self.stack.pop()
        self.currCount -= 1
        
    def isCellEmpty(self, row, col):
        """Function to check if the specified cell is empty."""        
        if self.board[row][col] == 0:
            return True
        return False
        
    def isSolved(self):
        """Function to check if the puzzle has been solved."""        
        if self.currCount >= 25:
            self.numAnswers += 1
            return True
        return False
    
    def printStack(self):
        """Function that prints the moves required to get the current
        state of the gameboard.
        """        
        print(self.stack)
        
def puzzleSolver(numRows, numCols):
    """Function that solves the 538 DoodlePuzzle Riddle by checking
    all possible variation of moves from all possible starting positions, 
    and returns the number of possible solutions.
    """    
    puzzle = DoodlePuzzle(numRows, numCols)
    
    #test the problem with each possible starting position
    for i in range(numRows):
        for j in range(numCols):
            testStrat(puzzle, i, j)
    print(puzzle.numAnswers)

def testStrat(puzzle, i, j):
    """Recursive algorithm that tests every possible move and backtracks
    when no more moves are possible.
    """    
    puzzle.addMove(i, j)
    if puzzle.isSolved():
        puzzle.printStack()    
    else:
        #test each of the 8 possible moves from any given position
        if (i + 3) < 5 and puzzle.isCellEmpty(i+3, j):
            testStrat(puzzle, i+3, j)
        if (j + 3) < 5 and puzzle.isCellEmpty(i, j+3):
            testStrat(puzzle, i, j+3)
        if (i - 3) >= 0 and puzzle.isCellEmpty(i-3, j):
            testStrat(puzzle, i-3, j)
        if (j - 3) >= 0 and puzzle.isCellEmpty(i, j-3):
            testStrat(puzzle, i, j-3)
        if (i + 2) < 5 and (j + 2) < 5 and puzzle.isCellEmpty(i+2, j+2):
            testStrat(puzzle, i+2, j+2)
        if (i + 2) < 5 and (j - 2) >= 0 and puzzle.isCellEmpty(i+2, j-2):
            testStrat(puzzle, i+2, j-2)
        if (i - 2) >= 0 and (j + 2) < 5 and puzzle.isCellEmpty(i-2, j+2):
            testStrat(puzzle, i-2, j+2)    
        if (i - 2) >= 0 and (j - 2) >= 0 and puzzle.isCellEmpty(i-2, j-2):
            testStrat(puzzle, i-2, j-2)      

    puzzle.deleteMove(i, j)

#puzzleSolver(5, 5)
