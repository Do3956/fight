from lib.config import config
import random
from abc import ABC, abstractmethod
from person import skills as module_skills


class Hero(ABC):
    def __init__(self, hero_id):
        self.data = config.heros.get(hero_id)

        skill_configs = config.skills
        skill_ids = config.hero_skill.get(self.data.id)
        self.skills = list(map(lambda skill_id: getattr(
            module_skills, skill_configs[skill_id]._class)(skill_id), skill_ids))

    def random_skill(self):
        return random.choice(self.skills)

    def add_hp(self, hp):
        self.data.hp += hp
        if self.data.hp < 0:
            self.data.hp = 0

    def fight(self, defender, *agrs, **kw):
        skill = self.random_skill()
        return skill.execute(defender)


class HeroMaster(Hero):
    """
    法师
    """


class HeroWarrior(Hero):
    """
    战士
    """

    def add_hp(self, hp):
        super().add_hp(hp)
        super().add_hp(self.get_arm())

    def get_arm(self)->int:
        return 0


class HeroAssassin(Hero):
    """
    刺客
    """

    # def __init__(self, hero_id):
    #     super(WarriorMaster, self).__init__(hero_id)

# class HeroManager(object):
#     heros = {
#         'HeroMaster': HeroMaster,
#         'HeroWarrior': HeroWarrior,
#         'HeroKiller': HeroAssassin,
#     }

#     @classmethod
#     def get_hero(cls, hero_id):
#         hero_class = cls.heros.get(config.heros.get(hero_id).profession)
#         hero = hero_class(hero_id)
#         return hero

#     # @classmethod
#     # def get_hero_class(cls, hero_id):
#     #     # import pdb;pdb.set_trace()
#     #     hero_class = cls.heros.get(config.heros.get(hero_id).profession)
#     #     return hero_class

