# candidate: 119

# -pip install numpy

import numpy as np

# Function for defining the constrains of sudoku puzzles
def possible(sudoku, x, y, n, knight_cons, king_cons,consecutive_cons):
    # column check
    for i in range(0, 9):
        if sudoku[i][x] == n:
            return False
    # line check
    for i in range(0, 9):
        if sudoku[y][i] == n:
            return False
    # box check
    x_start = (x // 3)*3
    y_start = (y // 3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[i + y_start][j + x_start] == n:
                return False

    # checking 8 knight moves
    if knight_cons == "y":
        for i in (x - 2, x + 2):
            for j in (y - 1, y + 1):
                if 9 > i >= 0 and 9 > j >= 0 and i != x and j != y:
                    if sudoku[j][i] == n:
                        return False
        # remaining 4 moves
        for i in (x - 1, x + 1):
            for j in (y - 2, y + 2):
                if 9 > i >= 0 and 9 > j >= 0 and i != x and j != y:
                    if sudoku[j][i] == n:
                        return False

    # checking king move diagonally from cell
    if king_cons == "y":
        for i in (x - 1, x + 1):
            for j in (y - 1, y + 1):
                if 9 > i >= 0 and 9 > j >= 0 and i != x and j != y:
                    if sudoku[j][i] == n:
                        return False

    # checking non-consecutive
    if consecutive_cons == 'y':
        for i in (x - 1, x + 1):
            for j in (y, y):
                if 9 > i >= 0 and 9 > j >= 0:
                    if n == 1:
                        continue
                    if sudoku[j][i] == n + 1 or sudoku[j][i] == n - 1:
                        return False
        for i in (x, x):
            for j in (y - 1, y + 1):
                if 9 > i >= 0 and 9 > j >= 0:
                    if n == 1:
                        continue
                    if sudoku[j][i] == n + 1 or sudoku[j][i] == n -1:
                        return False


    return True

# function for solving the sudoku
def solver(sudoku, knight_cons, king_cons, consecutive_cons):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1, 10):
                    if possible(sudoku, x, y, n, knight_cons, king_cons,consecutive_cons):
                        sudoku[y][x] = n
                        solver(sudoku, knight_cons, king_cons, consecutive_cons)
                        sudoku[y][x] = 0
                return False
    print("\n\nSolution found:")
    print(np.matrix(sudoku))
    input("\nCheck for more solutions?")
    # return the solved sudoku


