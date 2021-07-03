import copy

from Monster import Monster


class EarthMonster(Monster):
    def __init__(self):
        self._type = "EarthMonster"
        self._name = "Minotauro"

    def clone(self):
        return copy.copy(self)
