from typing import List, Optional

from resources.database.database import db
from src.riddles.domain.Category import Category
from src.riddles.domain.Riddle import Riddle
from src.riddles.domain.RiddleModel import RiddleModel
from src.riddles.domain.clues.Clue import Clue
from src.riddles.domain.clues.ClueModel import ClueModel


class RiddleRepository:

    @staticmethod
    def addRiddle(riddle: Riddle) -> Riddle:
        riddleModel = RiddleModel(riddle)
        db.session.add(riddleModel)

        for clues in riddle.clues:
            RiddleRepository.addClueToARiddle(riddle.riddleId, clues)

        db.session.commit()

        return riddle

    @staticmethod
    def editRiddle(riddle: Riddle, riddleId: str) -> Riddle | None:
        # Check if riddle exists in database
        checkExistingRiddle = db.session.query(RiddleModel).filter(RiddleModel.riddle_id == riddleId).first()
        if checkExistingRiddle is None:
            return None

        # Validate category
        if riddle.category not in [category.label for category in Category]:
            return None

        # Validate difficulty
        if riddle.difficulty < 0 or riddle.difficulty > 5:
            return None

        db.session.query(RiddleModel).filter(RiddleModel.riddle_id == riddleId).update(
            {
                RiddleModel.riddle_id: riddleId,
                RiddleModel.description: riddle.description,
                RiddleModel.solution: riddle.solution,
                RiddleModel.difficulty: riddle.difficulty,
                RiddleModel.category: riddle.category,
                RiddleModel.fk_ownerId: riddle.ownerId
            }
        )

        # Delete existing clues
        db.session.query(ClueModel).filter(ClueModel.fk_riddle_id == riddleId).delete()

        # Add clues
        for clues in riddle.clues:
            RiddleRepository.addClueToARiddle(riddleId, clues)

        # Reestablish the correct riddle ID for returned value
        riddle.riddleId = riddleId

        db.session.commit()
        return riddle

    @staticmethod
    def getAllRiddle() -> List[Riddle]:
        riddles = db.session.query(RiddleModel).all()
        if riddles:
            for riddle in riddles:
                riddle.clues = db.session.query(ClueModel).filter(ClueModel.fk_riddle_id == riddle.riddle_id).all()
        return [riddle.to_realRiddleObject() for riddle in riddles] if riddles else []

    @staticmethod
    def getRiddleByID(riddleId: str) -> Riddle | None:
        riddle = db.session.query(RiddleModel).filter(RiddleModel.riddle_id == riddleId).first()
        if riddle:
            riddle.clues = db.session.query(ClueModel).filter(ClueModel.fk_riddle_id == riddleId).all()
        return riddle.to_realRiddleObject() if riddle else None

    @staticmethod
    def deleteRiddle(riddleId: str) -> Optional[Riddle]:
        riddle = RiddleRepository.getRiddleByID(riddleId)
        if riddle is not None:
            # Delete associated clues
            db.session.query(ClueModel).filter(ClueModel.fk_riddle_id == riddleId).delete()
            # Delete Riddle
            db.session.query(RiddleModel).filter(RiddleModel.riddle_id == riddleId).delete()
            db.session.commit()
            return riddle
        return None

    @staticmethod
    def getAllRiddlesOfAnOwner(ownerId: str) -> List[Riddle]:
        riddles = db.session.query(RiddleModel).filter(RiddleModel.fk_ownerId == ownerId)
        if riddles:
            for riddle in riddles:
                riddle.clues = db.session.query(ClueModel).filter(ClueModel.fk_riddle_id == riddle.riddle_id).all()
        return [riddle.to_realRiddleObject() for riddle in riddles] if riddles else []

    @staticmethod
    def addClueToARiddle(riddleId: str, clue: Clue):
        clue.setRiddleId(riddleId)
        new_clue = ClueModel(clue)
        db.session.add(new_clue)
        db.session.commit()
