'''
封装网关请求和直连请求
'''

import requests
import json
from completeFramework.common import parameter
from completeFramework.common.sign import doSign
from completeFramework.config import readconf

platformNo=readconf.platformNo
url=readconf.initurl
redirecturl=readconf.redirecturl

time = parameter.fixPara().getTime()

class apirequest():

    """
    拼装存管请求格式
    """

    def formatReq(self,serviceName,req,userDevice):
        mysign = doSign(req)
        formatBody = {
            "serviceName": serviceName,
            "userDevice": userDevice,
            "reqData": req,
            "keySerial": 1,
            "sign": mysign,
            "platformNo":platformNo
        }

        return formatBody

    def directReq(self,serviceName,req,*userDevice):
        directurl=url+'service'
        fixedmsg={
            "timestamp":time,
            "platformNo":platformNo
        }
        fixedmsg.update(req)
        data=json.dumps(fixedmsg)
        reqdata= self.formatReq(serviceName,data,userDevice)
        print(userDevice)

        #发送post请求
        resp=requests.post(directurl,reqdata)
        print("请求参数为：",reqdata)
        print("返回结果为：",resp.text)
        return resp.json()

    def gateReq(self,serviceName,req,*userDevice):
        gateurl=url+'gateway'
        fixedmsg = {
            "timestamp": time,
            "platformNo": platformNo,
            "redirectUrl":redirecturl
        }
        fixedmsg.update(req)
        data=json.dumps(fixedmsg)
        reqdata=self.formatReq(serviceName,data,userDevice)

        #发送post请求
        resp=requests.post(gateurl,reqdata)
        print("请求参数为：", data)
        #网关请求，重定向
        return resp.url








