from typing import List, Optional

from werkzeug.security import check_password_hash

from resources.database import db
from src.backend.users.domain.User import User
from src.backend.users.domain.UserModel import UserModel


class UserRepository:

    @staticmethod
    def addUser(user: User) -> Optional[User]:
        # Check if email address is already in db
        checkExistingEmail = db.session.query(UserModel).filter(UserModel.email == user.email).first()
        if checkExistingEmail is not None:
            return None
        userModel = UserModel(
            user_id=user.userId,
            firstName=user.firstName,
            lastName=user.lastName,
            password=user.password,
            email=user.email,
            role=user.role.label,  # Important to add label !
            isConnected=user.isConnected,
            bestScore=user.bestScore
        )
        db.session.add(userModel)
        db.session.commit()
        return user

    @staticmethod
    def editUser(user: User, userId: str) -> Optional[User]:
        # check if user exists in DB
        checkExistingUser = db.session.query(UserModel).filter(UserModel.user_id == userId).first()
        if checkExistingUser is None:
            return None

        db.session.query(UserModel).filter(UserModel.user_id == userId).update(
            {
                UserModel.firstName: user.firstName,
                UserModel.lastName: user.lastName,
                UserModel.password: user.password,
                UserModel.email: user.email,
                UserModel.role: user.role.label,
                UserModel.isConnected: user.isConnected,
                UserModel.bestScore: user.bestScore
            }
        )
        db.session.commit()
        return user

    @staticmethod
    def getAllUsers() -> List[User]:
        users = db.session.query(UserModel).all()
        return [user.toRealUserObject() for user in users] if users else []

    @staticmethod
    def getUserByUserId(userId: str) -> User | None:
        user = db.session.query(UserModel).filter(UserModel.user_id == userId).first()
        if user is None:
            return None
        else:
            return user.toRealUserObject()

    @staticmethod
    def getUserByEmailAndByPassword(email: str, password: str) -> Optional[User]:
        user = db.session.query(UserModel).filter(
            UserModel.email == email
        ).first()
        if user is None:
            return None
        else:
            # Use check_password_hash to compare the stored hashed password with the provided plaintext password
            if check_password_hash(user.password, password):
                return user.toRealUserObject()
            else:
                return None

    @staticmethod
    def connectUser(userId: str) -> Optional[User]:
        user = UserRepository.getUserByUserId(userId)
        if user is None:
            return None
        db.session.query(UserModel).filter(UserModel.user_id == userId).update({UserModel.isConnected: True})
        db.session.commit()
        return UserRepository.getUserByUserId(userId)

    @staticmethod
    def disconnectUser(userId: str) -> Optional[User]:
        user = UserRepository.getUserByUserId(userId)
        if user is None:
            return None
        db.session.query(UserModel).filter(UserModel.user_id == userId).update({UserModel.isConnected: False})
        db.session.commit()
        return UserRepository.getUserByUserId(userId)

    @staticmethod
    def deleteUserByUserId(userId: str) -> Optional[User]:
        user = db.session.query(UserModel).filter(UserModel.user_id == userId).first()
        if user is None:
            return None
        else:
            db.session.delete(user)
            db.session.commit()
            return user.toRealUserObject()

    @staticmethod
    def setBestScore(userId: str, bestScore: int):
        user = UserRepository.getUserByUserId(userId)
        if user is None:
            return None
        else:
            db.session.query(UserModel).filter(UserModel.user_id == userId).update({UserModel.bestScore: bestScore})
            db.session.commit()
            return UserRepository.getUserByUserId(userId)
