numAnswers = 0
def puzzle():
    rows = 5
    cols = 5
    
    #creating our gameboard
    board = [0] * rows
    for i in range(rows):
        board[i] = [0] * cols
    
    #stack keeps track of the order of moves for each solution
    stack = []
    numAnswers = 0
    currCount = 0
    
    #test the problem with each possible starting position
    for i in range(rows):
        for j in range(cols):
            testStrat(board, i, j, stack, currCount)
    global numAnswers
    print(numAnswers)


#recursive algorithm that tests each possible move
def testStrat(board, i, j, stack, currCount):
    board[i][j] = 1;
    stack.append([i, j])
    currCount += 1
    
    #count=0
    #for row in range(5):
        #for col in range(5):
            #if board[row][col] == 1:
                #count += 1
    
    if currCount >= 25:
        global numAnswers
        numAnswers += 1
        print(stack)
    
    #test each of the 8 possible moves from any given position
    if (i + 3) < 5 and board[i+3][j] == 0:
        testStrat(board, i+3, j, stack, currCount)
    if (j + 3) < 5 and board[i][j+3] == 0:
        testStrat(board, i, j+3, stack, currCount)
    if (i - 3) >= 0 and board[i-3][j] == 0:
        testStrat(board, i-3, j, stack, currCount)
    if (j - 3) >= 0 and board[i][j-3] == 0:
        testStrat(board, i, j-3, stack, currCount)
    if (i + 2) < 5 and (j + 2) < 5 and board[i+2][j+2] == 0:
        testStrat(board, i+2, j+2, stack, currCount)
    if (i + 2) < 5 and (j - 2) >= 0 and board[i+2][j-2] == 0:
        testStrat(board, i+2, j-2, stack, currCount)
    if (i - 2) >= 0 and (j + 2) < 5 and board[i-2][j+2] == 0:
        testStrat(board, i-2, j+2, stack, currCount)    
    if (i - 2) >= 0 and (j - 2) >= 0 and board[i-2][j-2] == 0:
        testStrat(board, i-2, j-2, stack, currCount)      

    board[i][j] = 0
    stack.pop()
    currCount -= 1

puzzle()

#[X,O,O,X,O]
#[X,O,X,O,O]
#[O,X,O,O,X]
#[X,O,O,X,O]
#[X,O,X,X,O]

#[ 0, 15, 18,  1, 14]
#[10, 21,  4, 11, 20]
#[17,  7, 24, 16,  6]
#[ 3, 12, 19,  2, 13]
#[ 9, 22,  5,  8, 23]