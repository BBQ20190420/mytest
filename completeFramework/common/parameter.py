import time
import uuid
'''
封装时间类和请求
'''
class fixPara():
    def getTime(self):
        formattime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        return formattime

    def getRequestNo(self):
        '''
        uuid1,基于时间戳
        uuid3()——基于名字的MD5散列值
        uuid4()——基于随机数
        uuid5()——基于名字的SHA-1散列值
        python没有uuid2
        '''
        requestNo="".join(str(uuid.uuid1()).split('-'))
        return requestNo
