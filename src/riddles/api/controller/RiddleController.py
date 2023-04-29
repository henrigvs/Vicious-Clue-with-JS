from flask import jsonify, request, Blueprint

from src.riddles.api.service.RiddleService import RiddleService
from src.riddles.api.service.dtos.CreateRiddleDTO import CreateRiddleDTO
from src.riddles.api.service.dtos.RiddleDTO import RiddleDTO
from src.riddles.domain.RiddleRepository import RiddleRepository

# Blueprint
riddleBP = Blueprint('riddles', __name__)

# Initializing of service
riddleRepository = RiddleRepository()
riddleService = RiddleService(riddleRepository)


# POST
@riddleBP.route('/addRiddle', methods=['POST'])
def addRiddle():
    data = request.get_json()
    createRiddleDTO = CreateRiddleDTO(data['description'], data['solution'], data['clue'], data['difficulty'],
                                      data['ownerId'])
    riddleDTO = riddleService.addRiddle(createRiddleDTO)
    return _jsonifyRiddles(riddleDTO, 201, "add riddle failed", 400)


# DELETE
@riddleBP.route('/delete/<riddleId>', methods=['DELETE'])
def deleteRiddle(riddleId):
    riddleDTO = riddleService.deleteRiddle(riddleId)
    return _jsonifyRiddles(riddleDTO, 200, "riddleId unknown", 404)


# PUT
@riddleBP.route('/edit/<riddleId>', methods=['PUT'])
def editRiddle(riddleId):
    data = request.get_json()
    createRiddleDTO = CreateRiddleDTO(data['description'], data['solution'], data['clue'], data['difficulty'],
                                      data['ownerId'])
    riddleDTO = riddleService.editRiddle(createRiddleDTO, riddleId)
    return _jsonifyRiddles(riddleDTO, 200, "riddleId unknown", 404)


# GET
@riddleBP.route('/getAllRiddles', methods=['GET'])
def getAllRiddles():
    riddleDTOs = riddleService.getAllRiddle()
    return jsonify([riddleDTO.to_dict() for riddleDTO in riddleDTOs])


@riddleBP.route('/riddle/<riddleId>', methods=['GET'])
def getRiddleById(riddleId):
    riddleDTO = riddleService.getRiddleByID(riddleId)
    return _jsonifyRiddles(riddleDTO, 200, "riddleId unknown", 404)


@riddleBP.route('/getAllRiddlesOf/<ownerId>', methods=['GET'])
def getAllRiddlesOfAnOwner(ownerId):
    riddleDTOs = riddleService.getAllRiddlesOfAnOwner(ownerId)
    return jsonify([riddleDTO.to_dict() for riddleDTO in riddleDTOs])


def _jsonifyRiddles(riddleDTO: RiddleDTO, code_ok: int, message_ko, code_ko: int):
    if riddleDTO is not None:
        return jsonify(riddleDTO.to_dict()), code_ok
    else:
        return jsonify({'success': False, 'message': message_ko}), code_ko
