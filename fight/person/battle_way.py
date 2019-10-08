from abc import ABC, abstractmethod
from lib.constants import BattleStatus


class Battle(ABC):
    battle_ways = set([])

    def __init__(self, fighter_1, fighter_2):
        self.battle_status = BattleStatus.prepare
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2

    def hit(self, skill_id, attacker, defender):
        from person.views import Skill
        skill = Skill(skill_id)
        can_use = skill.can_use(attacker)
        if not can_use:
            return
        hit = skill.cal_hit_num(attacker, defender)
        defender.add_hp(-hit)
        return defender.hp

    @abstractmethod
    def battle(self):
        """
        具体的战斗方式
        """


class RandomBattle(Battle):
    """
    random_battle
    """

    def battle(self):
        self.battle_status = BattleStatus.ing
        attacker, defender = self.fighter_1, self.fighter_2
        while True:
            hp = self.hit(attacker.random_skill(), attacker, defender)
            if hp is not None and hp <= 0:
                self.battle_status = BattleStatus.end
                return attacker
            attacker, defender = defender, attacker

# ---------------具体的类型-------------------

# def is_battle_way(m):
#     """
#     module = __import__(get_obj)
#     """
#     if not m.endswith("Battle") or m == 'Battle':
#         return False
#     print('is_battle_way', m)
#     m = __import__(f'person.battle_way.{m}')
#     return m.endswith("Battle") and isinstance(x, Battle)


# def get_battle_ways():
#     battle_ways = {}
#     print('dir()', dir('battle_way'))
#     print('dir()', dir('./'))
#     for m in filter(lambda m: is_battle_way(m), dir('battle_way')):
#         print('m', m)
#         m_name = m.lower.insert(-6, '_')
#         print('m_name', m_name)
#         battle_ways[m_name] = Class.forName(m)


class BattleWays(object):
    battle_ways = {
        'random_battle': RandomBattle,
    }

    @classmethod
    def get_ways(cls):
        return cls.battle_ways

    @classmethod
    def get_way(cls, way):
        return cls.battle_ways.get(way)


battleWays = BattleWays()
