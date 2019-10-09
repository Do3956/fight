from lib.config import config
import random
from person.skills import allSkills


class Hero(object):
    def __init__(self, hero_id):
        self.data = config.heros.get(hero_id)
        self.skill_ids = config.hero_skill.get(self.data.id)
        self.skill = None

    def random_skill(self):
        return random.choice(self.skill_ids)

    def set_skill(self, skill_id, defender):
        self.skill = allSkills.get_skill_class(skill_id)(skill_id, defender)

    def add_hp(self, hp):
        self.data.hp += hp
        if self.data.hp < 0:
            self.data.hp = 0

    def fight(self):
        return self.skill.executeCommand()


class HeroMaster(Hero):
    """
    法师
    """

class WarriorMaster(Hero):
    """
    战士
    """

    # def __init__(self, hero_id):
    #     super(WarriorMaster, self).__init__(hero_id)

class AllHeros(object):
    heros = {
        'HeroMaster': HeroMaster,
        'WarriorMaster': WarriorMaster,
    }

    @classmethod
    def get_hero(cls, hero_id):
        hero_class = cls.heros.get(config.heros.get(hero_id).profession)
        hero = hero_class(hero_id)
        return hero

    @classmethod
    def get_hero_class(cls, hero_id):
        # import pdb;pdb.set_trace()
        hero_class = cls.heros.get(config.heros.get(hero_id).profession)
        return hero_class


allHeros = AllHeros()
