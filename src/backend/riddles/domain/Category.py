from enum import Enum


class Category(Enum):
    ANIMAL = 'Animal'
    DIFFICULT = 'Difficult'
    EASY = 'Easy'
    FOOD = 'Food'
    FUNNY = 'Funny'
    KIDS = 'Kids'
    LOGIC = 'Logic'
    MATH = 'Math'
    SPORT = 'Sport'
    TRICKY = 'Tricky'
    WHATIAM = 'What I am'
    WHOIAM = 'Who I am'

    def __init__(self, label):
        self.label = label

    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, value: str) -> None:
        self._label = value
