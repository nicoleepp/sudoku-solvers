from propagation_forwardtracking_with_lookahead import (
    sudokuSolver as lookahead_solver
)
from backtracking import sudokuSolver as backtracking_solver
from simulated_annealing import sudoku_solver as sim_annealing_solver

import json
import timeit

NUM_TRIES = 10


class Puzzle(object):
    def __init__(self, include, type, puzzle):
        self.include = include
        self.type = type
        self.puzzle = puzzle


class Algorithm(object):
    def __init__(self, name):
        self.name = name
        self.times = {}
        self.total_puzzles = {}

    def add_time(self, time, type):
        if type in self.times:
            self.times[type] += time
            self.total_puzzles[type] += 1
        else:
            self.times[type] = time
            self.total_puzzles[type] = 1


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


with open('puzzles.json') as data_file:
    data = json.load(data_file)
    puzzles = data["puzzles"]
    backtracking_stats = Algorithm("backtracking")
    forwardtracking_stats = Algorithm("forwardtracking")
    sim_annealing_stats = Algorithm("simulatedannealing")

    for puzzleObject in puzzles:
        newPuzzle = Puzzle(
            puzzleObject["include"], puzzleObject["type"],
            puzzleObject["puzzle"]
        )
        if newPuzzle.include:
            puzzle = newPuzzle.puzzle
            puzzle_type = newPuzzle.type

            # Backtracking solver
            backtracking = wrapper(backtracking_solver, puzzle)
            # return value of timeit func is seconds as a float for the total
            # time taken to run the test (not counting the setup)
            # the average is then the time divided by the number argument
            bt_time = timeit.timeit(backtracking, number=NUM_TRIES)
            backtracking_stats.add_time(bt_time/NUM_TRIES, puzzle_type)  # avg

            # Lookadhead solver
            forwardtracking = wrapper(lookahead_solver, puzzle)
            ft_time = timeit.timeit(forwardtracking, number=NUM_TRIES)
            forwardtracking_stats.add_time(ft_time/NUM_TRIES, puzzle_type)

            # Sim annealing solver
            simulatedannealing = wrapper(sim_annealing_solver, puzzle)
            sa_time = timeit.timeit(simulatedannealing, number=NUM_TRIES)
            sim_annealing_stats.add_time(sa_time/NUM_TRIES, puzzle_type)

    # print results
    row = "{0:20} {1:15} {2:15}      {3:10}"
    print(row.format(
        "Algorithm:", "Puzzle Type:", "Time (s):", "Total Puzzles"
    ))
    print("="*72)
    for type in backtracking_stats.times:
        print(row.format(
            backtracking_stats.name, type, backtracking_stats.times[type],
            backtracking_stats.total_puzzles[type]
        ))
    for type in forwardtracking_stats.times:
        print(row.format(
            forwardtracking_stats.name, type,
            forwardtracking_stats.times[type],
            forwardtracking_stats.total_puzzles[type]
        ))
    for type in sim_annealing_stats.times:
        print(row.format(
            sim_annealing_stats.name, type, sim_annealing_stats.times[type],
            sim_annealing_stats.total_puzzles[type]
        ))
