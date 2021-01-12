from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse


# class checkMD(MiddlewareMixin):
#     def process_request(self,request):
#         print('方法执行了奥')

def checkMD(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.Meta)
        print("执行了")