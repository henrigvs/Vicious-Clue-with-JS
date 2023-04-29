from typing import List, Optional

from sqlalchemy import update

from database.database import db

from src.riddles.domain.Riddle import Riddle
from src.riddles.domain.RiddleModel import RiddleModel


class RiddleRepository:

    def __init__(self):
        self.riddleRepository = {}

    def addRiddle(self, riddle: Riddle) -> Riddle:
        riddleModel = RiddleModel(
            riddle_id=riddle.riddleId,
            description=riddle.description,
            solution=riddle.solution,
            clue=riddle.clue,
            difficulty=riddle.difficulty,
            fk_ownerId=riddle.ownerId
        )
        db.session.add(riddleModel)
        db.session.commit()

        return riddle

    def editRiddle(self, riddle: Riddle, riddleId: str) -> Riddle | None:
        # Check if riddle exists in database
        checkExistingRiddle = db.session.query(RiddleModel).filter(RiddleModel.riddle_id == riddleId).first()
        if checkExistingRiddle is None:
            return None

        db.session.query(RiddleModel).filter(RiddleModel.riddle_id == riddleId).update(
            {
                RiddleModel.description: riddle.description,
                RiddleModel.solution: riddle.solution,
                RiddleModel.clue: riddle.clue,
                RiddleModel.difficulty: riddle.difficulty,
                RiddleModel.fk_ownerId: riddle.ownerId
            }
        )
        db.session.commit()
        return riddle

    def getAllRiddle(self) -> List[Riddle]:
        riddles = db.session.query(RiddleModel).all()
        return [riddle.to_realRiddleObject() for riddle in riddles] if riddles else []

    def getRiddleByID(self, riddleId: str) -> Riddle | None:
        riddle = db.session.query(RiddleModel).filter(RiddleModel.riddle_id == riddleId).first()
        return riddle.to_realRiddleObject() if riddle else None

    def deleteRiddle(self, riddleId: str) -> Optional[Riddle]:
        riddle = db.session.query(RiddleModel).filter(RiddleModel.riddle_id == riddleId).first()
        if riddle is not None:
            db.session.delete(riddle)
            db.session.commit()
            return riddle.to_realRiddleObject()
        return None

    def getAllRiddlesOfAnOwner(self, ownerId: str) -> List[Riddle]:
        riddles = db.session.query(RiddleModel).filter(RiddleModel.fk_ownerId == ownerId)
        return [riddle.to_realRiddleObject() for riddle in riddles] if riddles else []
