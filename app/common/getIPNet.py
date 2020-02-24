import re

# 获取IP地址网络部分，用于向资产发现引擎传输网络部分
class netWork:
    net = ''
    def getNet(self,str):
        n = re.search("\d{1,3}.\d{1,3}.\d{1,3}",str)
        if n[0]:
            self.net=n[0]
            return n[0]

if __name__ =="__main__":
    ip ='192.168.1.1'
    net =netWork()
    print(net.getNet(ip))