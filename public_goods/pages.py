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
            round=self.round_number

        )


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    body_text = "Waiting for other participants to contribute."

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
        return dict(total_earnings=self.group.total_contribution * Constants.multiplier)


page_sequence = [Contribute, ResultsWaitPage, Results]
# Introduction,
