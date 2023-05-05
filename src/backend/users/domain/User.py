import uuid

from src.backend.users.domain import Role


class User:

    def __init__(self, firstName: str, lastName: str, password: str, email: str, role: Role, bestScore: int,
                 correctAnswer: int, incorrectAnswers: int, clueRequested: int, consecutiveSeriesOfThree: int, isConnected=False,
                 userId: str = None):
        self.userId = userId if userId else str(uuid.uuid4())
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.role = role
        self.isConnected = isConnected
        self.bestScore = bestScore
        self.correctAnswer = correctAnswer
        self.incorrectAnswers = incorrectAnswers
        self.clueRequested = clueRequested
        self.consecutiveSeriesOfThree = consecutiveSeriesOfThree

    def __repr__(self) -> str:
        return self.userId + " - " \
            + self.firstName + " - " \
            + self.lastName + " - " \
            + self.password + " - " \
            + self.email + " - " \
            + self.role.label + " - " \
            + str(self.correctAnswer) + " - "\
            + str(self.incorrectAnswers) + " - " \
            + str(self.clueRequested) + " - " \
            + str(self.consecutiveSeriesOfThree) + " - " \
            + str(self.isConnected) \
            + str(self.bestScore)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, User):
            return False
        return (
                self.firstName == o.firstName
                and self.lastName == o.lastName
                and self.email == o.email
                and self.password == o.password
                and self.role == o.role
        )
