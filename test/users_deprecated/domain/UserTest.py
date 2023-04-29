import unittest
import uuid
from src.users.domain.User import User


class TestUser(unittest.TestCase):

    def test_constructor(self):
        # Arrange
        name = "John"
        lastName = "Doe"
        password = "password123"
        email = "johndoe@example.com"
        isConnected = True

        # Act
        user = User(name, lastName, password, email, isConnected)

        # Assert
        self.assertIsInstance(user, User)
        self.assertEqual(user.firstName, name)
        self.assertEqual(user.lastName, lastName)
        self.assertEqual(user.password, password)
        self.assertEqual(user.email, email)
        self.assertEqual(user.isConnected, isConnected)
        self.assertIsInstance(uuid.UUID(user.userId), uuid.UUID)


if __name__ == '__main__':
    unittest.main()
