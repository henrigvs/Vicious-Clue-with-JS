
@staticmethod
def convertJSONToERiddlesArray(jsonData) -> []:
    riddles = []
    for data in jsonData:
        riddle = {
            "riddleId": data["riddleId"],
            "description": data["description"],
            "clues": data["clues"],
            "solution": data["solution"],
            "difficulty": data["difficulty"],
            "ownerId": data["ownerId"]
        }
        riddles.append(riddle)
    return riddles