# Define the Sudoku board as a 2D list (9x9 grid)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Function to print the Sudoku board for better visualization
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Function to find an empty cell (a cell with a value of 0) in the Sudoku board
def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

# Function to check if a number can be placed in a certain cell according to Sudoku rules
def is_valid_move(board, row, col, num):
    # Check the row
    if num in board[row]:
        return False

    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# Recursive function to solve the Sudoku puzzle using backtracking
def solve_sudoku(board):
    row, col = find_empty_cell(board)

    # Base case: if there are no empty cells, the puzzle is solved
    if row is None:
        return True

    # Try placing numbers from 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            # Place the number if it's valid
            board[row][col] = num

            # Recur to solve the rest of the puzzle
            if solve_sudoku(board):
                return True

            # If placing the number leads to an invalid solution, backtrack
            board[row][col] = 0

    # No number can be placed, need to backtrack
    return False

# Call the solve_sudoku function and print the solved Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("Solved Sudoku Puzzle:")
    print_board(sudoku_board)
else:
    print("No solution exists for the given Sudoku puzzle.")
