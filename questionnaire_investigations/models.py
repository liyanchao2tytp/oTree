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
    answer_age = []
    answer_age.append("不想说")
    for i in range(1, 100):
        answer_age.append(str(i))
    name_in_url = 'questionnaire_investigations'
    players_per_group = None
    num_rounds = 1
    answer_sex = [[0, "女性"], [1, "男性"]]
    answer_race = [[0, "少数民族"], [1, "汉族"]]
    answer_economic = [[0, "不是"], [1, "是"]]
    answer_communist = [[0, "不是"], [1, "是"]]
    answer_ganbu = [[0, "不是"], [1, "是"]]
    answer_aid = [[0, "没有"], [1, "有"], [2, "不方便透露"]]
    answer_work = [[0, "没有"], [1, "有"]]
    answer_experience = [[0, "没有"], [1, "有"]]
    answer_citizen = [[0, "农村"], [1, "城市"]]
    answer_mosttrust = [[0, "第一种说法"], [1, "第二种说法"]]
    answer_mostfair = [[0, "第一种说法"], [1, "第二种说法"]]
    answer_mosthelp = [[0, "第一种说法"], [1, "第二种说法"]]
    answer_victim = [[0, "没有"], [1, "有"]]
    answer_xueli = [[1, "小学"], [2, "初中"], [3, "高中"], [4, "大专"], [5, "本科"], [6, "研究生及以上"], ]
    # age = models.IntegerField(label="年龄")
    # answer_sex=[[0,"女性"],[1,"男性"]]
    #
    # sex = models.StringField(label="性别",choices=answer_sex,widget=widgets.RadioSelectHorizontal)


class Subsession(BaseSubsession):
    def sub_session(self):
        player_four=self.session.vars["player_off"]
        for g in self.get_groups():
            for p in self.get_players():
                for m in player_four.keys():
                    if(p.participant_id==m):
                        p.payoff_demo=player_four[m]
                        p.payoff=p.payoff_demo

    pass


class Group(BaseGroup):
    def set_payoff(self):
        buyer = self.get_player_by_role('buyer')
        print(buyer.decision)

class Player(BasePlayer):
    answer_age = Constants.answer_age
    hoesty1 = models.IntegerField(label="请问您在游戏过程中对游戏币的数量（或者资金的多少）的在意程度是", widget=widgets.Slider, min=0, max=10)
    hoesty2 = models.IntegerField(label="请问您个人认为自己对游戏过程的理解程度是", widget=widgets.Slider, min=0, max=10)
    age = models.StringField(label="年龄", choices=answer_age)
    answer_sex = Constants.answer_sex
    sex = models.IntegerField(label="性别", choices=answer_sex, widget=widgets.RadioSelectHorizontal)
    answer_race = Constants.answer_race
    race = models.IntegerField(label="民族", choices=answer_race, widget=widgets.RadioSelectHorizontal)
    answer_economic = Constants.answer_economic
    economic = models.IntegerField(label="是否是经济类专业的学生", choices=answer_economic, widget=widgets.RadioSelectHorizontal)
    highest = models.StringField(label="期望获得的最高教育", choices=['小学', '初中', '高中', '大专', '本科', '研究生及以上'])
    answer_communist = Constants.answer_communist
    communist = models.IntegerField(label="实验对象是否是党员", choices=answer_communist, widget=widgets.RadioSelectHorizontal)
    answer_ganbu = Constants.answer_ganbu
    ganbu = models.IntegerField(label="是否是学生干部", choices=answer_ganbu, widget=widgets.RadioSelectHorizontal)

    sfindex = models.IntegerField(label="对上述党员和班级两个干部加总标准化")
    # sfindex=communist(int)+ganbu(int)
    answer_xueli = Constants.answer_xueli
    father = models.IntegerField(label="实验父亲的学历", choices=answer_xueli)
    mother = models.IntegerField(label="实验母亲的学历", choices=answer_xueli)
    fmindex = models.IntegerField(label="对上述父母学历变量的加总标准化")
    answer_aid = Constants.answer_aid
    aid = models.IntegerField(label="是否有助学贷款", choices=answer_aid, widget=widgets.RadioSelectHorizontal)
    answer_work = Constants.answer_work
    work = models.IntegerField(label="有没有兼职", choices=answer_work, widget=widgets.RadioSelectHorizontal)
    answer_experience = Constants.answer_experience
    experience = models.IntegerField(label="是否参加过实验", choices=answer_experience, widget=widgets.RadioSelectHorizontal)
    studentstatus = models.StringField(label="年级", choices=['2017', '2018', '2019', '2020'])
    answer_citizen = Constants.answer_communist
    citizen = models.IntegerField(label="来自农村还是城市", choices=answer_citizen, widget=widgets.RadioSelectHorizontal)
    hhinc = models.StringField(label="年收入水平", choices=['不方便透露', '贫穷', '温饱', '小康', '富裕', ])

    answer_mosttrust = Constants.answer_mosttrust
    mosstrust = models.IntegerField(label="下面的说法你相对赞成哪种？1.一般而言，大部分人是值得信任的，2.一般而言，再和大多数打交道怎么谨慎也不为过",
                                    choices=answer_mosttrust, widget=widgets.RadioSelectHorizontal)
    answer_mostfair = Constants.answer_mostfair
    mostfair = models.IntegerField(label="下面说法你相对赞成那种？1.这个世界上大部分人会客观公正的对待你；2，这个世界上大部分人在有机会的时候会试着利用你",
                                   choices=answer_mostfair, widget=widgets.RadioSelectHorizontal)
    answer_mosthelp = Constants.answer_mosthelp
    mosthelp = models.IntegerField(label="下面的说法你相对赞成哪一种？1.人们大多数的时候还是乐于助人的；2.他们只不过是为自己谋利而已", choices=answer_mosthelp,
                                   widget=widgets.RadioSelectHorizontal)
    trustindex = models.IntegerField(label="前面3个变量的加总标准化")

    strangers = models.IntegerField(label="你会相信陌生人的言行吗", widget=widgets.Slider, min=1, max=6)
    trustworthy = models.IntegerField(label="你举得自己是应该可以值得信赖的人吗", widget=widgets.Slider, min=1, max=6)
    hoesty = models.IntegerField(label="你是否是一个诚实的人", widget=widgets.Slider, min=0, max=10)

    leavedoor = models.IntegerField(label="你是否离开宿舍时经常不锁门", widget=widgets.Slider, min=1, max=5)
    loanstrange = models.IntegerField(label="你是否经常借钱给陌生人", widget=widgets.Slider, min=1, max=5)
    loanmoney = models.IntegerField(label="你经常借钱给朋友或同学么？", widget=widgets.Slider, min=1, max=5)

    behaviorindex = models.IntegerField(label="前面3个加总的标准化")
    answer_victim = Constants.answer_victim
    victim = models.IntegerField(label="最近一年你是否遇到以下情形中的任何一种:被偷，被人攻击，被诈骗，被诬陷，被抢劫，受到家庭暴力", choices=answer_victim,
                                 widget=widgets.RadioSelectHorizontal)
    payoff_demo = models.CurrencyField(initial=0, label="你最终获得的筹码")
    # def forindex(self):
    #   self.sfindex=self.communist+self.ganbu
    #   self.fmindex=self.father+self.mother
    #   self.trustind=self.mosstrust+self.mostfair+self.mosthelp
    #   self.behaviorindex=self.leavedoor+self.loanstrange+self.loanmoney
    #























