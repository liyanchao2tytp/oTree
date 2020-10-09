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
    name_in_url = 'pre_public_goods'
    players_per_group = 6
    num_rounds = 1
    instructions_template = 'pre_public_goods/instructions.html'
    endowment = c(100)
    multiplier = 0.4


class Subsession(BaseSubsession):
    def vars_for_admin_report(self):
        contributions = [
            p.contribution for p in self.get_players() if p.contribution != None
        ]
        if contributions:
            return dict(
                # 返回平均，最大和最小值
                avg_contribution=sum(contributions) / len(contributions),
                min_contribution=min(contributions),
                max_contribution=max(contributions),
            )
        else:
            return dict(
                avg_contribution='(no data)',
                min_contribution='(no data)',
                max_contribution='(no data)',
            )


class Group(BaseGroup):
    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

    def set_payoffs(self):
        # 这里是total_contribution的值，是总的游戏币
        self.total_contribution = sum([p.contribution for p in self.get_players()])

        # 这里是返还的游戏币
        self.individual_share = (
                self.total_contribution * Constants.multiplier
            # / Constants.players_per_group
        )
        playes_id = []
        playes_payoff = []
        for p in self.get_players():
            # 这里设置payoff，就是玩家转的钱
            playes_id.append(p.id_in_group)

            p.payoff = (Constants.endowment - p.contribution) + self.individual_share
            playes_payoff.append(p.payoff)
            # 总投入设置
            if (self.round_number == 2):
                p.player_pay = p.contribution + p.in_round(1).contribution
                p.payoff_all = p.payoff + p.in_round(1).payoff
        # 通过session来对id进行排序
        # for p in self.get_players():
        #     p.participant.id_in_session
        # payoffs = sorted([p.payoff for p in self.get_players()])

        # dict_plays=[
        # 这里获取到投入的的值,从第一轮到第round_number轮
        if (self.round_number == Constants.num_rounds):
            # 遍历值，将其他的值全部加到这里
            for p in self.get_players():
                for i in range(1, Constants.num_rounds):
                    p.player_pay = p.player_pay + p.in_round(i).contribution
                    # 4轮结束后，看看能不能存储
                    print(p.player_pay)


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment, doc="""The amount contributed by the player"""
    )
    # 默认用户的初始值为0
    player_pay = models.CurrencyField(initial=0)
    ##############################
    payoff_all = models.CurrencyField(initial=0)

    # count=print(Group.individual_share)
    def set_app(self):
        print("检测是否进入了这里")
        # self.player_pay = self.payoff
        self.player_pay = self.contribution + self.player_pay
        # self.session.vars[]
        self.session.vars[self.id_in_group] = self.payoff
    # def role(self):
    #     if self.id_in_group ==
