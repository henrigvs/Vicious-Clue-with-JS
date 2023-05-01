from typing import List

from src.riddles.api.service.dtos.riddle.CreateRiddleDTO import CreateRiddleDTO
from src.riddles.api.service.dtos.riddle.RiddleDTO import RiddleDTO
from src.riddles.api.service.mapper.RiddleMapper import RiddleMapper
from src.riddles.domain.Riddle import Riddle


class RiddleService:
    def __init__(self, riddleRepository):
        self.riddleRepository = riddleRepository
        self.riddleMapper = RiddleMapper()

    def addRiddle(self, createRiddleDTO: CreateRiddleDTO) -> RiddleDTO:
        riddle = self.riddleMapper.toEntityNew(createRiddleDTO)
        return self.riddleMapper.toDTO(self.riddleRepository.addRiddle(riddle))

    def deleteRiddle(self, riddleId: str) -> RiddleDTO:
        return self.riddleMapper.toDTO(self.riddleRepository.deleteRiddle(riddleId))

    def editRiddle(self, createRiddleDTO: CreateRiddleDTO, riddleId: str) -> RiddleDTO:
        riddle = self.riddleMapper.toEntityNew(createRiddleDTO)
        return self.riddleMapper.toDTO(self.riddleRepository.editRiddle(riddle, riddleId))

    def getAllRiddle(self) -> List[RiddleDTO]:
        return [self.riddleMapper.toDTO(riddle) for riddle in self.riddleRepository.getAllRiddle()]

    def getRiddleByID(self, riddleId: str) -> RiddleDTO:
        return self.riddleMapper.toDTO(self.riddleRepository.getRiddleByID(riddleId))

    def getAllRiddlesOfAnOwner(self, ownerId: str) -> List[RiddleDTO]:
        return [self.riddleMapper.toDTO(riddle) for riddle in self.riddleRepository.getAllRiddlesOfAnOwner(ownerId)]
