from flask import Blueprint, jsonify, request

from src.users.api.service.UserService import UserService
from src.users.api.service.dtos.CreateUserDTO import CreateUserDTO
from src.users.api.service.dtos.UserDTO import UserDTO
from src.users.domain.Role import Role
from src.users.domain.UserRepository import UserRepository

# BluePrint
userBP = Blueprint('users', __name__)

# Initializing service
userRepository = UserRepository()
userService = UserService(userRepository)


@userBP.route('/addUser', methods=['POST'])
def addUser():
    data = request.get_json()
    createUserDTO = CreateUserDTO(data['firstName'],
                                  data['lastName'],
                                  data['password'],
                                  data['email'],
                                  _identifyRole(data['role']),
                                  False)
    userDTO = userService.addUser(createUserDTO)
    return _jsonifyUserDTO(userDTO, 201, "email already exists", 400)


@userBP.route('/allUsers', methods=['GET'])
def getAllUsers():
    userDTOs = userService.getAllUsers()
    return jsonify([userDTO.to_dict() for userDTO in userDTOs]), 200


@userBP.route('/<userId>', methods=['GET'])
def getUserById(userId):
    userDTO = userService.getUserByUserId(userId)
    return _jsonifyUserDTO(userDTO, 200, "userId unknown", 404)


@userBP.route('/delete/<userId>', methods=['DELETE'])
def deleteUserByUserId(userId):
    userDTO = userService.deleteUserByUserId(userId)
    return _jsonifyUserDTO(userDTO, 200, "userId unknown", 404)


@userBP.route('/edit/<user_id>', methods=['PUT'])
def editUser(user_id):
    data = request.get_json()
    updatingUserDTO = UserDTO(user_id,
                              data['firstName'],
                              data['lastName'],
                              data['password'],
                              data['email'],
                              _identifyRole(data['role']),
                              data['isConnected'])
    userDTO = userService.editUser(updatingUserDTO)
    return _jsonifyUserDTO(userDTO, 200, "userId unknown", 404)


@userBP.route('/login', methods=['PUT'])
def connectAnUserByEmailAndPassword():
    data = request.get_json()
    email, password = data['email'], data['password']
    userDTO = userService.getUserByEmailAndByPassword(email, password)
    if userDTO is not None:
        userDTO = userService.connectUser(userDTO.userId)
    return _jsonifyUserDTO(userDTO, 200, "Wrong email or password", 400)


@userBP.route('/<user_id>/logout', methods=['PUT'])
def disconnectAnUserByUserId(user_id):
    userDTO = userService.getUserByUserId(user_id)
    updatedUserDTO = userService.disconnectUser(userDTO.userId)
    return _jsonifyUserDTO(updatedUserDTO, 200, "userId unknown", 404)


@userBP.route('/delete/<user_id>', methods=['DELETE'])
def deleteUser(user_id):
    userDTO = userService.deleteUserByUserId(user_id)
    return _jsonifyUserDTO(userDTO, 200, "userId unknown", 404)


@userBP.route('/setBestScore/<user_id>', methods=['PUT'])
def setBestScore(user_id):
    bestScore = request.get_json()['bestScore']
    userDTO = userService.setBestScore(user_id, bestScore)
    return _jsonifyUserDTO(userDTO, 200, "userId unknown", 404)


def _jsonifyUserDTO(userDTO: UserDTO, code_ok: int, message_ko: str, code_ko: int):
    if userDTO is not None:
        return jsonify(userDTO.to_dict()), code_ok
    else:
        return jsonify({'success': False, 'message': message_ko}), code_ko


def _identifyRole(role: str) -> Role:
    # identify role
    if role == "admin":
        return Role.ADMIN
    elif role == "player":
        return Role.PLAYER
    else:
        return Role.UNKNOWN
