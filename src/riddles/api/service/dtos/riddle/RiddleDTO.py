class RiddleDTO:

    def __init__(self, riddleId: str, description: str, solution: str, clues: list, difficulty: int, category: str, ownerId: str):
        self.riddleId = riddleId
        self.description = description
        self.solution = solution
        self.clues = clues
        self.difficulty = difficulty
        self.category = category
        self.ownerId = ownerId

    def to_dict(self):
        return {
            'riddleId': self.riddleId,
            'description': self.description,
            'solution': self.solution,
            'clues': [clue.to_dict() for clue in self.clues],
            'difficulty': self.difficulty,
            'category': self.category,
            'ownerId': self.ownerId
        }
