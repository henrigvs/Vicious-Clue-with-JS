import unittest
from src.backend.users.api.service.UserService import UserService
from src.backend.users.api.service import CreateUserDTO
from src.backend.users.api.service.dtos.UserDTO import UserDTO
from src.backend.users.api.service.mapper.UserMapper import UserMapper
from src.backend.users.domain.UserRepository import UserRepository


class TestUserService(unittest.TestCase):

    def setUp(self):
        # Initialization of objects for tests
        self.userMapper = UserMapper()
        self.userRepository = UserRepository()
        self.userService = UserService(self.userRepository)
        self.createUserDTO = CreateUserDTO("Ada", "Lovelace", "ada.lovelace@example.com", "password123", False)

    def test_addUser(self):
        # Given When
        userDTO = self.userService.addUser(self.createUserDTO)
        userId = userDTO.userId

        # Then
        self.assertIsNotNone(userId)
        self.assertEqual(userDTO.firstName, self.createUserDTO.firstName)
        self.assertEqual(userDTO.lastName, self.createUserDTO.lastName)
        self.assertEqual(userDTO.email, self.createUserDTO.email)

    def test_editUser(self):
        # Given
        userDTO = self.userService.addUser(self.createUserDTO)
        updatingUserDTO = UserDTO(userDTO.userId,
                                  self.createUserDTO.firstName,
                                  self.createUserDTO.lastName,
                                  self.createUserDTO.password,
                                  "ada.lovelace@anotherExample.com",
                                  self.createUserDTO.isConnected)

        # When
        userDTOUpdated = self.userService.editUser(updatingUserDTO)

        # Then
        self.assertIsNotNone(updatingUserDTO.userId)
        self.assertEqual(updatingUserDTO.firstName, userDTOUpdated.firstName)
        self.assertEqual(updatingUserDTO.lastName, userDTOUpdated.lastName)
        self.assertEqual("ada.lovelace@anotherExample.com", userDTOUpdated.email)
        self.assertEqual(updatingUserDTO.password, userDTOUpdated.password)

    def test_getAllUsers(self):
        # Given
        userDTO1 = self.userService.addUser(self.createUserDTO)
        createUserDTO2 = CreateUserDTO("Alan", "Turing", "alan.turing@example.com", "password456", False)
        userDTO2 = self.userService.addUser(createUserDTO2)

        # When
        allUsers = self.userService.getAllUsers()

        # Then
        self.assertEqual(2, len(allUsers))
        self.assertIn(userDTO1, allUsers)
        self.assertIn(userDTO2, allUsers)

    def test_getUserByUserId(self):
        # Given
        userDTO = self.userService.addUser(self.createUserDTO)

        # When
        foundUserDTO = self.userService.getUserByUserId(userDTO.userId)

        # Then
        self.assertIsNotNone(foundUserDTO)
        self.assertEqual(userDTO, foundUserDTO)

    def test_getUserByEmailAndByPassword(self):
        # Given
        userDTO = self.userService.addUser(self.createUserDTO)

        # When
        foundUserDTO = self.userService.getUserByEmailAndByPassword(self.createUserDTO.email, self.createUserDTO.password)

        # Then
        self.assertIsNotNone(foundUserDTO)
        self.assertEqual(userDTO, foundUserDTO)