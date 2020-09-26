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

doc = """
This is a one-period public goods game with 3 players.
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods'
    players_per_group = 18

    # 设置两次实验
    num_rounds = 2

    instructions_template = 'public_goods/instructions.html'

    # """Amount allocated to each player"""
    endowment = c(20)
    multiplier = 0.6


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
        playes_id=[]
        playes_payoff=[]
        for p in self.get_players():
            # 这里设置payoff，就是玩家转的钱
            playes_id.append(p.id_in_group)

            p.payoff = (Constants.endowment - p.contribution) + self.individual_share
            playes_payoff.append(p.payoff)
            #总投入设置
            if(self.round_number==2):
                 p.player_pay=p.contribution+p.in_round(1).contribution

        #通过session来对id进行排序
        # for p in self.get_players():
        #     p.participant.id_in_session
        #payoffs = sorted([p.payoff for p in self.get_players()])

        #dict_plays=[

        #]



        #self.session.vars['player_id']=playes_id
        #self.session.vars['playes_payoff']=playes_payoff
        #print(self.session.vars['player_id'])
        #print(self.session.vars['playes_payoff'])
        #participant_id
        player={}
        player_id_list={}
        for p in self.get_players():
           player[p.participant_id]=p.player_pay
           player_id_list[p.id_in_group]=p.player_pay
        print("对列表进行排序")
        print(player)
        #将没有排序前的传递到这里
        self.session.vars['to_trust_id_before']=player_id_list
        #d_order = sorted(player.items(), key=lambda x: x[1], reverse=False)
        id_order_player=sorted(player_id_list.items(), key=lambda x: x[1], reverse=True)
        #获取id排列顺序
        id_list=list(id_order_player)
        print("d_order排序")
        #print(d_order)
        #player=sorted(player.items(), key=lambda kv: (kv[1], kv[0]))
        #可以直接获取id
        self.session.vars['to_trust_id']=id_list
        #这是捐献的值
        self.session.vars['to_trust_player']=id_order_player
        print(player)
        #问题，可以传入，但是不能获取。
        #self.session.vars['public_goods'] = payoffs
        #如果可以获取
    # def set_payoff(self):
    #         # play = {}
            # for i in sum(1, 6):
            #     play[i] = self.session.vars[i]
            # print("对play进行排序")
            # print(play)
            # sorted(play.items(), key=lambda kv: (kv[1], kv[0]))
            # print(play)
            #依次保存play的key

            # for p,i in self.get_players(),play.items():
            #     p.id_in_group=i
            #     p.payoff=



play_demo=[]
class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment, doc="""The amount contributed by the player"""
    )
    # 默认用户的初始值为0
    player_pay = models.CurrencyField(initial=0)

    # count=print(Group.individual_share)
    def set_app(self):
        print("检测是否进入了这里")
        #self.player_pay = self.payoff
        self.player_pay=self.contribution+self.player_pay
        #self.session.vars[]
        self.session.vars[self.id_in_group] = self.payoff
    # def role(self):
    #     if self.id_in_group ==
