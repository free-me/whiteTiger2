import hashlib

class getMd5:
    def get(self,str):
        md5 = hashlib.md5()
        # 实例化md5加密方法
        md5.update(str.encode())
        # 进行加密，python2可以给字符串加密，python3只能给字节加密
        result = md5.hexdigest()
        return result


if __name__ =="__main__":
    d = getMd5()
    s=d.get('sssssssssss')
    print(s)