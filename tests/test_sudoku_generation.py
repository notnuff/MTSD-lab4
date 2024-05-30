import unittest
import numpy as np
from app import generate_sudoku, remove_numbers

class SudokuGenerationTestCase(unittest.TestCase):

    def test_generate_sudoku(self):
        board = generate_sudoku()
        self.assertEqual(board.shape, (9, 9))

    def test_remove_numbers(self):
        board = generate_sudoku()
        board_with_holes = remove_numbers(board.copy(), 'easy')
        self.assertTrue((board_with_holes == 0).sum() >= 40)

if __name__ == '__main__':
    unittest.main()
