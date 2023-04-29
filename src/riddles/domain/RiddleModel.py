from database import db
from src.riddles.domain.Riddle import Riddle


class RiddleModel(db.Model):
    riddle_id = db.Column(db.String(36), primary_key=True)
    description = db.Column(db.String(200))
    solution = db.Column(db.String(100))
    clue = db.Column(db.String(100))
    difficulty = db.Column(db.Integer)
    fk_ownerId = db.Column(db.String(36))

    def __init__(self, riddle_id, description, solution, clue, difficulty, fk_ownerId):
        self.riddle_id = riddle_id
        self.description = description
        self.solution = solution
        self.clue = clue
        self.difficulty = difficulty
        self.fk_ownerId = fk_ownerId

    def to_realRiddleObject(self):
        return Riddle(
            riddleId=self.riddle_id,
            description=self.description,
            solution=self.solution,
            clue=self.clue,
            difficulty=self.difficulty,
            ownerId=self.fk_ownerId
        )
