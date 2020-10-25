from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player


class MyPage(Page):
   pass

class ResultsWaitPage(WaitPage):
    title_text = "等待页面"
    body_text = "请等待其他玩家结束"
    

class Results(Page):
    pass

class Survey(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
    def vars_for_template(self):
        list=[]
        q_list = []
        for i in range(10):
            q_list.append('100%的概率获得{}元'.format(50+(i*10)))
        return dict(
            q_list=q_list,
            same_question='50%的概率获得200元，50%的概率获得0元'
        )

page_sequence = [MyPage,Survey,Results]
