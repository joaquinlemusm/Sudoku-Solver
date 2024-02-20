# Sudoku Solver
The Sudoku.py script is a simple Sudoku solver written in Python. It solves a given Sudoku puzzle using the backtracking algorithm.

## Usage
1. Clone the repository containing Sudoku.py to your local machine:
```
git clone https://github.com/tuusuario/SudokuSolver.git
```
2. Run the script using Python:
```
python Sudoku.py
```

## Description
- The script initializes a Sudoku board with a 9x9 grid containing numbers from 1 to 9 and zeros representing empty cells.

- It provides functions to check whether a number is safe to place in a given row, column, or 3x3 subgrid.

- The main solving algorithm uses backtracking to recursively fill in the empty cells while ensuring the Sudoku constraints are satisfied.

- Once the puzzle is solved, the script prints the original Sudoku board and the solved Sudoku board.

## Future Implementation: Computer Vision
As a future enhancement, the Sudoku solver could be integrated with computer vision techniques. This would allow the script to solve Sudoku puzzles by analyzing images of printed or handwritten Sudoku grids. By using image processing and optical character recognition (OCR), the solver could extract the puzzle from an image and then apply the solving algorithm.

## File Structure
Sudoku.py: Main Python script containing the Sudoku solver implementation.
## Author
Author: Joaquín Lemus
Date: 18-Nov-2023
