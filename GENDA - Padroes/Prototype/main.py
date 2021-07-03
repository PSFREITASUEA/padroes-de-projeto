from Monster import Monster
from MonsterRegistry import MonsterRegistry

if __name__ == "__main__":
    monster_registry = MonsterRegistry()

    water_monster: Monster = monster_registry.get_water_monster()
    earth_monster: Monster = monster_registry.get_earth_monster()

    print("%s: %s" % (water_monster.get_type(), water_monster.get_name()))
    print("%s: %s" % (earth_monster.get_type(), earth_monster.get_name()))
