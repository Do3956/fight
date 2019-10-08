import random

from django.shortcuts import render
from lib.config import config
from lib.constants import BattleStatus
from lib.constants import BattleWay
from django.views.decorators.http import require_POST, require_GET


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
        print(2222, self.hp)
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


class Battle(object):
    def __init__(self, fighter_id_1, fighter_id_2):
        self.battle_status = BattleStatus.prepare
        self.fighter_1 = Heros(fighter_id_1)
        self.fighter_2 = Heros(fighter_id_2)

    def hit(self, skill_id, attacker, defender):
        skill = Skill(skill_id)
        can_use = skill.can_use(attacker)
        if not can_use:
            return
        hit = skill.cal_hit_num(attacker, defender)
        defender.add_hp(-hit)
        return defender.hp

    def random_fight(self):
        self.battle_status = BattleStatus.ing
        attacker, defender = self.fighter_1, self.fighter_2
        while True:
            hp = self.hit(attacker.random_skill(), attacker, defender)
            if hp is not None and hp <= 0:
                self.battle_status = BattleStatus.end
                return attacker
            attacker, defender = defender, attacker


def have_a_battle(fighter_id_1, fighter_id_2, battle_way):
    if battle_way[0] == '_' or not battle_way in BattleWay.__dict__:
        return
    if not (config.heros.get(fighter_id_1) and config.heros.get(fighter_id_2)):
        return
    battle = Battle(fighter_id_1, fighter_id_2)
    winner = battle.random_fight()
    print(f"winner name is {winner.name}")


if __name__ == "__main__":
    random_fight(1, 2)
