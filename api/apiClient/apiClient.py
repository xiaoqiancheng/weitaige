# -*- coding: UTF-8 -*-
import json
import time

import requests
from api.entity import apiRequest
from api.utils import IdGenerator
from api.utils.SignHelper import SignHelper


class ApiClient(object):
    def __init__(self,host,port,clusterId=None):
        self.host=host
        self.port=port
        self.clusterId=clusterId



    def post(self, accessKeySecret, apiRquest=apiRequest.apiRequest, requesetId=None):

        if requesetId == None:
            requesetId = IdGenerator.getRequestId()


        if not apiRquest or not accessKeySecret:
            raise Exception("One or more parameters are empty")
        if len(requesetId) !=20:
            raise Exception("Illegal request Id")

        apiRquest.setRequestId(requesetId)
        nowTime = lambda:int(round(time.time() * 1000))
        apiRquest.setTimestamp(nowTime())
        signature = SignHelper.sign('POST',accessKeySecret,apiRquest)
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        url="http://%s:%s%s%s" % (self.host,self.port,apiRquest.buildTruncatedUri(),signature)
        print('[%s]:POST - %s' % (requesetId,url))
        parameterJson = json.dumps(apiRquest.parameters,separators=(',', ':'))
        print('[%s] -> %s' % (requesetId,parameterJson))
        response = requests.post(url, data=parameterJson,headers=headers)
        if response.status_code == 200:
            resJson =  response.json()
            print('[%s]——> %s' % (requesetId,str(resJson)))
            return resJson
        else:
            None









