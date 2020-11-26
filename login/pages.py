'''
Author: lyc
Date: 2020-11-23 16:59:21
LastEditors: lyc
LastEditTime: 2020-11-26 13:22:52
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

# @csrf_exempt
# def my_view(request):
#
# #     读取 指定路径下文件的数据 并将数据拼接到person中
#     with open(os.path.join(settings.PROJECT_DIR,'oTree/collect_static','user.csv'),'r',encoding="gbk") as f:
#         reader = csv.reader(f)
#         reader_row = next(reader)
#         # row代表每一列
#         num = 0
#         for row in reader:
#             num=num+1
#             print(num)
#             if num == 1:
#                 print('yes')
#             # print(row[0].split()[0])
#     return HttpResponse('test')

# 动态
class MyPage(Page):
    form_model = 'player'
    form_fields = ['userName', 'passWord']

    def app_after_this_page(self, upcoming_apps):
        userName = self.player.userName
        passWord = self.player.passWord
        # 获取当前角色对应的id
        player_number = settings.SESSION_CONFIGS[0]['num_demo_participants']
        if self.player.id%player_number == 0:
            id = player_number
        else :
            id = self.player.id%player_number

        # 读取 指定路径下文件的数据
        with open(os.path.join(settings.PROJECT_DIR, 'oTree/collect_static', 'user.csv'), 'r', encoding="gbk") as f:
            reader = csv.reader(f)
            reader_row = next(reader)
            # 记录第几次循环
            num = 0
            # row代表每一列
            for row in reader:
                num = num+1

                if num == id and row[0].split()[0] == userName and passWord == row[0].split()[1]:
                    return upcoming_apps[0]
                else:
                    pass

    def vars_for_template(self):
        return dict(
            round = self.round_number
        )


page_sequence = [MyPage]
