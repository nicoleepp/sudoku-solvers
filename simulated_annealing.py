# Simulated annealing solver for sudoku puzzles
# Sources:
# https://github.com/erichowens/SudokuSolver

from random import shuffle, random, sample, randint
from copy import deepcopy
from math import exp


class SudokuPuzzle(object):
    def __init__(self, data, original_entries=None):
        """
        data - input puzzle as a 2D array, all rows concatenated.

        original_entries - for inheritance of the original entries of one
                                sudoku puzzle's original, immutable entries we
                                don't allow to change between random steps.
        """
        self.data = data

        if original_entries is None:
            self.original_entries = [
                (i, j) for i in range(9) for j in range(9) if
                self.data[i][j] > 0
            ]
        else:
            self.original_entries = original_entries

    def randomize_on_zeroes(self):
        """
        Go through entries, replace incomplete entries (zeroes)
        with random numbers.
        """
        for num in range(9):
            block_indices = self.get_block_indices(num)
            block = [self.data[i][j] for (i, j) in block_indices]
            zero_indices = [
                ind for m, ind in enumerate(block_indices) if block[m] == 0
            ]
            to_fill = [i for i in range(1, 10) if i not in block]
            shuffle(to_fill)
            for ind, value in zip(zero_indices, to_fill):
                self.data[ind[0]][ind[1]] = value

    def score_board(self):
        """
        Score board by viewing every row and column and giving
        -1 points for each unique entry.
        """
        score = 0
        for row in self.data:
            score -= len(set(row))

        for i in range(9):
            col = list(self.data[j][i] for j in range(9))
            score -= len(set(col))
        return score

    def get_block_indices(self, k, ignore_originals=False):
        """
        Get data indices for kth block of puzzle.
        """
        row_offset = (k % 3) * 3
        col_offset = (k // 3) * 3
        indices = [
            (row_offset+i, col_offset+j) for i in range(3) for j in range(3)
        ]
        if ignore_originals:
            indices = filter(lambda x: x not in self.original_entries, indices)
        return indices

    def make_candidate_data(self):
        """
        Generates "neighbor" board by randomly picking
        a square, then swapping two small squares within.
        """
        new_data = deepcopy(self.data)
        block = randint(0, 8)
        num_in_block = len(
            self.get_block_indices(block, ignore_originals=True)
        )
        random_squares = sample(range(num_in_block), 2)
        square1, square2 = [
            self.get_block_indices(block, ignore_originals=True)[ind] for
            ind in random_squares
        ]
        new_data[square1[0]][square1[1]], new_data[square2[0]][square2[1]] = new_data[square2[0]][square2[1]], new_data[square1[0]][square1[1]]
        return new_data


def sudoku_solver(input_data):
    """
    Uses a simulated annealing technique to solve a Sudoku puzzle.

    Randomly fills out the sub-squares to be consistent sub-solutions.

    Scores a puzzle by giving a -1 for every unique element
    in each row or each column. Best solution has a score of -162.
    (This is our stopping rule.)

    Candidate for new puzzle is created by randomly selecting
    sub-square, then randomly flipping two of its entries, evaluating
    the new score. The delta_S is the difference between the scores.

    Let T be the global temperature of our system, with a geometric
    schedule for decreasing (perhaps by T <- .999 T).

    If U is drawn uniformly from [0,1], and exp((delta_S/T)) > U,
    then we accept the candidate solution as our new state.
    """

    SP = SudokuPuzzle(input_data)
    SP.randomize_on_zeroes()
    best_SP = deepcopy(SP)
    current_score = SP.score_board()
    best_score = current_score
    T = .5
    count = 0

    while (count < 400000) and best_score != -162:
        if (count % 1000 == 0):

            # For debugging, comment this print when benchmarking
            print (
                "Iteration %s,    \tT = %.5f, \tbest_score = %s,"
                " \tcurrent_score = %s" % (
                    count, T, best_score, current_score
                )
            )

        candidate_data = SP.make_candidate_data()
        SP_candidate = SudokuPuzzle(candidate_data, SP.original_entries)
        candidate_score = SP_candidate.score_board()
        delta = float(current_score - candidate_score)

        if (exp((delta/T)) - random() > 0):
            SP = SP_candidate
            current_score = candidate_score

        if (current_score < best_score):
            best_SP = deepcopy(SP)
            best_score = best_SP.score_board()

        if candidate_score == -162:
            SP = SP_candidate
            break

        T = .99999*T
        count += 1
    if best_score == -162:
        return best_SP.data
    else:
        return None

