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

def remove_numbers(board, level):
    if level == 'easy':
        squares_to_remove = 40
    elif level == 'medium':
        squares_to_remove = 50
    else:
        squares_to_remove = 60

    all_cells = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(all_cells)
    for i in range(squares_to_remove):
        row, col = all_cells[i]
        board[row, col] = 0

    return board

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        difficulty = request.form["difficulty"]
        sudoku_board = generate_sudoku()
        sudoku_board = remove_numbers(sudoku_board, difficulty)
        return render_template("index.html", board=sudoku_board.tolist(), solved_board=None)
    return render_template("index.html", board=None, solved_board=None)

@app.route("/solve", methods=["POST"])
def solve():
    board = np.zeros((9, 9), dtype=int)
    for i in range(9):
        for j in range(9):
            cell_value = request.form.get(f"cell-{i}-{j}")
            if cell_value and cell_value.isdigit():
                board[i, j] = int(cell_value)
    
    solved_board = board.copy()
    if solve_sudoku(solved_board):
        return render_template("index.html", board=board.tolist(), solved_board=solved_board.tolist())
    else:
        return render_template("index.html", board=board.tolist(), solved_board=None, error="This Sudoku puzzle cannot be solved.")

@app.route("/custom", methods=["GET", "POST"])
def custom():
    if request.method == "POST":
        board = np.zeros((9, 9), dtype=int)
        original_board = np.zeros((9, 9), dtype=int)
        for i in range(9):
            for j in range(9):
                cell_value = request.form.get(f"cell-{i}-{j}")
                if cell_value and cell_value.isdigit():
                    board[i, j] = int(cell_value)
                    original_board[i, j] = int(cell_value)
        
        if "check" in request.form:
            if solve_sudoku(board.copy()):
                if np.array_equal(board, original_board):
                    return render_template("custom.html", board=board.tolist(), solved_board=None, message="Sudoku is correct!")
                else:
                    return render_template("custom.html", board=board.tolist(), solved_board=None, error="Sudoku is incorrect.")
            else:
                return render_template("custom.html", board=board.tolist(), solved_board=None, error="This Sudoku puzzle cannot be solved.")

        if "solve" in request.form:
            solved_board = original_board.copy()
            if solve_sudoku(solved_board):
                return render_template("custom.html", board=original_board.tolist(), solved_board=solved_board.tolist())
            else:
                return render_template("custom.html", board=original_board.tolist(), solved_board=None, error="This Sudoku puzzle cannot be solved.")
        
        return render_template("custom.html", board=board.tolist())
    return render_template("custom.html", board=[[0]*9 for _ in range(9)])

if __name__ == "__main__":
    app.run(debug=True)