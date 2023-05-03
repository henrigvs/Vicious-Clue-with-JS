from resources.database import db
from src.backend.riddles.domain.Riddle import Riddle


class RiddleModel(db.Model):
    riddle_id = db.Column(db.String(36), primary_key=True)
    description = db.Column(db.String(200))
    solution = db.Column(db.String(100))
    difficulty = db.Column(db.Integer)
    category = db.Column(db.String(20))
    fk_ownerId = db.Column(db.String(36))

    def __init__(self, riddle: Riddle):
        self.riddle_id = riddle.riddleId
        self.description = riddle.description
        self.solution = riddle.solution
        self.difficulty = riddle.difficulty
        self.category = riddle.category
        self.fk_ownerId = riddle.ownerId

    def to_realRiddleObject(self):
        return Riddle(
            riddleId=self.riddle_id,
            description=self.description,
            solution=self.solution,
            clues=[clue.to_realClueObject() for clue in self.clues],
            difficulty=self.difficulty,
            category=self.category,
            ownerId=self.fk_ownerId
        )
