import unittest

from src.riddles.api.service.RiddleService import RiddleService
from src.riddles.api.service.dtos.CreateRiddleDTO import CreateRiddleDTO
from src.riddles.api.service.dtos.RiddleDTO import RiddleDTO
from src.riddles.domain.Riddle import Riddle
from src.riddles.domain.RiddleRepository import RiddleRepository
from src.riddles.api.service.mapper.RiddleMapper import RiddleMapper


class RiddleServiceTest(unittest.TestCase):

    def setUp(self):
        self.riddleRepository = RiddleRepository()
        self.riddleMapper = RiddleMapper()
        self.riddleService = RiddleService(self.riddleRepository)

    def test_addRiddle(self):
        createRiddleDTO = CreateRiddleDTO("Test description", "Test solution", "Test clue", 1, "userID1")
        riddleDTO = self.riddleService.addRiddle(createRiddleDTO)

        self.assertIsInstance(riddleDTO, RiddleDTO)
        self.assertEqual(riddleDTO.description, createRiddleDTO.description)
        self.assertEqual(riddleDTO.solution, createRiddleDTO.solution)
        self.assertEqual(riddleDTO.clue, createRiddleDTO.clue)
        self.assertEqual(riddleDTO.difficulty, createRiddleDTO.difficulty)
        self.assertEqual(riddleDTO.ownerId, createRiddleDTO.ownerId)

    def test_deleteRiddle(self):
        # Given
        createRiddleDTO = CreateRiddleDTO("Test description", "Test solution", "Test clue", 1, "userID1")
        riddleId = self.riddleRepository.addRiddle(self.riddleMapper.toEntity(createRiddleDTO)).riddleId
        assert self.riddleRepository.getRiddleByID(riddleId) is not None

        # When
        self.riddleService.deleteRiddle(riddleId)

        # Then
        assert self.riddleRepository.getRiddleByID(riddleId) is None

    def test_updateRiddle(self):
        # Given
        riddle = Riddle("Test description", "Test solution", "Test clue", 1, "userID1")
        riddleId = self.riddleRepository.addRiddle(riddle).riddleId

        # When
        updatingRiddleDTO = CreateRiddleDTO("Updated description", "Updated solution", "Updated clue", 2, "userID1")
        updatedRiddleDTO = self.riddleService.editRiddle(updatingRiddleDTO, riddleId)

        # Then
        assert updatedRiddleDTO is not None
        assert updatedRiddleDTO.riddleId == riddleId
        assert updatedRiddleDTO.description == "Updated description"
        assert updatedRiddleDTO.solution == "Updated solution"
        assert updatedRiddleDTO.clue == "Updated clue"
        assert updatedRiddleDTO.difficulty == 2

    def test_getAllRiddles(self):
        # Given
        riddle1 = Riddle("Test description 1", "Test solution 1", "Test clue 1", 1, "userID1")
        riddle2 = Riddle("Test description 2", "Test solution 2", "Test clue 2", 2, "userID1")
        self.riddleRepository.addRiddle(riddle1)
        self.riddleRepository.addRiddle(riddle2)

        # When
        riddleDTOs = self.riddleService.getAllRiddle()

        # Then
        assert len(riddleDTOs) == 2
        assert riddleDTOs.__contains__(self.riddleMapper.toDTO(riddle1))
        assert riddleDTOs.__contains__(self.riddleMapper.toDTO(riddle2))

    def test_getRiddleByID(self):
        # Given
        riddle = Riddle("Test description", "Test solution", "Test clue", 1, "userID1")
        riddleId = self.riddleRepository.addRiddle(riddle).riddleId

        # When
        riddleDTO = self.riddleService.getRiddleByID(riddleId)

        # Then
        assert riddleDTO.riddleId == riddleId
        assert riddleDTO.description == "Test description"
        assert riddleDTO.solution == "Test solution"
        assert riddleDTO.clue == "Test clue"
        assert riddleDTO.difficulty == 1

