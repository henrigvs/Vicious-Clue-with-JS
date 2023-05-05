from src.backend.users.domain.Role import Role


class UserDTO:

    def __init__(self, userId: str, firstName: str, lastName: str, password: str, email: str, role: Role,
                 isConnected: bool, correctAnswer: int, incorrectAnswers: int, clueRequested: int,
                 consecutiveSeriesOfThree: int, bestScore: int):
        self.userId = userId
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.role = role
        self.isConnected = isConnected
        self.correctAnswer = correctAnswer
        self.incorrectAnswers = incorrectAnswers
        self.clueRequested = clueRequested
        self.consecutiveSeriesOfThree = consecutiveSeriesOfThree
        self.bestScore = bestScore

    def to_dict(self) -> dict:
        return {
            'userId': self.userId,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'password': self.password,
            'email': self.email,
            'role': self.role.label,
            'isConnected': self.isConnected,
            'correctAnswer': self.correctAnswer,
            'incorrectAnswers': self.incorrectAnswers,
            'clueRequested': self.clueRequested,
            'consecutiveSeriesOfThree': self.consecutiveSeriesOfThree,
            'score': self.bestScore
        }
