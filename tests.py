import unittest
import Sudoku

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

class TestGetters(unittest.TestCase):
    
    def test_row(self):
        self.assertEqual(Sudoku.get_row([2,0], sudoku_puzzle), row3)
        
    def test_column(self):
        column3 = [0,1,2,6,0,0,5,0,0]
        self.assertEqual(Sudoku.get_column([0,2], sudoku_puzzle), column3)
        
    def test_block(self):
        block3 = [0,9,0,6,0,0,3,0,0]
        self.assertEqual(Sudoku.get_block([8,0], sudoku_puzzle), block3 )

if __name__ == '__main__':
    unittest.main()