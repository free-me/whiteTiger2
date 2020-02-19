from django.views.generic import View
from app.common.datetime import *
from app.modelsDir.userModels import *
from app.common.cmd5 import *

class register(View):
    def post(self, requests):
        userID=users.objects.count()+1 #控制urserid
        # result = users.objects.filter(email='dfa@kdf').first()
        # print(result.email)
        # print(result)
        print('===================')
        print('请求邮箱：'+requests.POST['email'])
        md5 = getMd5()
        passWord = md5.get(requests.POST['passWord'])
        if not users.objects.filter(email=requests.POST['email']).first():
            users.objects.create(userName=requests.POST['userName'],userID=userID,email=requests.POST['email'],passWord=passWord,date=getNow.date)
            print('==========用户注册成功===========')
            msg='恭喜您已注册成功！！！'
        else:
            msg ='邮箱已存在，请重新尝试！！'
        return HttpResponse(msg)
        # result=users.objects.filter(email=requests.POST['email'])
        # for i in result:
        #      print(i.email)
        # return HttpResponse(msg)