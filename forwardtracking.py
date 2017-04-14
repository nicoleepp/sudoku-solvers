# Sources:
# http://stackoverflow.com/questions/1697334/algorithm-for-solving-sudoku
# Forward Checking & Look Ahead:
# http://ktiml.mff.cuni.cz/~bartak/constraints/propagation.html
from utils import validate_sudoku_solution
from copy import deepcopy

N = 9


def sudokuSolver(field):
    result = solve(field)
    if result is None:
        return None
    isValid = validate_sudoku_solution(result)
    if not isValid:
        return None
    else:
        return result


def read(field):
    # Read field into state (replace 0 with set of possible values)

    state = deepcopy(field)
    for i in range(N):
        for j in range(N):
            cell = state[i][j]
            if cell == 0:
                state[i][j] = set(range(1, 10))

    return state


def done(state):
    # Are we done?

    for row in state:
        for cell in row:
            if isinstance(cell, set):
                return False
    return True


def propagate_step(state):
    # Propagate one step

    new_units = False

    for i in range(N):
        row = state[i]
        values = set([x for x in row if not isinstance(x, set)])
        for j in range(N):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    state[i][j] = state[i][j].pop()
                    new_units = True
                elif len(state[i][j]) == 0:
                    return False, None

    for j in range(N):
        column = [state[x][j] for x in range(N)]
        values = set([x for x in column if not isinstance(x, set)])
        for i in range(N):
            if isinstance(state[i][j], set):
                state[i][j] -= values
                if len(state[i][j]) == 1:
                    state[i][j] = state[i][j].pop()
                    new_units = True
                elif len(state[i][j]) == 0:
                    return False, None

    for x in range(3):
        for y in range(3):
            values = set()
            for i in range(3*x, 3*x+3):
                for j in range(3*y, 3*y+3):
                    cell = state[i][j]
                    if not isinstance(cell, set):
                        values.add(cell)
            for i in range(3*x, 3*x+3):
                for j in range(3*y, 3*y+3):
                    if isinstance(state[i][j], set):
                        state[i][j] -= values
                        if len(state[i][j]) == 1:
                            state[i][j] = state[i][j].pop()
                            new_units = True
                        elif len(state[i][j]) == 0:
                            return False, None

    return True, new_units


def propagate(state):
    # Propagate until we reach a fixpoint
    while True:
        solvable, new_unit = propagate_step(state)
        if not solvable:
            return False
        if not new_unit:
            return True


def solve(field):
    # Solve sudoku

    state = read(field)

    solvable = propagate(state)

    if not solvable:
        return None

    if done(state):
        return state

    for i in range(N):
        for j in range(N):
            cell = state[i][j]
            if isinstance(cell, set):
                for value in cell:
                    new_state = deepcopy(state)
                    new_state[i][j] = value
                    solved = solve(new_state)
                    if solved is not None:
                        return solved
                return None
