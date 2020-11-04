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
    players_per_group = 3
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
        payoff_all_list = self.session.vars['to_trust_payoff_all']
        payoff_avg = self.session.vars['to_trust_payoff_avg']
        print(sub_player)
        # for m, n in id_list, id_order_player:
        #     sub_player[m] = n
        # for m,id in
        # 然后根据已经排序好的对象序列进行分组
        # for g in self.get_groups():

        id_list = id_order_player
        for p in self.get_players():
            p.payoff_play = sub_player[p.participant.id_in_session]

            ###################修改的值
            p.payoff_public = payoff_all_list[p.participant.id_in_session]
            p.payoff_avg_public = payoff_avg[p.participant.id_in_session]

        new_structure = [
            # [id_order_player[0][0], id_order_player[12][0], id_order_player[6][0]],
            # [id_order_player[1][0], id_order_player[13][0], id_order_player[7][0]],
            # [id_order_player[2][0], id_order_player[14][0], id_order_player[8][0]],
            # [id_order_player[3][0], id_order_player[15][0], id_order_player[9][0]],
            # [id_order_player[4][0], id_order_player[16][0], id_order_player[10][0]],
            # [id_order_player[5][0], id_order_player[17][0], id_order_player[11][0]],

            # [id_order_player[0][0], id_order_player[2][0], id_order_player[1][0]],
            [id_order_player[0][0], id_order_player[4][0], id_order_player[2][0]],
            [id_order_player[1][0], id_order_player[5][0], id_order_player[3][0]],
        ]
        matrix = self.set_group_matrix(new_structure)
        for e in self.get_groups():
            for g in e.get_players():
                g.groups_id = g.group_id
        #print(id_order_player[1212][0])
    def creating_session(self):
        matrix = self.get_group_matrix()

    def get_dmeo(self):
        player_four = {}
        if self.round_number == Constants.num_rounds:
            print("打印是否可以进入到这里")
            for g in self.get_groups():
                for p in g.get_players():
                    players = p.in_previous_rounds()
                    # p.payoff_all_now=p.payoff
                    for m in players:
                        p.payoff_all_now = p.payoff_all_now + m.payoff
                    p.payoff_all_now = p.payoff_all_now + p.payoff
                    p.payoff_avg_now = p.payoff_all_now / Constants.num_rounds
                    p.payoff_truth = p.payoff_avg_now + p.payoff_avg_public
                    player_four[p.participant_id] = p.payoff_truth
                    print(p)
            for p in self.get_players():
                pass
                    # 存入payoff。
            print("测试")
            self.session.vars["player_off"] = player_four
            print(player_four)

            # demo = []
            # demo.append(111)
            # print(demo[12])

class Group(BaseGroup):
    sent_amount_b1 = models.CurrencyField(
        label='您要投资给B1企业多少资金',
    )
    sent_amount_b2 = models.CurrencyField(
        label='您要投资给B2企业多少资金',

    )

    sent_back_amount_b1 = models.CurrencyField(
        label='您要返还给A企业多少资金'
    )
    sent_back_amount_b2 = models.CurrencyField(
        label='您要返还给A企业多少资金'
    )

    # 角色A 期待返回的金额
    A_expect_back_point = models.CurrencyField(initial=0,label='您期待对方返还的资金额是多少')


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
        B1 = self.get_player_by_id(1)
        B2 = self.get_player_by_id(2)
        A = self.get_player_by_id(3)
        A.payoff = Constants.endowment - self.sent_amount_b1 - self.sent_amount_b2 + self.sent_back_amount_b1 + self.sent_back_amount_b2
        B1.payoff = self.sent_amount_b1 * Constants.multiplication_factor_b1 - self.sent_back_amount_b1
        B2.payoff = self.sent_amount_b2 * Constants.multiplication_factor_b2 - self.sent_back_amount_b2
        print('A-->{}  B---->{}   c---->{}'.format(A.payoff,B1.payoff,B2.payoff))

class Player(BasePlayer):
    # 用来记录用户上一局的投钱数
    payoff_play = models.CurrencyField(initial=0)
    ##########3
    payoff_public = models.CurrencyField(initial=0)
    # 这个是上一句的平均收入。
    payoff_avg_public = models.CurrencyField(initial=0)
    payoff_all_now = models.CurrencyField(initial=0)
    payoff_avg_now = models.CurrencyField(initial=0)
    payoff_truth = models.CurrencyField(initial=0)
    groups_id = models.IntegerField()
    def role(self):
        return {1: 'B1', 2: 'B2', 3: 'A'}[self.id_in_group]

    def demo(self):
        print("得到其他玩家")
        i = self.get_others_in_subsession()
        print(i)
        m = self.get_others_in_group()
        print(m)
