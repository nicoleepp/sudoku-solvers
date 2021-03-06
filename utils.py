# Sources:
# https://github.com/erichowens/SudokuSolver/blob/master/sudoku.py
# http://stackoverflow.com/questions/17605898/sudoku-checker-in-python


def print_sudoku_puzzle(data_grid):
    def notzero(s):
        if s != 0:
            return str(s)
        if s == 0:
            return "'"

    output = ""
    for i, row in enumerate(data_grid):
        if i % 3 == 0:
            output += "="*25+'\n'
        for j, value in enumerate(row):
            if j % 3 == 0:
                output += "| "
            output += notzero(value) + " "
        output += "|\n"
    output += "="*25+'\n'
    print output


def validate_sudoku_solution(data_grid):
    """
    Here we should check all the requirements needed for a valid sudoku sln
    We should talk abou this in our report (what conditions are needed to be
    met for a 9 by 9 data grid to be a valid sudoku solution)
    """

    def check_block(data_grid, k):
        """
        Get data indices for kth block of puzzle.
        """
        row_offset = (k % 3) * 3
        col_offset = (k // 3) * 3
        block_data = [
            data_grid[row_offset+i][col_offset+j] for i in range(3) for
            j in range(3)
        ]
        return sorted(list(set(block_data))) != sorted(block_data)

    # check the rows
    for row in data_grid:
        if sorted(list(set(row))) != sorted(row):
            return False
    # check the cols
    cols = []
    for col in range(len(data_grid)):
        for row in data_grid:
            cols += [row[col]]
        # set will get unique values, its converted to list so you can compare
        # it's sorted so the comparison is done correctly.
        if sorted(list(set(cols))) != sorted(cols):
            return False
        cols = []
    # check the blocks
    for num in range(len(data_grid)):
        check_block(data_grid, num)
    # if you get past all the false checks return True
    return True
