from resources.database import db
from src.backend.users.domain.Role import Role
from src.backend.users.domain.User import User


class UserModel(db.Model):
    user_id = db.Column(db.String(36), primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    role = db.Column(db.String(10))
    isConnected = db.Column(db.Boolean)
    bestScore = db.Column(db.Integer)

    def __init__(self, user_id: str, firstName: str, lastName: str, password: str, email: str, role: str,
                 isConnected: bool, bestScore: int):
        self.user_id = user_id
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.role = role
        self.isConnected = isConnected
        self.bestScore = bestScore

    def toRealUserObject(self):
        getRole = None
        if self.role == "player":
            getRole = Role.PLAYER
        elif self.role == "admin":
            getRole = Role.ADMIN

        return User(
            userId=self.user_id,
            firstName=self.firstName,
            lastName=self.lastName,
            password=self.password,
            email=self.email,
            role=getRole,
            isConnected=self.isConnected,
            bestScore=self.bestScore
        )
