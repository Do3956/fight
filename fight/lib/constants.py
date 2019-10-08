from enum import Enum


class StrEnum(str, Enum):
    pass


class BattleStatus(StrEnum):
    prepare = 'prepare'
    ing = 'ing'
    end = 'end'

