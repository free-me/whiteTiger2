from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from app.modelsDir.userModels import *
from mongoengine.queryset.visitor import Q

class login(View):
    def get(self,request):
        return HttpResponse("请使用POST登录！！！")
    def post(self, requests):
        print(requests.POST['email'], requests.POST['passWord'])
        if requests.POST['email'] != '' and requests.POST['passWord'] != '':
            # result = users.objects.filter(email=requests.POST['email'],passWord=requests.POST['passWord']).first()
            result = users.objects(
                Q(email=requests.POST['email']) & Q(passWord=requests.POST['passWord'])).first()  # 判断用户名密码是否正确
            print(result)
            if result != None:
                context = {}
                context['url'] = requests.path
                context['email'] = result.userName
                # response.set_cookie('userName', result.userName)
                return render(requests, 'app/index.html', context)
            else:
                return render(requests, 'app/login.html')

