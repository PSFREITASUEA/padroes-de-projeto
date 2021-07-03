import copy

from Monster import Monster


class WaterMonster(Monster):
    def __init__(self):
        self._type = "WaterMonster"
        self._name = "Tchutchuco"

    def clone(self):
        return copy.copy(self)
