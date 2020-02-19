from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from app.modelsDir.assetsModel import *
from app.common.datetime import *

class assetsaddForm(View):
    def get(self,requests):
        return HttpResponse('=========请使用post提交=======')
    def post(self, requests):
        # 获取前台提交的资产信息
        AssetsName = requests.POST['assetsName']
        AssetsIP = requests.POST['asstsIP']
        NetMask = requests.POST['netMask']
        # Gateway = requests.POST['gateway']
        OsVersion = requests.POST['osVersion']
        # DeveType = requests.POST['deveType']
        appName = requests.POST['appName']
        # ManageUser = requests.POST['manageUser']
        # Person = requests.POST['person']
        dateTime = getNow()
        dateTime.date
        print(dateTime.date)
        print(dateTime)
        context = {}
        if AssetsName != '' and AssetsIP != '':
            zichan.objects.create(AssetsName=AssetsName, AssetsIP=AssetsIP, NetMask=NetMask,
                                  OsVersion=OsVersion,  appName=appName,  DateTime=dateTime.date)
            context['code']="添加成功！！"
            print('==========资产添加成功！！==========')
        else:
            print('==========资产名称与IP不能为空==========')
        return render(requests,'app/handasstes.html',context)
        # return HttpResponse('添加成功')