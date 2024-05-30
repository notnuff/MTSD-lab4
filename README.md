# Sudoku Web Application


## Description
This Python web application allows users to generate and solve Sudoku puzzles. It is built using the Flask framework and supports generating puzzles of varying difficulties as well as solving custom puzzles inputted by users.

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- NumPy

### Installation
1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/notnuff/MTSD-lab4
   ```

2. Navigate to the project directory:
   ```sh
   cd sudoku-web-app
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application
To run the application, execute the following command:
```sh
python app.py
```

The application will start on `http://127.0.0.1:5000/`. Open this URL in your web browser to use the application.

### Running Tests
To run the tests for this application, navigate to the project directory and execute:
```sh
python -m unittest discover -s tests
```

This will discover and run all the test cases present in the `tests` directory.

## User Guide

### Generating Sudoku
1. Open the application in your web browser.
2. Choose the difficulty level from the dropdown menu (Easy, Medium, Hard).
3. Click the "Generate" button to create a new Sudoku puzzle.

### Solving Sudoku
1. Enter the numbers into the empty cells of the Sudoku grid.
2. Click the "Solve" button to get the solution for the Sudoku puzzle.

### Creating Custom Sudoku
1. Click on the "Create Custom Sudoku" button on the main page.
2. Fill in the numbers for your custom Sudoku puzzle.
3. Click the "Resolve" button to solve your custom Sudoku puzzle.

## Project Structure

```plaintext
sudoku-web-app/
├── templates/
│   ├── custom.html
│   └── index.html
├── tests/
│   ├── __init__.py
│   ├── test_flask_routes.py
│   ├── test_sudoku_generation.py
│   └── test_sudoku_logic.py
├── app.py
└── requirements.txt
```

- **app.py**: The main application file containing the Flask routes and logic for generating and solving Sudoku puzzles.
- **templates/**: Contains HTML templates for rendering the web pages.
  - **index.html**: Template for the main Sudoku page.
  - **custom.html**: Template for creating and solving custom Sudoku puzzles.
- **tests/**: Contains unit tests for the application.
  - **test_flask_routes.py**: Tests for Flask routes.
  - **test_sudoku_generation.py**: Tests for Sudoku generation functions.
  - **test_sudoku_logic.py**: Tests for Sudoku solving logic.
- **requirements.txt**: List of Python packages required for the project.
