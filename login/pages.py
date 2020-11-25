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

def my_view(request):
    person = {
        'user':[
        ]
    }
    with open(os.path.join(settings.PROJECT_DIR,'oTree/collect_static','user.csv'),'r',encoding="gbk") as f:
        reader = csv.reader(f)
        reader_row = next(reader)
        # row代表每一列
        for row in reader:
            person['user'].append({row[0].split()[0]:row[0].split()[1]})


    person_str = json.dumps(person)
    response = HttpResponse(person_str , content_type='application/json; charset=utf-8')
    # print(person['user'])
    return response

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
