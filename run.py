#Board object to represent the minesweeper game
# i.e "create new board object" or "dig here", or "render this game for this object"
class Board: 
    def __init__(self, dim_size, num_bombs):
        #Keep track of parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #Let's create the board
        #helper function
        self.board = self.make_new_board() # plant the bomb

        #initialize a set to keep track of which locations have been dub
        #save (row,col) tuples into this set
        self.dug = set() # ie dig at 0,0, self_dug = {[0,0]}
    
    def make_new_board(self):
        #constuct new board based on dim size and num bombs
        #using lists of lists

        #generate new board
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
        #bombs planted, assign number 0-8 for all empty spaces, which represents 
        #how many neighboring bombs there are. Precompute in order to save time
        #checking whats around the board later.
        for r in range(self.dim_size):#row index
            for c in range(self.dim_size):#column index
                if self.board[r][c] == '*':
                    #if already a bommmb nothing needs to be calc
                    continue
                self.board[r] = self.get_num_neighboring_bombs(r,c) 

    def get_num_neighboring_bombs(self, row, col):
        #iterate each neighboring position and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, co+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left (row+1, col-1)
        # bottom middle (row+1, col)
        # bottm right (row+1, col +1)

        num_neighboring_bombs = 0 
        for r in range(max (0, row-1), min(self.dim_size - 1, row+1)+1):  # for the current row check bellow and above
            for c in range(max (0, col-1), min(self.dim_size - 1, row+1) +1): # for the current collumn check left and right. Min & Max make sure not to go out of bounds!
                if r == row and c == col:
                    #orginal location, no need for check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1 #increments num of neighbouring bombs by 1
        
        return num_neighboring_bombs

# play the game 
def play(dim_size=10, num_bombs=10)
    #Step 1: create the board and plant the bombs
    #Step 2: show the user the board and ask where they want to dig
    #Step 3a: if location is a bomb, show game over message
    #Step 3b: if location is not a bomb, dig recursively until each sqaure is at least
    #         next to a bomb
    #Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    pass
