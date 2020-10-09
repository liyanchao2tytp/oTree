from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


#
# class Send(Page):
#     form_model = 'player'
#     form_fields = ['sent_amount_b1', 'sent_amout_b2']
#     def is_displayed(self):
#         if self.player.role() != 'A':
#             return True
#
#
# class SendBack(Page):
#     form_model = 'player'
#     form_fields = ['sent_back_amount']
#
#     def is_displayed(self):
#         return self.player.id_in_group == 2
#
#     def vars_for_template(self):
#         return dict(
#             tripled_amount=self.player.sent_amount * Constants.multiplication_factor
#         )
#

class WaitForP1(WaitPage):
    pass


class A_pre(Page):
    def is_displayed(self):
        if self.player.role() == 'A':
            return True
        else:
            return False


class A_Ivest(Page):
    form_model = 'group'
    form_fields = ['sent_amount_b1', 'sent_amount_b2']

    def is_displayed(self):
        if self.player.role() == 'A':
            return True
        else:
            return False

    def vars_for_template(self):

        return dict(
            b1_in_public=self.group.get_player_by_id(1).payoff_play,
            b2_in_public=self.group.get_player_by_id(2).payoff_play
        )


class B1_Ivest(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount_b1']

    def is_displayed(self):
        if self.player.role() == 'B1':
            return True
        else:
            return False

    def vars_for_template(self):
        return dict(
            tripled_amount=self.group.sent_amount_b1 * Constants.multiplication_factor_b1
        )


class B2_Ivest(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount_b2']

    def is_displayed(self):
        if self.player.role() == 'B2':
            return True
        else:
            return False

    def vars_for_template(self):
        return dict(
            tripled_amount=self.group.sent_amount_b2 * Constants.multiplication_factor_b2
        )


class Waiter(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = "do_my_shuffle"


class Waiter2(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = "get_dmeo"


page_sequence = [Waiter, A_pre, A_Ivest, WaitForP1, B1_Ivest, B2_Ivest, ResultsWaitPage, Results, Waiter2]
