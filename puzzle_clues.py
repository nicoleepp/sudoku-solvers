import json

ROWS = 9
COLUMNS = 9


class Puzzle(object):
    def __init__(self, include, type, puzzle, clues):
        self.include = include
        self.type = type
        self.puzzle = puzzle
        self.clues = clues

def countClues(puzzle):
    count = 0
    for i in range(ROWS):
        for j in range(COLUMNS):
            if puzzle[i][j] is not 0:
                count = count + 1
    return count

class PuzzleType(object):
    def __init__(self, type):
    	self.type = type
        self.min = 81
        self.max = 0
        self.count = 0
        self.total = 0

with open('puzzles.json') as data_file:
    data = json.load(data_file)
    puzzles = data["puzzles"]

    easyPuzzles = PuzzleType("Easy")
    mediumPuzzles = PuzzleType("Medium")
    hardPuzzles = PuzzleType("Hard")
    insanePuzzles = PuzzleType("Insane")

    for puzzleObject in puzzles:
    	clues = countClues(puzzleObject["puzzle"])
        newPuzzle = Puzzle(
            puzzleObject["include"], puzzleObject["type"],
            puzzleObject["puzzle"], clues
        )

        if newPuzzle.include:
            puzzle = newPuzzle.puzzle
            puzzle_type = newPuzzle.type
            puzzle_clues = newPuzzle.clues

            if puzzle_type == "Easy":
                easyPuzzles.count = easyPuzzles.count + 1
                easyPuzzles.total = easyPuzzles.total + puzzle_clues
                if puzzle_clues < easyPuzzles.min:
                    easyPuzzles.min = puzzle_clues
                if puzzle_clues > easyPuzzles.max:
                    easyPuzzles.max = puzzle_clues

            if puzzle_type == "Medium":
                mediumPuzzles.count = mediumPuzzles.count + 1
                mediumPuzzles.total = mediumPuzzles.total + puzzle_clues
                if puzzle_clues < mediumPuzzles.min:
                    mediumPuzzles.min = puzzle_clues
                if puzzle_clues > mediumPuzzles.max:
                    mediumPuzzles.max = puzzle_clues

            if puzzle_type == "Hard":
                hardPuzzles.count = hardPuzzles.count + 1
                hardPuzzles.total = hardPuzzles.total + puzzle_clues
                if puzzle_clues < hardPuzzles.min:
                    hardPuzzles.min = puzzle_clues
                if puzzle_clues > hardPuzzles.max:
                    hardPuzzles.max = puzzle_clues

            if puzzle_type == "Insane":
                insanePuzzles.count = insanePuzzles.count + 1
                insanePuzzles.total = insanePuzzles.total + puzzle_clues
                if puzzle_clues < insanePuzzles.min:
                    insanePuzzles.min = puzzle_clues
                if puzzle_clues > insanePuzzles.max:
                    insanePuzzles.max = puzzle_clues

    # print puzzle type results
    print("\nNumber of clues per puzzle type:")
    row = "{0:23} {1:15} {2:15} {3:15}"
    print(row.format(
        "Puzzle Type:", "Minimum Clues:", "Maximum Clues:", "Average Clues:"
    ))
    print("="*72)
    print(row.format(
        easyPuzzles.type, easyPuzzles.min, easyPuzzles.max, easyPuzzles.total/easyPuzzles.count
    ))
    print(row.format(
        mediumPuzzles.type, mediumPuzzles.min, mediumPuzzles.max, mediumPuzzles.total/mediumPuzzles.count
    ))
    print(row.format(
        hardPuzzles.type, hardPuzzles.min, hardPuzzles.max, hardPuzzles.total/hardPuzzles.count
    ))
    print(row.format(
        insanePuzzles.type, insanePuzzles.min, insanePuzzles.max, insanePuzzles.total/insanePuzzles.count
    ))
    print

