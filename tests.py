import unittest
import Sudoku
import copy

#Sample Sudoku Below
#https://sudoku9x9.com/?level=1 L1: #547263085
#       0  1  2  3  4  5  6  7  8
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

class TestGetters(unittest.TestCase):
    
    def test_row(self):
        self.assertEqual(Sudoku.get_row([2,0], copy.deepcopy(sudoku_puzzle)), set(row3))
        
    def test_column(self):
        column3 = {0,1,2,6,0,0,5,0,0}
        self.assertEqual(Sudoku.get_column([0,2], copy.deepcopy(sudoku_puzzle)), column3)
        
    def test_block(self):
        block3 = {9,0,5,8,4,0,2,0,0}
        self.assertEqual(Sudoku.get_block([8,0], copy.deepcopy(sudoku_puzzle)), block3 )
    
    def test_find_possibilities(self):
        internal_puzzle = copy.deepcopy(sudoku_puzzle)
        self.assertEqual(Sudoku.find_possibilities([0,3], internal_puzzle), {3})
        Sudoku.find_possibilities([1,0], internal_puzzle)
        self.assertEqual(internal_puzzle[1][0], 3)
        
    #7,5,8,9,
    def test_get_empty_spaces(self):
        
        solution = [
            [0,2],[0,3],[0,5],[0,6],[0,8],
            [1,0],[1,1],[1,4],[1,7],[1,8],
            [2,0],[2,5],[2,7],[2,8],
            [3,0],[3,1],[3,3],[3,8],
            [4,2],[4,3],[4,4],[4,7],[4,8],
            [5,0],[5,2],[5,4],[5,6],
            [6,1],[6,3],[6,5],[6,7],
            [7,2],[7,4],[7,5],[7,6],[7,7],
            [8,1],[8,2],[8,4],[8,6],[8,7]
        ]
        internal_puzzle = copy.deepcopy(sudoku_puzzle)
        self.assertEqual(Sudoku.get_empty_spaces(internal_puzzle), solution)
        
    def test_solved(self):
        solved_puzzle = [[7,5,4,3,8,6,2,9,1],
                         [3,9,1,2,7,4,6,5,8],
                         [6,8,2,9,1,5,3,7,4],
                         [5,2,6,8,9,7,4,1,3],
                         [4,7,8,1,6,3,5,2,9],
                         [1,3,9,5,4,2,7,8,6],
                         [9,6,5,7,3,8,1,4,2],
                         [8,4,7,6,2,1,9,3,5],
                         [2,1,3,4,5,9,8,6,7]
                         ]
        Sudoku.solve_puzzle(sudoku_puzzle)
        self.assertEqual(sudoku_puzzle, solved_puzzle)

if __name__ == '__main__':
    unittest.main()
    