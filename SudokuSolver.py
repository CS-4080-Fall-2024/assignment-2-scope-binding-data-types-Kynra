
def solve_sudoku(board):
    empty_cell = find_empty(board)

    if not empty_cell:
        return True
    
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num 

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def is_valid(board, num, row, col):
    for i in range(9):
        if board[row][i] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for i in range(box_row_start, box_row_start + 3):
        for j in range(box_col_start, box_col_start + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(board[i][j], end=" ")
        print()

board = [
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

print("Original Sudoku Board:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku Board:")
    print_board(board)
else:
    print("No solution exists.")