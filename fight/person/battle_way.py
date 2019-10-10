from abc import ABC, abstractmethod
from lib.constants import BattleStatus
from person.skills import Skill
from person.heros import Hero
from lib.config import config


class Battle(ABC):
    def __init__(self, fighter_1, fighter_2):
        self.fighter_list = [fighter_1, fighter_2]

    def is_finish(self):
        """
        具体的结束方式
        """
        return self._is_finish_by_hp()

    @abstractmethod
    def battle(self) -> Hero:
        """
        具体的战斗方式
        """

    def _is_finish_by_hp(self):
        """
        """
        for hero in self.fighter_list:
            if hero.data.hp <= 0:
                return True
        return False


class RandomBattle(Battle):
    """
    random_battle
    """

    def battle(self):
        attacker, defender = self.fighter_list
        while not self.is_finish():
            hit = attacker.fight(defender)
            defender.add_hp(-hit)
            attacker, defender = defender, attacker
        return defender


class BattleManager(object):
    battle_ways = {
        'random_battle': RandomBattle,
    }

    @classmethod
    def get_way(cls, way):
        return cls.battle_ways.get(way)

    @classmethod
    def all_ways(cls, way):
        return cls.battle_ways.keys()
