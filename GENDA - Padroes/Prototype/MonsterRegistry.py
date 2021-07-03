from EarthMonster import EarthMonster
from WaterMonster import WaterMonster


class MonsterRegistry:
    def __init__(self):
        self._earthMonster = EarthMonster()
        self._waterMonster = WaterMonster()

    def get_earth_monster(self):
        return self._earthMonster.clone()

    def get_water_monster(self):
        return self._waterMonster.clone()
