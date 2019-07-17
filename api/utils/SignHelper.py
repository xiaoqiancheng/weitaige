

import base64
import json
from urllib.parse import quote_plus

from api import entity as apiRequest
from api.entity import signature as signType

EQUAL = "="
AMPERSAND = "&"

class SignHelper(object):
    def __init__(self):
        None

    @staticmethod
    def sign(method, accessKeySecret, apiRequest=apiRequest.apiRequest):
        key = base64.b64decode(accessKeySecret)
        key+=bytes('&',encoding='utf-8')
        str2Sign = SignHelper.getStringToSign(method,apiRequest)
        signature = signType.signature(key,str2Sign,apiRequest.signType)
        resSign = signature.sign()

        print('str2Sign=',str2Sign)
        print('resSign=',resSign)
        return resSign

    @staticmethod
    def getStringToSign(method, apiRequest=apiRequest.apiRequest):
        truncatedUri = apiRequest.buildTruncatedUri()
        truncatedUri = SignHelper.encode(truncatedUri)
        queryString = ''
        for k,v in apiRequest.parameters.items():
            if v:
                queryString+='%s%s%s%s' % (AMPERSAND,SignHelper.encode(k),EQUAL,SignHelper.encode(str(json.dumps(v,separators=(',', ':')))))


        return '%s%s%s%s' % (method,AMPERSAND,truncatedUri,queryString)

    @staticmethod
    def encode(data):
        data = quote_plus(data)
        data = data.replace('+','%20').replace('*','%2A').replace('%7E','~')
        return data



