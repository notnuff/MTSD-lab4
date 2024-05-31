import unittest
import numpy as np
from app import is_valid, find_empty, solve_sudoku

class SudokuLogicTestCase(unittest.TestCase):

    def test_is_valid(self):
        board = np.zeros((9, 9), dtype=int)

        board[1, 1] = 5
        self.assertFalse(is_valid(board, 0, 1, 5), "Number 5 is already in the column 1")
        self.assertFalse(is_valid(board, 1, 0, 5), "Number 5 is already in the row 1")
        self.assertFalse(is_valid(board, 2, 2, 5), "Number 5 is already in the 3x3 grid starting at (0, 0)")

    def test_find_empty(self):
        board = np.zeros((9, 9), dtype=int)
        self.assertEqual(find_empty(board), (0, 0))
        board[0, 0] = 5
        self.assertEqual(find_empty(board), (0, 1))
        board[0, :] = 5
        self.assertEqual(find_empty(board), (1, 0))

    def test_solve_sudoku(self):
        board = np.array([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ])
        self.assertTrue(solve_sudoku(board))
        self.assertTrue(all(board[i, j] != 0 for i in range(9) for j in range(9)), "All cells should be filled")
        
        # Перевіряємо, чи розв'язана судоку дотримується правил
        for row in range(9):
            for col in range(9):
                num = board[row, col]
                self.assertTrue(is_valid(board, row, col, num), f"Number {num} is correctly placed at ({row}, {col})")

if __name__ == '__main__':
    unittest.main()
