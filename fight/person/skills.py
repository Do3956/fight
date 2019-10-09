from lib.config import config
from abc import ABC, abstractmethod


class Skill(ABC):
    """
    命令设计模式
    1. 必须有接收者
    2. 必须实现一个以上的命令 abstractmethod
    3. 把该类绑在调用者上面
    """

    def __init__(self, skill_id, receiver):
        self.data = config.skills.get(skill_id)
        self.receiver = receiver

    def can_use(self):
        """
        可能和冷却时间、状态有关
        """
        return True

    @abstractmethod
    def executeCommand(self):
        """
        具体命令
        """


class SkillHit(Skill):
    """
    伤害技能
    """

    # def __init__(self, skill_id, receiver):
    #     super(SkillHit, self).__init__(skill_id, receiver)

    def executeCommand(self):
        """
        计算伤害值
        """
        return self.data.attack


class AllSkills(object):
    skills = {
        'hit': SkillHit,
    }

    @classmethod
    def get_skill_class(cls, skill_id):
        skill_class = cls.skills.get(config.skills.get(skill_id).effect)
        return skill_class


allSkills = AllSkills()
