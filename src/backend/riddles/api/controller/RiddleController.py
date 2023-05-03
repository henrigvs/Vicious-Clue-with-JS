from flask import jsonify, request, Blueprint

from src.backend.riddles.api.service.RiddleService import RiddleService
from src.backend.riddles.api.service.dtos.riddle.CreateRiddleDTO import CreateRiddleDTO
from src.backend.riddles.domain.Category import Category
from src.backend.riddles.domain.RiddleRepository import RiddleRepository
from src.backend.riddles.domain.clues.Clue import Clue

# Blueprint
riddleBP = Blueprint('riddles', __name__)

# Initializing of service
riddleRepository = RiddleRepository()
riddleService = RiddleService(riddleRepository)


# POST
@riddleBP.route('/addRiddle', methods=['POST'])
def addRiddle():
    data = request.get_json()
    # Validate category
    if data['category'] not in [category.label for category in Category]:
        return jsonify({
            "message": "Creation failed",
            "error": "Invalid category"
        }), 400
    # Validate difficulty
    elif data['difficulty'] < 0 or data['difficulty'] > 5:
        return jsonify({
            "message": "Creation failed",
            "error": "Invalid difficulty"
        }), 400
    # Return created object
    else:
        # Create an array of Clue objects
        clues = []
        for clue in data['clues']:
            newClue = Clue(clue['description'])
            clues.append(newClue)

        createRiddleDTO = CreateRiddleDTO(
            data['description'],
            data['solution'],
            clues,
            data['difficulty'],
            data['category'],
            data['ownerId']
        )

        riddleDTO = riddleService.addRiddle(createRiddleDTO)
        return jsonify(riddleDTO.to_dict()), 201


# DELETE
@riddleBP.route('/delete/<riddleId>', methods=['DELETE'])
def deleteRiddle(riddleId):
    riddleDTO = riddleService.deleteRiddle(riddleId)
    if riddleDTO is None:
        return jsonify({
            "message": "failed",
            "error": "Invalid riddle ID"
        }), 404
    return jsonify(riddleDTO.to_dict()), 200


# PUT
@riddleBP.route('/edit/<riddleId>', methods=['PUT'])
def editRiddle(riddleId):
    data = request.get_json()
    # Validate category
    if data['category'] not in [category.label for category in Category]:
        return jsonify(
            {
                "message": "Creation failed",
                "error": "Invalid category"
            }
        ), 400
    # Validate difficulty
    elif data['difficulty'] < 0 or data['difficulty'] > 5:
        return jsonify(
            {
                "message": "Creation failed",
                "error": "Invalid difficulty"
            }
        ), 400
    else:
        # Create an array of Clue objects
        clues = []
        for clue in data['clues']:
            newClue = Clue(clue['description'])
            clues.append(newClue)

        createRiddleDTO = CreateRiddleDTO(
            data['description'],
            data['solution'],
            clues,
            data['difficulty'],
            data['category'],
            data['ownerId']
        )
        riddleDTO = riddleService.editRiddle(createRiddleDTO, riddleId)
        return jsonify(riddleDTO.to_dict()), 200


# GET
@riddleBP.route('/getAllRiddles', methods=['GET'])
def getAllRiddles():
    riddleDTOs = riddleService.getAllRiddle()
    return jsonify([riddleDTO.to_dict() for riddleDTO in riddleDTOs])


@riddleBP.route('/riddle/<riddleId>', methods=['GET'])
def getRiddleById(riddleId):
    riddleDTO = riddleService.getRiddleByID(riddleId)
    if riddleDTO is None:
        return jsonify(
            {
                "message": "failed",
                "error": "Invalid riddle ID"
            }
        ), 404
    return jsonify(riddleDTO.to_dict()), 200


@riddleBP.route('/getAllRiddlesOf/<userId>', methods=['GET'])
def getAllRiddlesOfAnOwner(userId):
    riddleDTOs = riddleService.getAllRiddlesOfAnOwner(userId)
    if riddleDTOs is None:
        return jsonify(
            {
                "message": "fetch failed",
                "error": "Invalid user ID"
            }
        )
    else:
        return jsonify([riddleDTO.to_dict() for riddleDTO in riddleDTOs])


@riddleBP.route('/increaseDifficulty/<riddleId>', methods=['POST'])
def increaseDifficulty(riddleId):
    riddleDTO = riddleService.increaseDifficulty(riddleId)
    if riddleDTO is None:
        return jsonify(
            {
                "message": "failed",
                "error": "Invalid riddle ID or difficulty already at 5"
            }
        ), 404
    return jsonify(riddleDTO.to_dict()), 200


@riddleBP.route('/decreaseDifficulty/<riddleId>', methods=['POST'])
def decreaseDifficulty(riddleId):
    riddleDTO = riddleService.decreaseDifficulty(riddleId)
    if riddleDTO is None:
        return jsonify(
            {
                "message": "failed",
                "error": "Invalid riddle ID or difficulty already at 0"
            }
        ), 404
    return jsonify(riddleDTO.to_dict()), 200
