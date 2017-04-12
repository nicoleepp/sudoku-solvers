from propagation_forwardtracking_with_lookahead import (
    sudokuSolver as lookahead_solver
)
from backtracking import sudokuSolver as backtracking_solver
from simulated_annealing import sudoku_solver as sim_annealing_solver
from utils import print_sudoku_puzzle, validate_sudoku_solution

import json
import time


class Puzzle(object):
    def __init__(self, include, type, puzzle):
        self.include = include
        self.type = type
        self.puzzle = puzzle

with open('puzzles.json') as data_file:    
    #data = json.load(data_file)
    #puzzles = data["puzzles"]
    data = json.load(data_file)
    puzzles = data["puzzles"]

    for puzzleObject in puzzles:
        newPuzzle = Puzzle(puzzleObject["include"], puzzleObject["type"], puzzleObject["puzzle"])
        if newPuzzle.include:
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

