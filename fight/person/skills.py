from lib.config import config
from abc import ABC, abstractmethod
import copy


class Skill(ABC):
    """
    命令设计模式
    1. 必须有接收者
    2. 必须实现一个以上的命令 abstractmethod
    3. 把该类绑在调用者上面

    根据实际情况调整，不一定要满足所有条件
    """

    def __init__(self, skill_id):
        self.data = config.skills.get(skill_id)

    def can_use(self):
        """
        可能和冷却时间、状态有关
        """
        return True

    @abstractmethod
    def execute(self, receiver: 'Hero') -> int:
        """
        使用技能
        abstractmethod 必须要有返回值
        """


class Skill1(Skill):
    """
    """

    def execute(self, receiver: 'Hero'):
        """
        计算属性
        """
        return self.data.attack


