#This file will contain all the individual checks that the program requires: Block, Horizontal Line, Vertical Line
SUDOKU_SIZE = 9;
#This function will take in a row and return the missing values in that row as a list
def check_horizontal(row, possibilities):
    
    
    for num in possibilities:
        for val in row:
            if val == num:
                possibilities.remove(num);
                
                
    return possibilities;


''' 
The below functions will retrieve the column, block and row based on the index on the index that is being checked.

    
def get_row(index, puzzle):

def get_block(index, puzzle): 

'''


def get_column(index, puzzle):
    values = []
    for val in range(SUDOKU_SIZE):
        values.append(puzzle[val][index[1]])
    return values

def get_row(index, puzzle):
    values = []
    for val in range(SUDOKU_SIZE):
        values.append(puzzle[index[0]][val])
    return values

'''
    get_block takes in index that represents the coordinates of the value and the puzzle
    and returns a list of values in that block
    A block refers to a 3x3 area of numbers whose top left values are
    [0,0] [0,3] [0,6] [3,0] [3,3] [3,6] [6,0] [6,3] [6,6]
    See any 9x9 sudoku puzzle for a more clear picture.
'''
def  get_block(index, puzzle):
    values = []
    block_column = index[0] // 3
    block_row = index[1] // 3
    for x in range(3):
        for y in range(3):
            y_coord = y + (block_column * 3)
            x_coord = x + (block_row * 3)
            values.append(puzzle[x_coord][y_coord])
            
    return values
            

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

print(get_column([0,0], sudoku_puzzle))
print(get_row([0,0], sudoku_puzzle))
print(get_block([0,0], sudoku_puzzle))