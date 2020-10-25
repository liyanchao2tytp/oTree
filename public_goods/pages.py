from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from .models import Player

class Introduction(Page):
    """Description of the game: How to play and returns expected"""

    pass


class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = 'player'
    form_fields = ['contribution']

    def vars_for_template(self):
        return dict(
            round=self.round_number,
            number=Constants.num_rounds
        )


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'
    title_text = "等待页面"
    body_text = "请耐心等待其他玩家做出选择"

    def vars_for_template(self):
        #self.player.player_pay=self.player.player_pay+self.player.contribution
        return dict(

        )

class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
        #Player.set_app(self)
        #self.player.set_app(self)
        # 将用户投入的钱进行保存

        #self.player.player_pay = self.player.contribution+self.player.player_pay
        return dict(
            total_earnings=self.group.total_contribution * Constants.multiplier,
            round=self.round_number,
            number=Constants.num_rounds
                    )
class Waiter2(WaitPage):
    title_text = "等待页面"
    body_text = "请等待其他玩家结束"
    wait_for_all_groups = True
    
    after_all_players_arrive = "get_dmeo"

page_sequence = [Contribute, ResultsWaitPage, Results,Waiter2]
# Introduction,
