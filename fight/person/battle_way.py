from abc import ABC, abstractmethod
from lib.constants import BattleStatus
from person.skills import Skill
from person.heros import Hero


class Battle(object):
    def __init__(self, fighter_list):
        self.fighter_list = fighter_list

    @abstractmethod
    def is_finish(self):
        """
        具体的结束方式
        """

    @abstractmethod
    def battle(self):
        """
        具体的战斗方式
        """

    def is_finish_by_hp(self):
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

    # def __init__(self, fighter_list):
    #     super(RandomBattle, self).__init__(fighter_list)

    def is_finish(self):
        return self.is_finish_by_hp()

    def battle(self):
        attacker, defender = self.fighter_list
        while not self.is_finish():
            skill_id = attacker.random_skill()
            attacker.set_skill(skill_id, defender)
            hit = attacker.fight()
            defender.add_hp(-hit)
            attacker, defender = defender, attacker
        return defender


class BattleWays(object):
    battle_ways = {
        'random_battle': RandomBattle,
    }

    @classmethod
    def get_way(cls, way):
        return cls.battle_ways.get(way)


battleWays = BattleWays()
