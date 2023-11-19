import tkinter as tk
from tkinter import messagebox
import random

def print_board(board):
    for row in board:
        print(row)

def is_valid_move(board, row, col, num):
    # Check if the number is not repeated in the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if the number is not repeated in the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if the number is not repeated in the 3x3 subgrid
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):  # Try all numbers from 1 to 9
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Reset if the move did not lead to a solution

    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # Assuming 0 represents an empty cell
                return (i, j)
    return None

def fill_board(board):
    numbers = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                random.shuffle(numbers)
                for number in numbers:
                    if is_valid_move(board, i, j, number):
                        board[i][j] = number
                        if check_board_full(board) or fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def check_board_full(board):
    for row in board:
        for num in row:
            if num == 0:
                return False
    return True

def remove_numbers_from_board(board, num_to_remove):
    while num_to_remove > 0:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if board[i][j] != 0:
            board[i][j] = 0
            num_to_remove -= 1

def generate_sudoku(difficulty='medium'):
    base_board = [[0] * 9 for _ in range(9)]
    fill_board(base_board)
    num_to_remove = {
        'easy': 36,
        'medium': 45,
        'hard': 54
    }.get(difficulty, 45)
    remove_numbers_from_board(base_board, num_to_remove)
    return base_board

# GUI functions
def get_board_from_gui():
    board = []
    for row in rows:
        current_row = []
        for entry in row:
            if entry.get() == '':
                current_row.append(0)
            else:
                current_row.append(int(entry.get()))
        board.append(current_row)
    return board

def display_solved_board(board):
    for i in range(9):
        for j in range(9):
            rows[i][j].delete(0, tk.END)
            rows[i][j].insert(0, board[i][j])

def animate_solving(board, row, col, num):
    if num == 0:
        rows[row][col].delete(0, tk.END)
        rows[row][col].config(fg='black')  # Reset to default color
    else:
        rows[row][col].delete(0, tk.END)
        rows[row][col].insert(0, num)
        rows[row][col].config(fg='blue')  # Change color to show this is a computer move
    root.update()
    root.after(50)  # Delay in milliseconds for the animation effect

def solve_sudoku_gui(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):  # Try all numbers from 1 to 9
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            animate_solving(board, row, col, num)  # Animate the insertion
            if solve_sudoku_gui(board):
                return True
            board[row][col] = 0
            animate_solving(board, row, col, 0)  # Animate the removal

    return False

def solve_from_gui():
    board = get_board_from_gui()
    if solve_sudoku_gui(board):
        display_solved_board(board)
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists for the given Sudoku puzzle.")

def generate_and_display_puzzle(difficulty='medium'):
    puzzle = generate_sudoku(difficulty)
    for i in range(9):
        for j in range(9):
            rows[i][j].delete(0, tk.END)
            if puzzle[i][j] != 0:
                rows[i][j].insert(0, puzzle[i][j])

# Tkinter GUI setup
root = tk.Tk()
root.title("Sudoku Solver")

rows = []
for i in range(9):
    cols = []
    for j in range(9):
        e = tk.Entry(root, width=2, font=('Arial', 22), justify='center')
        e.grid(row=i, column=j)
        cols.append(e)
    rows.append(cols)

solve_button = tk.Button(root, text='Solve', command=solve_from_gui)
solve_button.grid(row=9, column=0, columnspan=9)

# Add the generate puzzle button with the correct function binding
generate_button = tk.Button(root, text='Generate Puzzle', command=lambda: generate_and_display_puzzle('medium'))
generate_button.grid(row=10, column=0, columnspan=9)

root.mainloop()