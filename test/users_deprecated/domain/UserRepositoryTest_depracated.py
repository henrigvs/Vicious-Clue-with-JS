import unittest
from src.users.domain.User import User
from src.users.domain.UserRepository import UserRepository


class TestUserRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.userRepository = UserRepository()

        self.user1 = User("Bill", "Gates", "microsoft", "billgates@microsoft.com", False)
        self.user2 = User("Elon", "Musk", "tesla", "elonmusk@tesla.mars", False)

        self.userRepository.addUser(self.user1)
        self.userRepository.addUser(self.user2)

    def test_addUser(self) -> None:
        user3 = User("Steve", "Jobs", "apple", "stevejobs@apple.com", False)
        self.userRepository.addUser(user3)

        self.assertEqual(len(self.userRepository.getAllUsers()), 3)
        self.assertEqual(self.userRepository.getUserByUserId(user3.userId), user3)

    # We don't test the unicity of userId in addUser => since it is a UUID

    def test_addUserWithExistingEmail(self) -> None:
        user4 = User("Billy", "Gatas", "office365", "billgates@microsoft.com", False)

        assert self.userRepository.addUser(user4) is None

    def test_editUser(self) -> None:
        userId = self.user2.userId
        userToUpdate = self.userRepository.getUserByUserId(userId)

        userToUpdate.password = "tesla-X"
        userToUpdate.email = "newemail@tesla.mars"

        self.userRepository.editUser(userToUpdate, userId)

        updatedUser = self.userRepository.getUserByUserId(userId)
        self.assertEqual(updatedUser.password, "tesla-X")
        self.assertEqual(updatedUser.email, "newemail@tesla.mars")

    def test_editUserWithExistingEmail(self) -> None:
        userId1 = self.user1.userId
        userId2 = self.user2.userId
        self.user1.email = self.user2.email

        with self.assertRaises(Exception):
            self.userRepository.editUser(self.user1, userId1)

        self.assertNotEqual(self.user2.email, self.userRepository.getUserByUserId(userId2))

    def test_getAllUsers(self) -> None:
        allUsers = self.userRepository.getAllUsers()

        self.assertEqual(len(allUsers), 2)
        self.assertIn(self.user1, allUsers)
        self.assertIn(self.user2, allUsers)

    def test_getUserByUserId(self) -> None:
        user = self.userRepository.getUserByUserId(self.user1.userId)
        self.assertEqual(user, self.user1)

    def test_getUserByEmailAndByPassword(self) -> None:
        user = self.userRepository.getUserByEmailAndByPassword("billgates@microsoft.com", "microsoft")
        self.assertEqual(user, self.user1)


if __name__ == '__main__':
    unittest.main()
