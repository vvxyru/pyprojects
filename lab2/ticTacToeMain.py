# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 2 - Debugging: Tic-Tac-Toe
#
# ~ Created by CMPUT 175 Team ~
# =================================================================

import time, os
from ticTacToe import TicTacToe

def clear():
    '''
    clears the screen
    '''
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


def getCoord(player, dimension):
    '''
    Prompts for an index value corresponding to either the row or column (as
    described by dimension) of a square on the board
    Inputs:
       player (int) - number of current player (1 or 2)
       dimension (str) - describes what the index relates to (e.g. 'row' or 'column')
    Returns: int index (either row or column)
    '''
    # BUG HERE (logic) Only allows inputs 0 and 1
    LOWER = 0
    UPPER = 3
    index = input('Player ' + str(player) + ', please enter a ' + dimension+': ')
    while True:
        if index.isdigit() and int(index) in range(LOWER, UPPER):
            # BUG HERE (logic) Doesn't properly return the players input as an integer
            # return index
            return int(index)
        else:
            index = input(f"Invalid input! Please enter a valid {dimension}: ")


def isGameOver(myBoard, player):
    '''
    The game is over if the current player has won, or there are no empty squares
    left for the next player to select.
    Inputs:
       myBoard (TicTacToe) - object containing current state of game board
       player (int) - number of current player (1 or 2)
    Returns: True if game if over; False otherwise
    '''
    # BUG HERE (syntax) Needs to have capital B's in drawBoard()
    if myBoard.isWinner(player):
        clear()
        # myBoard.drawboard()
        myBoard.drawBoard()
        print ('Player', player ,"wins. Congrats!")           
        return True
    elif myBoard.boardFull():
        clear()
        # myBoard.drawboard()
        myBoard.drawBoard()
        print ("It's a tie.")             
        return True
    return False


def playAgain():
    '''
    Asks if a new game should be started. A valid answer is any entry that begins
    with y/Y/n/N.
    Inputs: none
    Returns: True if a new game should start; False otherwise
    '''
    playAgain = ' ' 
    # validate user's input
    while playAgain[0].upper() not in ['Y', 'N']:
        playAgain=input("Do you want to play another game? (Y/N) ")

    # BUG HERE (logic) clear screen after player says 'Y'
    # (matching video output)
    if playAgain.upper() == "Y":
        clear()

    return playAgain[0].upper() == "Y"   


def main():
    '''
    Controls the game flow for a 2-player version of Numerical Tic Tac Toe.
    Inputs: none
    Returns: None
    '''
    newGame = True

    # BUG HERE (logic) Prints the title after every new game
    # (matches video sample output)
    TITLE = "Starting new Numerical Tic Tac Toe game"
    print("-"*len(TITLE))
    print (TITLE)
    print("-"*len(TITLE))

    while newGame:
        # TITLE = "Starting new Numerical Tic Tac Toe game"
        # print("-"*len(TITLE))
        # print (TITLE)
        # print("-"*len(TITLE))
        myBoard = TicTacToe()
        gameOver=False
        turn = 0
        while not gameOver:
            # BUG HERE (syntax) drawBoard has an uppercase B
            # myBoard.drawboard()

            myBoard.drawBoard()
            
            # get input from user
            entry = ['O','X'][turn]

            row = getCoord(turn+1, 'row')
            col = getCoord(turn+1, 'column')
                                   
            # update board and check if game continues
            if myBoard.update(row, col, entry):
                print(f"Player {turn+1}'s turn ended")

                # FIX**
                time.sleep(1)
                clear()

                gameOver = isGameOver(myBoard, turn+1)

                # BUG HERE (logic) Does not correctly alternate the player.
                # Floor (//) is not the same as (%), floor will always keep the 
                # same turn in this case
                turn = (turn+1) % 2            
            # need to reprompt for new input for given player   
            else:
                print('Error: could not make move!')

            # BUG HERE (logic) clear and time.sleep(1) should be after the turn ended
            # message (SEE fix** above)
            # (matching video output)

            # time.sleep(1)
            # clear()

        # BUG HERE (syntax) Does not assign newGame to the function
        # newGame = playAgain
        newGame = playAgain()
            
    print('Thanks for playing! Goodbye.')
            
# BUG HERE (syntax) Function does not run, needs to be unindented
main()      
