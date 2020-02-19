from django.http import HttpResponse
from django.views.generic import View
from app.modelsDir.appInfoModel import *
from app.common.datetime import *

class appinfoAddForm(View):
    def post(self,requests):
        appName = requests.POST['appNname']
        appAdd = requests.POST['appAdd']
        portNum = requests.POST['portNum']
        path = requests.POST['path']
        date = getNow.date
        if appName != '' and appAdd !='':
            appinfo.objects.create(appName=appName,appAdd=appAdd,portNum=portNum,path=path, date=date)
            print('======应用添加成功！！！=========')
        return HttpResponse('======应用添加成功！！！=========')
