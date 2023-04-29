import unittest
from src.riddles.domain.Riddle import Riddle
from src.riddles.domain.RiddleRepository import RiddleRepository


class RiddleRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.repository = RiddleRepository()
        self.riddle = Riddle("What has keys but can't open locks?", "A piano", "It's a musical instrument.", 1, "6418389f-d6e7-4a2f-a459-d549bf211818")
        self.addedRiddle = self.repository.addRiddle(self.riddle)

    def test_addRiddle(self):
        self.assertEqual(self.addedRiddle, self.riddle)

    def test_updateRiddle(self):
        updated_riddle = Riddle("Updated description", "Updated solution", "Updated clue", 2, "6418389f-d6e7-4a2f-a459-d549bf211818")
        result = self.repository.editRiddle(updated_riddle, self.riddle.riddleId)
        self.assertEqual(result.description, "Updated description")
        self.assertEqual(result.solution, "Updated solution")
        self.assertEqual(result.clue, "Updated clue")
        self.assertEqual(result.difficulty, 2)

    def test_getAllRiddle(self):
        all_riddles = self.repository.getAllRiddle()
        self.assertIn(self.riddle, all_riddles)

    def test_getRiddleByID(self):
        result = self.repository.getRiddleByID(self.riddle.riddleId)
        self.assertEqual(result, self.riddle)

    def test_deleteRiddle(self):
        deleted_riddle = self.repository.deleteRiddle(self.riddle.riddleId)
        self.assertEqual(deleted_riddle, self.riddle)
        self.assertNotIn(self.riddle.riddleId, self.repository.riddleRepository)

    def tearDown(self):
        del self.repository
        del self.riddle
        del self.addedRiddle


if __name__ == '__main__':
    unittest.main()
