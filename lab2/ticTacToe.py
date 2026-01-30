# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 2 - Debugging: Tic-Tac-Toe
#
# ~ Created by CMPUT 175 Team ~
# =================================================================

SIZE = 3

class TicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = SIZE   # number of columns and rows of board
        
        # populate the empty squares in board with " "

        # Should use _ instead lol but whatever
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(" ")
            self.board.append(row)
   
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |           
        
        # BUG HERE (logic) Uses 1, 2, 3 instead of 0, 1, 2.
        print('   0   1   2 ')
        seperator = '  -----------'
        for x in range(len(self.board)):
            temp = []
            for y in self.board[x]:
                if y == " ":
                    temp.append("   ")
                elif y == "O": 
                    temp.append(' \033[91mO\033[0m ')
                elif y == "X":
                    temp.append(' \033[95mX\033[0m ') 
                else:
                    temp.append(str(y))

            # print(f'{x+1} {"|".join(temp)}')
            print(f'{x} {"|".join(temp)}')

            # BUG HERE (logic) Prints an extra line at the end of the board.
            # The for loop runs from 0 and 2 (inclusive), the value of x
            # will never reach the value of len(self.board) ==> 3.
            # Minusing 1 will allow the if statement to be true, and stops
            # the extra line to print.

            # if x != len(self.board): 
            #     print(seperator)

            if x != len(self.board) - 1: 
                print(seperator)


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a symbol.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        if self.board[row][col] == " ":
            return True
        elif self.board[row][col] != " ":
            return False
    
    
    def update(self, row, col, letter):
        '''
        Assigns the letter, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           letter (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''

        # BUG HERE (logic), takes the row and col 1 index less, incorrectly 
        # checks the proper coordinate.

        # Coordinates are already used in terms of python indexes, so the 
        # first column and first row is index (0, 0).

        # if self.squareIsEmpty(row-1,col-1) == True: 
        #     self.board[row][col] = letter       
        #     return True
        # elif self.squareIsEmpty(row-1,col-1) == False:
        #     return False

        if self.squareIsEmpty(row,col) == True: 
            self.board[row][col] = letter       
            return True
        elif self.squareIsEmpty(row,col) == False:
            return False
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        full = True
        for i in range(len(self.board)):
            if " " in self.board[i]:
                full = False
        return full   


    def isWinner(self, playerId):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        has their symbol (X or O). That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''

        # BUG HERE (functional) Doesnt check for diagonal entries for winners and
        # does not correctly account for the index of the player

        # The index of 'O' is 0, the index of 'X' is 1
        # If you try to input player 2 without subracting 1, there will be an
        # index out of bounds errror

        # sym = ['O','X'][playerId]  

        # FIXED
        sym = ['O','X'][playerId - 1]  
        winCon = sym * SIZE
        won = False

        # Horizontal check
        for i in range(len(self.board)):
            if ''.join(self.board[i]) == winCon:
                won = True
        
        # Vertical check
        for j in range(len(self.board[0])):
            if self.board[0][j] + self.board[1][j] + self.board[2][j] == winCon:
                won = True

        # Diagonal check (fixed)
        # Hard coded check, assuming size never changes from 3x3 (also used in vertical check)
        if self.board[0][0] + self.board[1][1] + self.board[2][2] == winCon:
            won = True
        if self.board[2][0] + self.board[1][1] + self.board[0][2] == winCon:
            won = True
        
        return won     


def main():
    #     TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required

    # start by creating empty board and checking the contents of the board attribute
    myBoard = TicTacToe()
    print('Contents of board attribute when object first created:')
    print(myBoard.board)

    # does the empty board display properly?
    myBoard.drawBoard()
    print("\n")
    #YES, THE EMPTY BOARD DISPLAYS PROPERLY

    # assign a number to an empty square and display
    update = myBoard.update(1,2,'X')
    myBoard.drawBoard()
    #### print("\nCan assign to empty: ",update, "\n")
    print("\n",update, "\n")

    # IT ASSIGNS NUMBER TO EMPTY CELL AND RETURNS TRUE

    # try to assign a number to a non-empty square. What happens?
    TryEmptyCell = myBoard.update(1,2,'O')
    myBoard.drawBoard()
    #### print("\nCan assign to non-empty: ",TryEmptyCell,"\n")
    print("\n",TryEmptyCell,"\n")

    # IT DOES NOT ASSIGN THE NUMBER TO NON-EMPTY CELL AND RETURNS 'FALSE'

    myBoard.drawBoard()
    # THE BOARD DOESNT HAVE A WINNER AND NO, THERE CANNOT BE A WINNER AFTER 1 STEP, OT RETURNS 'FALSE'
    # check if the board has a winner. Should there be a winner after only 1 entry?
    #### print(f'Winner after 1 step: {myBoard.isWinner(1)}',"\n")
    print(f'{myBoard.isWinner(1)}',"\n")

    # check if the board is full. Should it be full after only 1 entry?

    #### print("\nBoard full: ",myBoard.boardFull(),"\n")
    print("\n",myBoard.boardFull(),"\n")

    # THE BOARD IS NOT FULL AND NO, IT CANNOT BE FULL AFTER 1 STEP

    myBoard.update(0,0,'O')
    myBoard.update(1,1,'O')
    myBoard.update(2,2,'O')
    myBoard.drawBoard()

    # check if the board has a winner
    #### print("\nBoard has winner: ",myBoard.isWinner(1), "\n")
    print("\n",myBoard.isWinner(1), "\n")
    myBoard.drawBoard()
    print("\n")

    # YES, THE BOARD NOW HAS A WINNER AND IT RETUENS TRUE

    # check if the board is full

    # ADDED VALUES TO FILL THE BOARD
    myBoard.update(1,0,'X')
    myBoard.update(2,0,'O')
    myBoard.update(2,1,'X')
    myBoard.update(0,1,'O')
    myBoard.update(0,2,'X')
    myBoard.drawBoard()
    #### print("\nP1 win:",myBoard.isWinner(1), "Player 1\n")
    #### print("\nP2 win:",myBoard.isWinner(2), "Player 2\n")
    #### print("\nBoard is full: ",myBoard.boardFull(),"\n")

    print("\n",myBoard.isWinner(1), "Player 1\n")
    print("\n",myBoard.isWinner(2), "Player 2\n")
    print("\n",myBoard.boardFull(),"\n")

# main()
