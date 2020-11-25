'''
Author: lyc
Date: 2020-11-23 16:59:21
LastEditors: lyc
LastEditTime: 2020-11-24 17:56:59
Description: file content
'''
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.http import HttpResponse
import json
import csv
import os
import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def my_view(request):
    # player_number = request.POST.get('player_number')
    # in_name = request.POST.get('inName')
    # in_word = request.Post.get('inWord')
    #
    # # 读取 指定路径下文件的数据 并将数据拼接到person中
    # with open(os.path.join(settings.PROJECT_DIR,'oTree/collect_static','user.csv'),'r',encoding="gbk") as f:
    #     reader = csv.reader(f)
    #     reader_row = next(reader)
    #     # row代表每一列
    #     for row in reader:
    #         if row[0].split()[0] == in_name and in_word == row[0].split()[1]:
    #             return render('one_questionaire/MyPage')
    #

    # result = False
    # response = JsonRest(result , content_type='application/json; charset=utf-8')
    # return response
    return render(request,'MyPage')
# 动态
class MyPage(Page):
    form_model = 'player'

    def vars_for_template(self):

        player_number = settings.SESSION_CONFIGS[0]['num_demo_participants']
        if self.player.id%player_number == 0:
            id = 3
        else :
            id = self.player.id%player_number
        return dict(
            id = id-1
        )




page_sequence = [MyPage]
