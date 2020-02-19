import time

#定义公共时间对象
class getNow(object):
    date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    def __init__(self):
        # self.userID = self.userID + 1
        self.date = time.strftime("%Y-%m-%d",time.localtime(time.time()))
        print(self.date)
