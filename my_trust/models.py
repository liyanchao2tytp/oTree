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
    name_in_url = 'my_trust'
    players_per_group = 6
    num_rounds = 3

    endowment = c(100)

    multiplication_factor_b1 = 3
    multiplication_factor_b2 = 5


class Subsession(BaseSubsession):
    def do_my_shuffle(self):
        print("测试能不能乖乖听话")
        # 要是分组就要在subsession这个类里面，但是creating_session是在这里执行的。watir页面要想调用方法，就必须在group里面。
        id_list1 = self.session.vars['to_trust_id']
        id_order_player = self.session.vars['to_trust_player']
        sub_player = self.session.vars['to_trust_id_before']
        # for m, n in id_list, id_order_player:
        #     sub_player[m] = n

        # for m,id in

        # 然后根据已经排序好的对象序列进行分组
        print(id_order_player)
        print(type(id_order_player))
        print(id_order_player[0][0])
        id_list = id_order_player
        print("打印participant的id_in_session")
        print(sub_player)
        print(type(sub_player))
        for p in self.get_players():
            p.payoff_play=sub_player[p.participant.id_in_session]
            print(p.payoff_play)
            print(p.participant.id_in_session)
        print(id_order_player)
        print(id_order_player[0][0])
        new_structure = [
            # [id_order_player[0][0], id_order_player[12][0], id_order_player[6][0]],
            # [id_order_player[1][0], id_order_player[13][0], id_order_player[7][0]],
            # [id_order_player[2][0], id_order_player[14][0], id_order_player[8][0]],
            # [id_order_player[3][0], id_order_player[15][0], id_order_player[9][0]],
            # [id_order_player[4][0], id_order_player[16][0], id_order_player[10][0]],
            # [id_order_player[5][0], id_order_player[17][0], id_order_player[11][0]],

            [id_order_player[0][0], id_order_player[4][0], id_order_player[2][0]],
            [id_order_player[1][0], id_order_player[5][0], id_order_player[3][0]],

        ]
        matrix = self.set_group_matrix(new_structure)

        #print(id_list[166][1])
    def creating_session(self):
        matrix = self.get_group_matrix()


class Group(BaseGroup):
    sent_amount_b1 = models.CurrencyField(
        label='你要发给公司B1多少',
    )
    sent_amount_b2 = models.CurrencyField(
        label='你要发给公司B2多少',

    )

    sent_back_amount_b1 = models.CurrencyField(
        label='你要返回给A多少'
    )
    sent_back_amount_b2 = models.CurrencyField(
        label='你要返回给A多少'
    )

    def sent_back_amount_b1_choices(self):
        return currency_range(
            c(0),
            self.sent_amount_b1 * Constants.multiplication_factor_b1,
            c(1),
        )

    def sent_back_amount_b2_choices(self):
        return currency_range(
            c(0),
            self.sent_amount_b2 * Constants.multiplication_factor_b2,
            c(1),
        )

    def set_payoffs(self):
        A = self.get_player_by_id(1)
        B1 = self.get_player_by_id(2)
        B2 = self.get_player_by_id(3)
        A.payoff = Constants.endowment - self.sent_amount_b1 - self.sent_amount_b2 + self.sent_back_amount_b1 + self.sent_back_amount_b2
        B1.payoff = self.sent_amount_b1 * Constants.multiplication_factor_b1 - self.sent_back_amount_b1
        B2.payoff = self.sent_amount_b2 * Constants.multiplication_factor_b2 - self.sent_back_amount_b2


class Player(BasePlayer):
    # 用来记录用户上一局的投钱数
    payoff_play = models.CurrencyField(initial=0)

    def role(self):
        return {1: 'B1', 2: 'B2', 3: 'A'}[self.id_in_group]

    def demo(self):
        print("得到其他玩家")
        i = self.get_others_in_subsession()
        print(i)
        m = self.get_others_in_group()
        print(m)
