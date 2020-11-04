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
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'one_questionnaire'
    players_per_group = 3
    num_rounds = 1

    answer = [[1,'A'],[2,'B']]
    


class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    constants = Constants()
    answer = constants.answer
    q1 = models.IntegerField(label='', choices=answer, widget=widgets.RadioSelectHorizontal)
    q2 = models.IntegerField(label='', choices=answer, widget=widgets.RadioSelectHorizontal)
    q3 = models.IntegerField(label='', choices=answer, widget=widgets.RadioSelectHorizontal)
    q4 = models.IntegerField(label='', choices=answer, widget=widgets.RadioSelectHorizontal)
    q5 = models.IntegerField(label='', choices=answer, widget=widgets.RadioSelectHorizontal)
    q6 = models.IntegerField(label='', choices=answer, widget=widgets.RadioSelectHorizontal)
    q7 = models.IntegerField(label='', choices=answer, widget=widgets.RadioSelectHorizontal)
    q8 = models.IntegerField(label='', choices=answer, widget=widgets.RadioSelectHorizontal)
    q9 = models.IntegerField(label='', choices=answer, widget=widgets.RadioSelectHorizontal)
    q10 = models.IntegerField(label='', choices=answer, widget=widgets.RadioSelectHorizontal)

