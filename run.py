import random
import re
from termcolor import colored


class Board: 
    """
    Board object to represent the minesweeper game
    i.e "create new board object" or "dig here", or "render this game for this object"
    """
    def __init__(self, dim_size, num_bombs):
        
        """
        Keep track of parameters
        """
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #create the board
        #helper function
        self.board = self.make_new_board() # plant the bomb
        self.assign_values_to_board()

        #initialize a set to keep track of which locations have been dub
        #save (row,col) tuples into this set
        self.dug = set() # ie dig at 0,0, self_dug = {[0,0]}
        self.flagged = set() #keep track of flags locaiton
    
    def make_new_board(self):
        """
        constuct new board based on dim size and num bombs
        using lists of lists.
        """

        #generate new empty board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #plant bombs
        bombs_planted = 0 
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) #this returns a random integer N such that a <= N
            row = loc // self.dim_size # nmber of times dim_size goes in loc
            col = loc  % self.dim_size # remainder to tell what index in that row to look at 

            if board[row][col] == '*':
                # this will mean there is already a bomb planted so keep going
                continue

            board[row][col] = '*' #plant bomb
            bombs_planted += 1
        
        return board

    def assign_values_to_board(self):
        """
        bombs planted, assign number 0-8 for all empty spaces, which represents 
        how many neighboring bombs there are.
        """
        for r in range(self.dim_size):#row index
            for c in range(self.dim_size):#column index
                if self.board[r][c] == '*':
                    #if already a bommmb nothing needs to be calc
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)
    
    def get_num_neighboring_bombs(self, row, col):
        """
        iterate each neighboring position and sum number of bombs
        top left: (row-1, col-1)
        top middle: (row-1, col)
        top right: (row-1, co+1)
        left: (row, col-1)
        right: (row, col+1)
        bottom left (row+1, col-1)
        bottom middle (row+1, col)
        bottm right (row+1, col +1)
        """


        num_neighboring_bombs = 0 
        for r in range(max (0, row-1), min(self.dim_size - 1, row+1)+1):  # for the current row check bellow and above
            for c in range(max (0, col-1), min(self.dim_size - 1, col+1) +1): # for the current collumn check left and right. Min & Max make sure not to go out of bounds!
                if r == row and c == col:
                    #orginal location, no need for check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1 #increments num of neighbouring bombs by 1
        
        return num_neighboring_bombs

    def dig(self, row, col):

        """"
        dig at the location
        Return true if dig is success, false if bomb is hit.

        Possible scenarios
        hit bomb -> game over
        neighboring bombs -> finish dig
        no neighboring bombs -> recursively dig
        """


        self.dug.add((row, col)) #keep track of dig

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0 :
            return True
        
        #self.board[row][col] == 0
        for r in range(max (0, row-1), min(self.dim_size - 1, row+1)+1):
            for c in range(max (0, col-1), min(self.dim_size - 1, col+1) +1):
                if (r,c) in self.dug:
                    continue #don't dig where already dug
                self.dig(r,c)
        
        #first dig doen't hit bomb, shouldn't be able to hit a bomb here
        return True

    def flag(self, row, col):
        """
        If not dug or bomb then is a flag.
        """
        if (row, col) not in self.dug:
            if (row, col) in self.flagged:
                self.flagged.remove((row, col))
                return "Flag removed from ({},{})".format(row, col)
            else:
                self.flagged.add((row, col))
                return "Flag placed at ({},{})".format(row, col)
        return "Cannot place flag on dug location"

    def __str__(self):
        """
        Insured player sees the game board in a formated way that looks similar to 
        minesweeper game.
        """
        # returns a string that shows the board to the player

        # nested loop iterates through each cell in the board, if the (col,row)
        # is in self.dug/flagged, the value is visible to the player, otherwise it is hidden
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.flagged:
                    visible_board[row][col] = 'F'
                elif (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this in a string
        string_rep = ''
        # get max column widths for printing
        #The map function is used to extract each column from visible_board, and the maximum length of the string in each column is calculated.
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        
        # print the csv strings
        #indices_row is a string that represents the column headers (0, 1, 2, ...)
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '\n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i:2d}|'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

# play the game 
def play(dim_size=10, num_bombs=10):
    """
    Step 1: create the board and plant the bombs
    
    Step 2: show the user the board and ask where they want to dig
    Step 3a: if location is a bomb, show game over message
    Step 3b: if location is not a bomb, dig recursively until each sqaure is at least
    next to a bomb
    Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    """

    board = Board(dim_size, num_bombs)
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = input("Where would you like to dig or place a flag? Input as row,col or f row,col for flag (ex: 1,3 or f 1,3): ")
        
        try:
            if user_input.lower().startswith('f'):
                action, coords = user_input.split(None, 1)
                row, col = map(int, re.split(',\\s*', coords.strip()))
                print(board.flag(row, col))
                continue  # Skip the digging part and go to the next iteration
            else:
                row, col = map(int, re.split(',\\s*', user_input.strip()))
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a comma, optionally preceded by 'f' for flag.")
            continue

        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print(f"Invalid location. Enter row and column between 0 and {board.dim_size - 1}.")
            continue

        # Only dig if it's not a flag operation
        if not user_input.lower().startswith('f'):
            safe = board.dig(row, col)
            if not safe:
                break

    if safe:
        print("CONGRATULATIONS!! YOU WON!")
    else:
        print("SORRY, GAME OVER :(")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()
