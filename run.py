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

# play the game 
def play(dim_size=10, num_bombs=10)
    #Step 1: create the board and plant the bombs
    #Step 2: show the user the board and ask where they want to dig
    #Step 3a: if location is a bomb, show game over message
    #Step 3b: if location is not a bomb, dig recursively until each sqaure is at least
    #         next to a bomb
    #Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    pass
