from src.backend.users.api.service.dtos.UserDTO import UserDTO
from src.backend.users.domain.User import User


class UserMapper:

    @staticmethod
    def toDTO(user) -> UserDTO | None:
        if user is None:
            return None
        else:
            return UserDTO(userId=user.userId,
                           firstName=user.firstName,
                           lastName=user.lastName,
                           password=user.password,
                           email=user.email,
                           role=user.role,
                           isConnected=user.isConnected,
                           correctAnswer=user.correctAnswer,
                           incorrectAnswers=user.incorrectAnswers,
                           clueRequested=user.clueRequested,
                           consecutiveSeriesOfThree=user.consecutiveSeriesOfThree,
                           bestScore=user.bestScore)

    @staticmethod
    def toEntity(createUserDTO) -> User:
        return User(firstName=createUserDTO.firstName,
                    lastName=createUserDTO.lastName,
                    password=createUserDTO.password,
                    email=createUserDTO.email,
                    role=createUserDTO.role,
                    isConnected=createUserDTO.isConnected,
                    correctAnswer=0,
                    incorrectAnswers=0,
                    consecutiveSeriesOfThree=0,
                    clueRequested=0,
                    bestScore=0)
