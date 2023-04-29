from src.riddles.api.service.dtos.RiddleDTO import RiddleDTO
from src.riddles.domain.Riddle import Riddle


class RiddleMapper:

    @staticmethod
    def toDTO(riddle):
        if riddle is None:
            return None
        else:
            return RiddleDTO(riddle.riddleId, riddle.description, riddle.solution, riddle.clue, riddle.difficulty, riddle.ownerId)

    @staticmethod
    def toEntity(createRiddleDTO):
        return Riddle(createRiddleDTO.description,
                      createRiddleDTO.solution,
                      createRiddleDTO.clue,
                      createRiddleDTO.difficulty,
                      createRiddleDTO.ownerId)
