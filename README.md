# CS50P-Final-Project
# Sudoku Solver
#### Video Demo: https://www.youtube.com/watch?v=LTUX93lsRLo
#### Description:
My project is a Sudoku Solver implemented in Python. The goal of the project is to develop a program capable of solving Sudoku puzzles of varying difficulty levels using a backtracking algorithm.

The solver takes the incomplete Sudoku grid as input and fills in the missing cells while respecting the Sudoku rules, ensuring that no numbers repeat within a row, column, or 3x3 sub-grid.


The main file in my project is named project.py.This file contains the implementation of the Sudoku-solving algorithm. It includes functions such as **is_valid**, which checks whether a number's position is valid within a given row, column, or 3x3 subgrid; **find_empty**, finds the next empty cell in the Sudoku grid, and **solve**, which solves Sudoku puzzles recursively by backtracking. The function **display_board** is also defined in this file to display the solved Sudoku grid.


The program accepts a 9x9 grid represented as a 2D list, where empty cells are represented by the value 0. It traverses the grid, trying to place the numbers 1 through 9 in the empty cells while still ensuring that the location is valid. If setting a number results in a conflict, it will go back and try another number until a solution is found.


Throughout the project's development, I - myself debated certain design choices to optimize the efficiency and readability of the solver. An important decision is the choice of a backtracking algorithm for solving Sudoku puzzles. I chose backtracking because of its simplicity and effectiveness in exploring possible solutions without having to explore all possibilities exhaustively. Backtracking allows a program to return from its current state if it hits a dead end, thereby significantly reducing the number of iterations needed to solve the puzzle compared to brute force approaches.


Another design choice I considered was a data structure to represent the Sudoku grid. I decided to use a 2D list to represent the grid because it provides a simple and intuitive representation of the Sudoku board. Additionally, using lists allows for easy indexing and manipulation of cells during the solving process.


I also thought about the naming convention and organization of functions in the project.py file to ensure clarity and maintainability. I've chosen descriptive feature names to clearly demonstrate their purpose and function. Additionally, I've organized features logically, grouped related features together, and used comments to document their purpose and usage.


In summary, my Sudoku Solver project is a Python program designed to solve Sudoku puzzles efficiently using a backtracking algorithm. The program consists of a main single file, project.py, which contains the solution algorithm implementation and related helper functions. Through thoughtful design choices and careful consideration of algorithmic efficiency and code readability, I have created a fully function and efficient Sudoku Solver, capable of solving puzzles. There are different levels of difficulty.

*Thanks for reading my description.*
