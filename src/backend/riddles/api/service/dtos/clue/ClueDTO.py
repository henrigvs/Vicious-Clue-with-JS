
class ClueDTO:
    def __init__(self, clueDescription: str, riddleId: str):
        self.clueDescription = clueDescription
        self.riddleId = riddleId

    def to_dict(self):
        return {
            'clueDescription': self.clueDescription,
            'riddleId': self.riddleId
        }
