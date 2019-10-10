import copy
from person.models import Heros
from person.models import Skills
from person.models import Hero_Skill


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class Config:
    """
    加载配置至内存
    """

    def __init__(self):
        """
        初始化，让别人一眼可以知道什么类型
        """
        self._heros = {}
        self._skills = {}
        self._hero_skill = {}

        self.load_data()

    def load_data(self):
        """
        加载数据
        """
        heros = Heros.load_data()
        skills = Skills.load_data()
        hero_skill = Hero_Skill.load_data()

        if not self.check_config():
            return False

        self._heros = heros
        self._skills = skills
        self._hero_skill = hero_skill

        return True

    def check_config(self):
        """
        检测配置是否正常
        """
        return True

    @property
    def heros(self):
        return copy.deepcopy(self._heros)

    @heros.setter
    def heros(self, value):
        pass

    @property
    def skills(self):
        return copy.deepcopy(self._skills)

    @skills.setter
    def skills(self, value):
        pass

    @property
    def hero_skill(self):
        return copy.deepcopy(self._hero_skill)

    @hero_skill.setter
    def hero_skill(self, value):
        pass

config = Config()
