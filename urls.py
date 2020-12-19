'''
Author: lyc
Date: 2020-11-08 12:53:53
LastEditors: lyc
LastEditTime: 2020-12-15 11:43:37
Description: file content
'''
from django.urls import path
from otree.urls import urlpatterns
import login
urlpatterns.append(
  path('my_view/', login.pages.my_view),
  url(r'^accounts/login/', views.accounts_login),
  url(r'^accounts/logout/', views.accounts_logout),
)