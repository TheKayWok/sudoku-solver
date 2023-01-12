#This file will contain all the individual checks that the program requires: Block, Horizontal Line, Vertical Line
'''
The variables below contain "constants" that are never meant to change.
SUDOKU_SIZE represents the dimensions of the Sucoku puzzle
BLOCK_SIZE represents the dimensions of the internal blocks of the puzzle
'''
SUDOKU_SIZE = 9;
BLOCK_SIZE = 3
#This function will take in a row and return the missing values in that row as a list
def check_horizontal(row, possibilities):
    
    
    for num in possibilities:
        for val in row:
            if val == num:
                possibilities.remove(num);
                
                
    return possibilities;


''' 
The below functions will retrieve the column, block and row based on the index on the index that is being checked.

the index that is input will be in the form of [x,y] where x represents the the row value counting from the top starting at 0
and y represents the column counting from the left as usual and starting at 0
'''


def get_column(index, puzzle):
    values = set()
    for val in range(SUDOKU_SIZE):
        values.add(puzzle[val][index[1]])
    return values

def get_row(index, puzzle):
    values = set()
    for val in range(SUDOKU_SIZE):
        values.add(puzzle[index[0]][val])
    return values

'''
    get_block takes in index that represents the coordinates of the value and the puzzle
    and returns a list of values in that block
    A block refers to a 3x3 area of numbers whose top left values are
    [0,0] [0,3] [0,6] [3,0] [3,3] [3,6] [6,0] [6,3] [6,6]
    See any 9x9 sudoku puzzle for a more clear picture.
'''
def  get_block(index, puzzle):
    values = set()
    block_column = index[0] // BLOCK_SIZE
    block_row = index[1] // BLOCK_SIZE
    for x in range(BLOCK_SIZE):
        for y in range(BLOCK_SIZE):
            y_coord = y + (block_column * BLOCK_SIZE)
            x_coord = x + (block_row * BLOCK_SIZE)
            values.add(puzzle[y_coord][x_coord])
            
    return values
            
'''
    find_possibilities will take in an index and a puzzle and will return a set of possible solutions for the square
    if there is only one possibility for the square, it will assign that value to the index given of the puzzle
'''
def find_possibilities(index, puzzle):
    possibilities = {1,2,3,4,5,6,7,8,9}
    taken_values = set.union(get_block(index, puzzle)).union(get_row(index, puzzle)).union(get_column(index, puzzle))
    possibilities -= taken_values
    if (len(possibilities) == 1):
        puzzle[index[0]][index[1]] = list(possibilities)[0]
        
    return possibilities

'''
    print_puzzle is a function that is used to print the puzzle in a more user friendly way for debugging purposes.
'''
def print_puzzle(puzzle):
    for row in puzzle:
        print(row)

def get_empty_spaces(puzzle):
    empty_spaces = []
    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):
            if(puzzle[x][y] == 0):
                empty_spaces.append([x,y])
                
    return empty_spaces
    
    
def solve_puzzle(puzzle):
    empty_spaces = get_empty_spaces(puzzle)
    count = 0
    while(len(empty_spaces) > 0):
        
        print(++count)
        for space in empty_spaces:
            
            if len(find_possibilities(space, puzzle)) == 1:
                print(space)
                empty_spaces.remove(space)
                
                print_puzzle(sudoku_puzzle)
                print("____________________________________")
            
                 


#Sample Sudoku Below
#https://sudoku9x9.com/?level=1 L1: #547263085
row1 = [7, 5, 0, 0, 8, 0, 0, 9, 0]
row2 = [0, 0, 1, 2, 0, 4, 6, 0, 0]
row3 = [0, 8, 2, 9, 1, 0, 3, 0, 0]
row4 = [0, 0, 6, 0, 9, 7, 4, 1, 0]
row5 = [4, 7, 0, 0, 0, 3, 5, 0, 0]
row6 = [0, 3, 0, 5, 0, 2, 0, 8, 6]
row7 = [9, 0, 5, 0, 3, 0, 1, 0, 2]
row8 = [8, 4, 0, 6, 0, 0, 0, 0, 5]
row9 = [2, 0, 0, 4, 0, 9, 0, 0, 7]

sudoku_puzzle = [row1, row2, row3, row4, row5, row6, row7, row8, row9]

print_puzzle(sudoku_puzzle)
print("________________________________________")
print(solve_puzzle(sudoku_puzzle))
print("________________________________________")
print_puzzle(sudoku_puzzle)