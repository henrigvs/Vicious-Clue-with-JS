
@staticmethod
def convertJSONToERiddlesArray(jsonData) -> []:
    riddles = []
    for data in jsonData:
        riddle = {
            "riddleId": data["riddleId"],
            "description": data["description"],
            "clue": data["clue"],
            "solution": data["solution"],
            "difficulty": data["difficulty"],
            "ownerId": data["ownerId"]
        }
        riddles.append(riddle)
    return riddles