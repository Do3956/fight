import random

from django.shortcuts import render
from lib.config import config
from django.views.decorators.http import require_POST, require_GET
from person.battle_way import battleWays

# Create your views here.

class Heros(object):
    def __init__(self, id):
        self.hp = 0
        self.name = ''
        self.id = 0
        self.skills = []

        self.init_data(id)

    def init_data(self, id):
        data = config.heros.get(id)
        skills = config.hero_skill.get(id)
        if not data or not skills:
            return
        self.hp = data.hp
        self.name = data.name
        self.id = data.id
        self.skills = skills

    def add_hp(self, hp):
        self.hp += hp
        if self.hp < 0:
            self.hp = 0

    def random_skill(self):
        return random.choice(self.skills)


class Skill(object):
    def __init__(self, skill_id):
        self.skill = config.skills.get(skill_id)

    def can_use(self, attacker):
        """
        可能和冷却时间、状态有关
        """
        return True

    def cal_hit_num(self, attacker, defender):
        """
        计算伤害值
        """
        return self.skill.attack


def have_a_battle(fighter_id_1, fighter_id_2, battle_way):
    """
    have_a_battle(1, 2, 'random_battle')
    """
    battle_meth = battleWays.get_way(battle_way)
    if not battle_meth:
        return 'error battle_way'
    if not (config.heros.get(fighter_id_1) and config.heros.get(fighter_id_2)):
        return
    battle = battle_meth(Heros(fighter_id_1), Heros(fighter_id_2))
    winner = battle.battle()
    print(f"winner name is {winner.name}")

