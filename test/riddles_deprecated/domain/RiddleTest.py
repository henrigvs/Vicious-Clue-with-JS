import unittest

from src.riddles.domain.Riddle import Riddle


class RiddleTest(unittest.TestCase):
    def test_riddle_creation(self):
        description = "What has keys but can't open locks?"
        solution = "A piano"
        clue = "It's a musical instrument."
        difficulty = 1

        riddle = Riddle(description, solution, clue, difficulty)

        self.assertEqual(riddle.description, description)
        self.assertEqual(riddle.solution, solution)
        self.assertEqual(riddle.clue, clue)
        self.assertEqual(riddle.difficulty, difficulty)
        self.assertIsInstance(riddle.riddleId, str)

    def test_riddle_repr(self):
        description = "What has keys but can't open locks?"
        solution = "A piano"
        clue = "It's a musical instrument."
        difficulty = 1

        riddle = Riddle(description, solution, clue, difficulty)
        repr_str = riddle.__repr__()

        self.assertIn(riddle.riddleId, repr_str)
        self.assertIn(description, repr_str)
        self.assertIn(solution, repr_str)
        self.assertIn(clue, repr_str)
        self.assertIn(str(difficulty), repr_str)


if __name__ == "__main__":
    unittest.main()
