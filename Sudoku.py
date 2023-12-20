"""
    Sudoku.py
    Author: Joaquin Lemus
    Date: 18-Nov-2023
"""

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
    ]

def print_sudoku(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            print(board[x][y], end=" ")
        print()

def check_row(number, row, board):
    for col in range(len(board)):
        if board[row][col] == number: 
            return False
    return True

    
def check_column(number, col, board):
    for row in range(len(board)):
        if board[row][col] == number: 
            return False
    return True

def check_box(number, row, col, board):
    row = row - (row - (3 * (row // 3)))
    col = col - (col - (3 * (col // 3)))
    for x in range(row, row+3):
        for y in range(col, col+3):
            if board[x][y] == number:
                return False
    return True

def is_safe(number, row, col, board):
    if check_row(number, row, board) and check_column(number, col, board) and check_box(number, row, col, board):
        return True
    return False

def empty_spaces(board):
    empty = []
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                empty.append((x,y))
    return empty

def solve(board):
    empty = empty_spaces(board)
    # Check if there are no empty spaces
    if not empty:
        return True # NO empty spaces left
    row, col = empty[0]
    for i in range(1, 10):
        if is_safe(i, row, col, board):
            board[row][col] = i
            finished = solve(board)
            if finished:
                return True # Sudoku is solved
            board[row][col] = 0 # Backtrack
    return False

def main():
    print("Original Sudoku:")
    print_sudoku(board)
    print()

    solve(board)

    if not solve(board):
        print("No Solution")
    else:
        print("\nSolved Sudoku:")
        print_sudoku(board)

if __name__ == "__main__":
    main()