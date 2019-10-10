from django.db import models
from collections import defaultdict
# Create your models here.


class ConfigModel(object):
    @classmethod
    def load_data(cls):
        result = {}
        datas = cls.objects.all()
        for d in datas:
            result[d.id] = d
        return result


class Heros(models.Model, ConfigModel):
    PROFESSION = (
        ('can_use', '可以使用'),
    )
    name = models.CharField('角色名', null=False, default='', max_length=20)
    _class = models.CharField('代码里对应的类名', null=False, default='', max_length=20)
    hp = models.PositiveIntegerField(
        '血量', null=False, default=0)
    # profession = models.CharField(
    #     '职业', null=False, choices=PROFESSION, max_length=20)



class Skills(models.Model, ConfigModel):
    name = models.CharField('技能名称', null=False, max_length=20)
    _class = models.CharField('代码里对应的类名', null=False, default='', max_length=20)
    attack = models.PositiveIntegerField(
        '攻击力', null=False, default=0)


class Hero_Skill(models.Model, ConfigModel):
    skill_id = models.PositiveIntegerField(
        'Skills', null=False, default=0)
    hero_id = models.PositiveIntegerField(
        'Heros', null=False, default=0)

    @classmethod
    def load_data(cls):
        result = defaultdict(list)
        datas = cls.objects.all()
        for d in datas:
            result[d.hero_id].append(d.skill_id)
        return result
