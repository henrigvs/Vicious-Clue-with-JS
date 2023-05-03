class CreateRiddleDTO:

    def __init__(self, description: str, solution: str, clues: list, difficulty: int, category: str, ownerId: str):
        self.description = description
        self.solution = solution
        self.clues = clues
        self.difficulty = difficulty
        self.ownerId = ownerId
        self.category = category
