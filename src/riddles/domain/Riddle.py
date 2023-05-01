import uuid
from typing import List
from src.riddles.domain.Category import Category
from src.riddles.domain.clues.Clue import Clue


class Riddle:

    def __init__(self,
                 description: str,
                 solution: str,
                 clues: List[Clue],
                 difficulty: int,
                 category: str,
                 ownerId: str,
                 riddleId: str = None):

        self.riddleId = riddleId if riddleId else str(uuid.uuid4())
        self.description = description
        self.solution = solution
        self.clues = clues
        self.difficulty = difficulty
        self.ownerId = ownerId
        self.category = category

    def __repr__(self) -> str:
        clues_repr = ", ".join([str(clue.clueDescription) for clue in self.clues])
        return f"{self.riddleId} - {self.description} - {self.solution} - [{self.clues.__repr__()}] - {self.difficulty} - {self.ownerId}"
