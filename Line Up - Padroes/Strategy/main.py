from __future__ import annotations
from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self, weapon: WeaponBehavior) -> None:
        self._weapon = weapon

    @property
    def weapon(self) -> WeaponBehavior:
        return self._weapon

    def set_weapon(self, weapon: WeaponBehavior) -> None:
        self._weapon = weapon

    @abstractmethod
    def fight(self) -> None:
        pass


class King(Character):

    def fight(self) -> None:
        print("The King " + self._weapon.use_weapon())


class Queen(Character):

    def fight(self) -> None:
        print("The Queen " + self._weapon.use_weapon())


class Knight(Character):

    def fight(self) -> None:
        print("The Knight " + self._weapon.use_weapon())


class Troll(Character):

    def fight(self) -> None:
        print("The Troll " + self._weapon.use_weapon())


class WeaponBehavior(ABC):

    @abstractmethod
    def use_weapon(self):
        pass


class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        return "used a sword"


class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        return "used a knife"


class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        return "used a axe"


class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        return "shot an arrow"


if __name__ == "__main__":

    queen = Queen(AxeBehavior())
    queen.fight()
    king = King(KnifeBehavior())
    king.fight()
    king.set_weapon(BowAndArrowBehavior())
    king.fight()