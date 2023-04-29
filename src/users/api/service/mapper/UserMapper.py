from src.users.api.service.dtos.UserDTO import UserDTO
from src.users.domain.User import User


class UserMapper:

    @staticmethod
    def toDTO(user) -> UserDTO:
        if user is None:
            return None
        else:
            return UserDTO(user.userId,
                           user.firstName,
                           user.lastName,
                           user.password,
                           user.email,
                           user.role,
                           user.isConnected)

    @staticmethod
    def toEntity(createUserDTO) -> User:
        return User(createUserDTO.firstName,
                    createUserDTO.lastName,
                    createUserDTO.password,
                    createUserDTO.email,
                    createUserDTO.role,
                    createUserDTO.isConnected)
