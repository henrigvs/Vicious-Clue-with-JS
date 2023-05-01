from src.users.domain.Role import Role


class CreateUserDTO:

    def __init__(self, firstName: str, lastName: str, password: str, email: str, role: Role, isConnected: bool):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.role = role
        self.isConnected = isConnected
        self.bestScore = 0
