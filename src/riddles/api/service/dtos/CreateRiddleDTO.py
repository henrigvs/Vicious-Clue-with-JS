class CreateRiddleDTO:

    def __init__(self, description: str, solution: str, clue: str, difficulty: int, ownerId: str):
        self.description = description
        self.solution = solution
        self.clue = clue
        self.difficulty = difficulty
        self.ownerId = ownerId
