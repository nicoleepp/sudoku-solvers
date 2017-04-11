from propagation_forwardtracking_with_lookahead import (
    solve as lookahead_solver
)
from backtracking import sudokuSolver as backtracking_solver
from utils import print_sudoku_puzzle, validate_sudoku_solution

import time

'''[# Designed to work against the brute-force algorithm:
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 8, 5],
    [0, 0, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 1, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 0, 0, 7, 3],
    [0, 0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 9]
]'''

puzzles = [
    [
        [5, 1, 7, 6, 0, 0, 0, 3, 4],
        [2, 8, 9, 0, 0, 4, 0, 0, 0],
        [3, 4, 6, 2, 0, 5, 0, 9, 0],
        [6, 0, 2, 0, 0, 0, 0, 1, 0],
        [0, 3, 8, 0, 0, 6, 0, 4, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 7, 8],
        [7, 0, 3, 4, 0, 0, 5, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [1, 0, 4, 0, 6, 8, 0, 0, 5],
        [9, 6, 0, 0, 7, 0, 4, 0, 3],
        [0, 3, 0, 9, 0, 4, 1, 6, 0],
        [0, 0, 0, 6, 0, 2, 5, 7, 1],
        [6, 8, 1, 0, 0, 5, 0, 4, 0],
        [0, 2, 5, 1, 0, 9, 0, 3, 0],
        [0, 0, 6, 8, 5, 3, 0, 0, 4],
        [4, 1, 0, 0, 9, 0, 3, 0, 8],
        [8, 0, 3, 0, 1, 0, 6, 9, 0]
    ],
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],
    [
        [1, 0, 4, 0, 6, 8, 0, 0, 5],
        [9, 6, 0, 0, 7, 0, 4, 0, 3],
        [0, 3, 0, 9, 0, 4, 1, 6, 0],
        [0, 0, 0, 6, 0, 2, 5, 7, 1],
        [6, 8, 1, 0, 0, 5, 0, 4, 0],
        [0, 2, 5, 1, 0, 9, 0, 3, 0],
        [0, 0, 6, 8, 5, 3, 0, 0, 4],
        [4, 1, 0, 0, 9, 0, 3, 0, 8],
        [8, 0, 3, 0, 1, 0, 6, 9, 0]
    ],
    [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]
]

for puzzle in puzzles:
    print("="*60 + "\n" + "="*60 + "\n")
    print ("Initial puzzle: \n")
    print_sudoku_puzzle(puzzle)

    # Backtracking solver
    print ("Solving with backtracking: \n")
    result = None
    startTime = time.time() * 1000
    result = backtracking_solver(puzzle)
    endTime = time.time() * 1000
    totalTime = endTime - startTime
    print_sudoku_puzzle(result)

    print (
        "This solution is valid: " + str(validate_sudoku_solution(result)) + "\n" +
        "Runtime was: " + str(totalTime) + "ms" + "\n"
    )

    # Lookadhead solver
    print ("Solving with propagation_forwardtracking_with_lookadhead: \n")
    result = None
    startTime = time.time() * 1000
    result = lookahead_solver(puzzle)
    endTime = time.time() * 1000
    totalTime = endTime - startTime
    print_sudoku_puzzle(result)

    print (
        "This solution is valid: " + str(validate_sudoku_solution(result)) + "\n" + 
        "Runtime was: " + str(totalTime) + "ms" + "\n"
    )

    # Sim annealing solver

