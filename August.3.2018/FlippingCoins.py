"""
Solution to the 538 Riddler August.3.2018 
Author: Luca Ostertag-Hill

To run the simulation run "testCoins(numTests, maxFlips)"
ex: testCoins(1000, 1000) for 1000 tests with max 1000 flips each
"""
import random as rd

class FlippingCoins:
    """This is a class for solving the 538 FlippingCoins Riddle.
    
    Attributes:
        numTails (int): The number of flipped coins that landed tails.
        numHeadsNeeded (int): The number of heads needed in a row to win.
    """
    
    def __init__(self):
        """The constructor for the FlippingCoins class.
        
        Parameters: none
        """
        self.numTails = 0
        self.numHeadsNeeded = 1
    
    def flipCoin(self):
        """
        Function to simluate flipping a coin. Landing tails increases
        the number of heads requried thereafter.
        """
        # 0 will be heads, 1 will be false
        if rd.randint(0, 1) == 1:
            self.numHeadsNeeded -= 1
        else:
            self.numTails += 1
            # you always need to flip 1 more head than fails flipped previously
            self.numHeadsNeeded = self.numTails + 1
            
    def checkWin(self):
        """Function to check if the game has been won"""
        if self.numHeadsNeeded <= 0:
            return True
        return False

def testCoins(numTests, maxFlips):
    """
    Function that simulates the flipping coin game. It runs a user
    specified number of tests and a maximum amount of flips per test until
    the user gives up. 
    """
    
    numWins = 0
    numLosses = 0
    
    while(numTests > 0):
        flipsLeft = maxFlips
        coin = FlippingCoins()
        while(flipsLeft > 0):
            coin.flipCoin()
            if coin.checkWin():
                numWins += 1
                break
            flipsLeft -= 1
            
        if flipsLeft <= 0:
            numLosses += 1
        numTests -= 1
        
    print("Number of wins: {0}".format(numWins))
    print("Number of losses: {0}".format(numLosses))
    print("Win percentage: {0}".format(float(numWins)/(numWins+numLosses)))

