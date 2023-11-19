# Sudoku Solver and Generator

This Python application solves Sudoku puzzles using a backtracking algorithm and generates new puzzles with varying levels of difficulty. It also features a graphical user interface (GUI) for interactive puzzle solving and generation.

## Features

- **Sudoku Solver:** Solves any given Sudoku puzzle using a recursive backtracking algorithm, which efficiently fills the puzzle by trying out possible solutions and backtracking as necessary.
- **Sudoku Puzzle Generator:** Creates random, solvable Sudoku puzzles with three difficulty settings: easy, medium, and hard. The generator fills a board with a complete solution and then strategically removes numbers to craft a puzzle.
- **Interactive GUI:** A user-friendly Tkinter-based GUI where users can input their puzzles, click to solve them, and visually see the puzzle being solved in real-time. Users can also generate new puzzles to play with.

## How to Use

To use the application, run the `sudoku_app.py` file in a Python 3 environment. The GUI window will appear with a blank Sudoku grid.

### Solving a Puzzle

1. Enter the numbers of your Sudoku puzzle into the grid.
2. Click the 'Solve' button to start the solving process.
3. Watch as the algorithm animates the solving process, filling in the grid with the correct numbers.

### Generating a Puzzle

1. Click the 'Generate Puzzle' button to create a new puzzle.
2. Choose the difficulty level by modifying the code (default is medium).
3. The new puzzle will appear on the grid, ready to be solved.

## Technical Details

- **Language:** Python 3
- **Libraries:** Tkinter for the GUI, random for puzzle generation
- **Algorithms:** Backtracking for puzzle solving, randomization for puzzle generation
- **GUI:** Tkinter-based with buttons and entry widgets for interaction

## Requirements

- Python 3.6 or higher
- Tkinter library (usually comes with Python)

## Installation

No installation is needed. Just ensure you have Python 3 installed on your system.

## Running the Application

Execute the script from the command line:

```bash
python sudoku_app.py
