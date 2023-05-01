import uuid

from resources.database import db
from src.riddles.domain.clues.Clue import Clue


class ClueModel(db.Model):
    __tablename__ = 'clue'
    clue_id = db.Column(db.String(36), primary_key=True)
    clue_description = db.Column(db.String(200))
    fk_riddle_id = db.Column(db.String(36))

    def __init__(self, clue: Clue):
        self.clue_id = clue.clueId
        self.clue_description = clue.clueDescription
        self.fk_riddle_id = clue.riddleId

    def to_realClueObject(self) -> Clue:
        return Clue(clueId=self.clue_id,
                    clueDescription=self.clue_description,
                    riddleId=self.fk_riddle_id)