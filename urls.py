'''
Author: lyc
Date: 2020-11-08 12:53:53
LastEditors: lyc
LastEditTime: 2020-11-24 15:49:43
Description: file content
'''
from django.urls import path
from otree.urls import urlpatterns
import login
urlpatterns.append(path('my_view/', login.pages.my_view))

urlpatterns.append(path('login/<int:player_id>/<str:slug>',login.pages.login))

urlpatterns.append(path('checkLogin/',login.pages.checkLogin))

urlpatterns.append(path('checkSession/',login.pages.checkSession))