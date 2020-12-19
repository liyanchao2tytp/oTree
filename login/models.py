'''
Author: lyc
Date: 2020-12-15 11:27:43
LastEditors: lyc
LastEditTime: 2020-12-15 11:42:26
Description: file content
'''
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'login'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

class User(models.Model):
    userName = models.StringField(max_length=30)
    passWord = models.StringField(max_length=30)

class UserInfo(models.Model):
    user=models.OneToOneField(User)
    name=models.CharField('姓名',max_length=32)

    def __str__(self):
        return self.name