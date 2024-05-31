from flask import Blueprint, render_template, request
import numpy as np
from .sudoku import generate_sudoku, remove_numbers, solve_sudoku

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        difficulty = request.form["difficulty"]
        sudoku_board = generate_sudoku()
        sudoku_board = remove_numbers(sudoku_board, difficulty)
        return render_template("index.html", board=sudoku_board.tolist(), solved_board=None)
    return render_template("index.html", board=None, solved_board=None)

@routes.route("/solve", methods=["POST"])
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

@routes.route("/custom", methods=["GET", "POST"])
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