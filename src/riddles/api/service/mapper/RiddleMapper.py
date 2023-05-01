from src.riddles.api.service.dtos.clue.ClueDTO import ClueDTO
from src.riddles.api.service.dtos.riddle.CreateRiddleDTO import CreateRiddleDTO
from src.riddles.api.service.dtos.riddle.RiddleDTO import RiddleDTO
from src.riddles.domain.Riddle import Riddle
from src.riddles.domain.clues.Clue import Clue


class RiddleMapper:

    @staticmethod
    def toDTO(riddle: Riddle):
        if riddle is None:
            return None
        else:
            cluesDTO = []
            if riddle.clues is not None:
                cluesDTO = [ClueDTO(clue.clueDescription, riddle.riddleId) for clue in riddle.clues]
            return RiddleDTO(riddle.riddleId, riddle.description, riddle.solution, cluesDTO, riddle.difficulty,
                             riddle.category, riddle.ownerId)

    @staticmethod
    def toEntityNew(createRiddleDTO: CreateRiddleDTO):
        # Create Riddle without assigning clues
        riddle = Riddle(createRiddleDTO.description,
                        createRiddleDTO.solution,
                        createRiddleDTO.clues,
                        createRiddleDTO.difficulty,
                        createRiddleDTO.category,
                        createRiddleDTO.ownerId
                        )
        return riddle

    @staticmethod
    def toEntityUpdate(createRiddleDTO: CreateRiddleDTO, riddleId: str):
        # Create Riddle without assigning clues
        riddle = Riddle(createRiddleDTO.description,
                        createRiddleDTO.solution,
                        [],
                        createRiddleDTO.difficulty,
                        createRiddleDTO.category,
                        createRiddleDTO.ownerId,
                        riddleId
                        )
        # Create Clue objects with the riddleId and add them to the Riddle
        clues = [Clue(createClueDTO.clueDescription, riddleId) for createClueDTO in createRiddleDTO.clues]
        riddle.clues = clues

        return riddle
