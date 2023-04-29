from src.users.domain.Role import Role


class CreateUserDTO:

    def __init__(self, firstName: str, lastName: str, password: str, email: str, role: Role, isConnected: bool):
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.role = role
        self.isConnected = isConnected

    def __eq__(self, o):
        if not isinstance(o, CreateUserDTO):
            return False
        return (self.firstName == o.firstName
                and self.lastName == o.lastName
                and self.password == o.password
                and self.email == o.email
                and self.role == o.role
                and self.isConnected == o.isConnected)