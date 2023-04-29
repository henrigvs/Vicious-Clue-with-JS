class RiddleDTO:

    def __init__(self, riddleId: str, description: str, solution: str, clue: str, difficulty: int, ownerId: str):
        self.riddleId = riddleId
        self.description = description
        self.solution = solution
        self.clue = clue
        self.difficulty = difficulty
        self.ownerId = ownerId

    def to_dict(self) -> dict:
        return {
            'riddleId': self.riddleId,
            'description': self.description,
            'solution': self.solution,
            'clue': self.clue,
            'difficulty': self.difficulty,
            'ownerId': self.ownerId
        }

    def __eq__(self, other):
        if not isinstance(other, RiddleDTO):
            return False
        return (self.riddleId == other.riddleId and
                self.description == other.description and
                self.solution == other.solution and
                self.clue == other.clue and
                self.difficulty == other.difficulty and
                self.ownerId == other.ownerId)
