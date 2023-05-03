from enum import Enum


class Role(Enum):
    UNKNOWN = ("unknown",)
    ADMIN = ("admin",)
    PLAYER = ("player",)

    def __init__(self, label):
        self.label = label

    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, value: str) -> None:
        self._label = value
