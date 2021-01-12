'''
Author: lyc
Date: 2020-11-23 16:59:21
LastEditors: lyc
LastEditTime: 2021-01-09 21:57:46
Description: file content
'''
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.http import HttpResponse,JsonResponse
import json
import csv
import os
import settings

def my_view(request):

    request.session['test'] = '1222222323'
    print(request.session.get('test'))

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

#TODO 跳转login 页面
def login(request,player_id, slug ,*args, **kwargs):
    return render(request,'login/login.html')

@csrf_exempt
def checkSession(request):
    #TODO 如果有session值 且正确
    print(request.session.get('token'))
    if request.session.get('token'):
        return JsonResponse({
            'is_login': 'OK'
        })
    else:
        return JsonResponse({
            'is_login':'ERROR'
        })


#TODO 提交表单 数据检查
@csrf_exempt
def checkLogin(request):
    usrname = request.POST.get('usrname')
    password = request.POST.get('password')
    slug = request.POST.get('slug')
    play_id = request.POST.get('play_id')
    url_pre = request.POST.get('url_pre')


    # 读取 指定路径下文件的数据
    with open(os.path.join(settings.PROJECT_DIR, 'oTree/collect_static', 'user.csv'), 'r', encoding="gbk") as f:
        reader = csv.reader(f)
        reader_row = next(reader)
        # 记录第几次循环
        num = 0
        # row代表每一列
        for row in reader:
            num = num + 1
            if num == int(play_id) and row[0].split()[0] == usrname and password == row[0].split()[1]:
                print('------------ 用户名密码存在 --------------')
                print(num,row[0].split()[0],row[0].split()[1])
                # 登录成功 存session
                request.session['token'] = slug
                break;
            else:
                print('------------bbb 用户名密码不存在 --------------')
                print(num,row[0].split()[0], row[0].split()[1])



    print(usrname,password,'-',slug,'-',play_id)
    print('{}/InitializeParticipant/{}'.format(url_pre,slug))
    return redirect('{}/InitializeParticipant/{}'.format(url_pre,slug))


# 动态
class MyPage(Page):
    form_model = 'player'
    def is_displayed(self):
        print(self.request)
        return True
    def vars_for_template(self):

        player_number = settings.SESSION_CONFIGS[0]['num_demo_participants']
        if self.player.id%player_number == 0:
            id = 3
        else :
            id = self.player.id%player_number
        return dict(
            id = id
        )




page_sequence = [MyPage]
