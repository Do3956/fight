from person.models import Heros
from person.models import Skills
from person.models import Hero_Skill


class Config:
    """
    加载配置至内存
    """
    def __init__(self):
        self.heros = {}
        self.skills = {}
        self.hero_skill = {}

        self.load_data()

    def load_data(self):
        heros = Heros.load_data()
        skills = Skills.load_data()
        hero_skill = Hero_Skill.load_data()

        self.heros = heros
        self.skills = skills
        self.hero_skill = hero_skill

    def check_data(self):
        """
        检测配置是否正常
        """
        pass


config = Config()
