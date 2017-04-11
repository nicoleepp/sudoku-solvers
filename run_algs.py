from propagation_forwardtracking_with_lookahead import (
    solve as lookahead_solver
)
from backtracking import sudokuSolver as backtracking_solver
from simulated_annealing import sudoku_solver as sim_annealing_solver
from utils import print_sudoku_puzzle, validate_sudoku_solution

import json
import time

# Designed to work against the brute-force algorithm:
# Brute-force just seems to run forever and never conclude, so not actually including for now
'''[
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


class Puzzle(object):
    def __init__(self, type, puzzle):
        self.type = type
        self.puzzle = puzzle

with open('puzzles.json') as data_file:    
    #data = json.load(data_file)
    #puzzles = data["puzzles"]
    data = json.load(data_file)
    puzzles = data["puzzles"]

    for puzzleObject in puzzles:
        newPuzzle = Puzzle(puzzleObject["type"], puzzleObject["puzzle"])
        puzzle = newPuzzle.puzzle
        print("="*60 + "\n" + "="*60 + "\n")
        print(
            "Puzzle type: " + newPuzzle.type +
            "\nInitial puzzle: \n"
        )
        print_sudoku_puzzle(puzzle)

        # Backtracking solver
        print ("Solving with backtracking: \n")
        result = None

        startTime = time.time() * 1000
        result = backtracking_solver(puzzle)
        endTime = time.time() * 1000
        totalTime = endTime - startTime

        if result is not None:
            print_sudoku_puzzle(result)
            print (
                "\nThis solution is valid: " + str(validate_sudoku_solution(result)) +
                "\nRuntime was: " + str(totalTime) + "ms" + "\n"
            )
        else:
            print("No solution found by backtracking algorithm")

        # Lookadhead solver
        print ("Solving with propagation_forwardtracking_with_lookadhead: \n")
        result = None

        startTime = time.time() * 1000
        result = lookahead_solver(puzzle)
        endTime = time.time() * 1000
        totalTime = endTime - startTime

        if result is not None:
            print_sudoku_puzzle(result)
            print (
                "This solution is valid: " + str(validate_sudoku_solution(result)) + "\n" + 
                "Runtime was: " + str(totalTime) + "ms" + "\n"
            )
        else:
            print("No solution found by lookahead algorithm")

        # Sim annealing solver
        print ("Solving with sim_annealing_solver: \n")
        result = None

        startTime = time.time() * 1000
        result = sim_annealing_solver(puzzle)
        endTime = time.time() * 1000
        totalTime = endTime - startTime

        if result is not None:
            print_sudoku_puzzle(result)
            print (
                "This solution is valid: " + str(validate_sudoku_solution(result)) +
                "\nRuntime was: " + str(totalTime) + "ms" + "\n"
            )
        else:
            print("No solution found by simulated annealing algorithm")

