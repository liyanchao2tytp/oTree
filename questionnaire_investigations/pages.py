from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .models import Player

class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    body_text = "请等待其他玩家结束"
    pass


class Survey(Page):
    form_model = 'player'
    form_fields = ['hoesty1', 'hoesty2', 'age', 'sex', 'race', 'economic', 'highest', 'communist', 'ganbu', 'father',
                   'mother', 'aid', 'work',
                   'experience', 'studentstatus', 'citizen', 'hhinc']


class Gss(Page):
    form_model = 'player'
    form_fields = ['mosstrust', 'mostfair', 'mosthelp', 'strangers', 'trustworthy', 'hoesty', ]


class Trust(Page):
    form_model = 'player'
    form_fields = ['leavedoor', 'loanstrange', 'loanmoney', 'victim', ]


class Results(Page):
    def vars_for_template(self):
      #处理完成后量化
      self.player.sfindex=int(self.player.communist)+int(self.player.ganbu)
      self.player.fmindex=int(self.player.father)+int(self.player.mother)
      self.player.trustindex=int(self.player.mosthelp)+int(self.player.mostfair)+int(self.player.mosstrust)
      self.player.behaviorindex=int(self.player.leavedoor)+int(self.player.loanmoney)+int(self.player.loanstrange)

      #aa=self.player.sfindex
      b=self.player.sfindex



      return dict(
          demo=self.player.payoff_demo

    )



    #pass
    # form_model = 'player'
    # Player.sfindex=Player.communist+Player.ganbu
    # Player.fmindex=Player.father+Player.mother
    # Player.trustindex=Player.mosstrust+Player.mostfair+Player.mosthelp
    # form_fields = ['sfindex',]

class ResultsWaitPage2(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'sub_session'
    body_text = "请等待其他玩家结束"
    #body_text = "Waiting for other participants to contribute."

    def vars_for_template(self):
        #self.player.player_pay=self.player.player_pay+self.player.contribution ResultsWaitPage2,
        return dict(

        )
   #ResultsWaitPage2




page_sequence = [ResultsWaitPage2,MyPage, Survey, Gss, Trust, ResultsWaitPage, Results]
