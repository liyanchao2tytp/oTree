from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player


class MyPage(Page):
   pass

class ResultsWaitPage(WaitPage):
    pass

class Results(Page):
    pass

class Survey(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
    def vars_for_template(self):
        list=[]
        q_list = []
        for i in range(10):
            q_list.append('100%的概率的{}元'.format(i))
        return dict(
            q_list=q_list,
            same_question='50%的概率获得20元，50%的概率获得0'
        )

page_sequence = [MyPage,Survey, Results]
