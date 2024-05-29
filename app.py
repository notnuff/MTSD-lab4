from flask import Flask, render_template, request
import numpy as np
import random

app = Flask(__name__)

def is_valid(board, row, col, num):
    for j in range(9):
        if board[row, j] == num and col != j:
            return False

    for i in range(9):
        if board[i, col] == num and row != i:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i, j] == num and (i, j) != (row, col):
                return False

    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i, j] == 0:
                return (i, j)
    return None

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row, col] = num
            if solve_sudoku(board):
                return True
            board[row, col] = 0
    return False

def generate_sudoku():
    board = np.zeros((9, 9), dtype=int)
    for _ in range(17): 
        num = random.randint(1, 9)
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row, col] != 0 or not is_valid(board, row, col, num):
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row, col] = num
    solve_sudoku(board)
    return board