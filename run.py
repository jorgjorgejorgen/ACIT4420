# candidate: 119


from solver import *
import numpy as np


# Test board. Use this to test different sudoku puzzles.
# This example is the Miracle sudoku.
#sudoku = [
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 1, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 2, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0],
#[0, 0, 0, 0, 0, 0, 0, 0, 0]]


# Creates the grid for the sudoku
# User enter 9 rows of digits

sudoku = []

print("Enter your sudoku by rows. Include 0 for missing numbers\n")
while True:
    row = list(input('Row --> '))
    ints = []

    for number in row:
        ints.append(int(number))
    sudoku.append(ints)
    if len(sudoku) == 9:
        break
    print("Enter next row")


print("\nThis is the sudoku you provided:\n")
# Prints the unsolved sudoku provided by user
print(np.matrix(sudoku))

# While loops to apply the special rule. User enters y or n.
while True:
    possible.knight_cons = str(input("\nIs the ANTI-KNIGHT constraint applicable? y/n: "))
    if possible.knight_cons == 'y' or possible.knight_cons == 'n':
        break
    else:
        print("Please provide an answer for the anti-knight rule: 'y' for yes or 'n' for no")
while True:
    possible.king_cons = str(input("Is the ANTI-KING constraint applicable? y/n: "))
    if possible.king_cons == 'y' or possible.king_cons == 'n':
        break
    else:
        print("Please provide an answer for the anti-king rule: 'y' for yes or 'n' for no")
while True:
    possible.consecutive_cons = str(input("Is the NON-CONSECUTIVE constraint applicable? y/n: "))
    if possible.consecutive_cons == 'y' or possible.consecutive_cons == 'n':
        break
    else:
        print("\nPlease provide an answer for the non-consecutive rule: 'y' for yes or 'n' for no")

# Calling the solver from solve.py.The sudoku is solved and printed
while solver(sudoku, possible.knight_cons, possible.king_cons, possible.consecutive_cons) is True:
    print(np.matrix(sudoku))
else:
    print("\nNo solution found")








