from typing import List

from src.backend.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.backend.users.api.service.dtos.UserDTO import UserDTO
from src.backend.users.api.service.mapper.UserMapper import UserMapper
from src.backend.users.domain.User import User


class UserService:

    def __init__(self, userRepository):
        self.userRepository = userRepository
        self.userMapper = UserMapper()

    def addUser(self, createUserDTO: CreateUserDTO) -> UserDTO:
        user = self.userRepository.addUser(UserMapper.toEntity(createUserDTO))
        return self.userMapper.toDTO(user)

    def editUser(self, updatingUserDTO: UserDTO) -> UserDTO:
        user = User(
            firstName=updatingUserDTO.firstName,
            lastName=updatingUserDTO.lastName,
            password=updatingUserDTO.password,
            email=updatingUserDTO.email,
            role=updatingUserDTO.role,
            isConnected=updatingUserDTO.isConnected,
            correctAnswer=updatingUserDTO.correctAnswer,
            incorrectAnswers=updatingUserDTO.incorrectAnswers,
            clueRequested=updatingUserDTO.clueRequested,
            consecutiveSeriesOfThree=updatingUserDTO.consecutiveSeriesOfThree,
            bestScore=updatingUserDTO.bestScore)
        updatedUser = self.userRepository.editUser(user, updatingUserDTO.userId)
        return self.userMapper.toDTO(updatedUser)

    def getAllUsers(self) -> List[UserDTO]:
        users = self.userRepository.getAllUsers()
        return [self.userMapper.toDTO(user) for user in users]

    def getUserByUserId(self, userId: str) -> UserDTO:
        user = self.userRepository.getUserByUserId(userId)
        return self.userMapper.toDTO(user)

    def getUserByEmailAndByPassword(self, email: str, password: str) -> UserDTO:
        user = self.userRepository.getUserByEmailAndByPassword(email, password)
        return self.userMapper.toDTO(user)

    def connectUser(self, userId: str):
        user = self.userRepository.connectUser(userId)
        return self.userMapper.toDTO(user)

    def disconnectUser(self, userId: str):
        user = self.userRepository.disconnectUser(userId)
        return self.userMapper.toDTO(user)

    def deleteUserByUserId(self, userId: str) -> UserDTO:
        deletedUser = self.userRepository.deleteUserByUserId(userId)
        return self.userMapper.toDTO(deletedUser)

    def setScore(self, userId: str, correctAnswer: int, incorrectAnswer: int, clueRequested: int,
                 consecutiveSeriesOfThree: int):
        user = self.userRepository.setScore(userId=userId,
                                            correctAnswer=correctAnswer,
                                            incorrectAnswer=incorrectAnswer,
                                            clueRequested=clueRequested,
                                            consecutiveSeriesOfThree=consecutiveSeriesOfThree)
        return self.userMapper.toDTO(user)
