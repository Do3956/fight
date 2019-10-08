from enum import Enum


class StrEnum(str, Enum):
    pass


class BattleStatus(StrEnum):
    prepare = 'prepare'
    ing = 'ing'
    end = 'end'


class BattleWay(StrEnum):
    turn_base = 'turn_base'


if __name__ == "__main__":
    print('a' in BattleWay.__dict__)
    print('turn_base' in BattleWay.__dict__)
    print(BattleWay.__dict__)
