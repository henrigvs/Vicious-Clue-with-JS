import uuid


class Clue:

    def __init__(self, clueDescription: str, riddleId: str = None, clueId: str = None):
        self.clueId = clueId if clueId else str(uuid.uuid4())
        self.clueDescription = clueDescription
        self.riddleId = riddleId

    def setRiddleId(self, riddleId: str):
        self.riddleId = riddleId

    def __repr__(self) -> str:
        return f"Clue(clueId={self.clueId}, clueDescription={self.clueDescription}, riddleId={self.riddleId})"
