from api.apiClient.apiClient import ApiClient
from api.entity import signature
from api.entity.apiRequest import apiRequest

from api.test import BaseBubboTest

VERSION = "1.0"
SERVICE = "F008"

if __name__ == '__main__':
    httpClint = ApiClient(BaseBubboTest.HOST, BaseBubboTest.PORT, BaseBubboTest.DEFAULT_CLUSTER_ID)
    apiRequest = apiRequest(SERVICE, VERSION, BaseBubboTest.REQUESTER, BaseBubboTest.ACCESS_KEY_ID)
    apiRequest.setSignType(signature.HMACSHA1)
    paramsMap1 = {
                  "orderId":"2562297485238345"
                  }

    parameter = {"paramsJson":paramsMap1}
    apiRequest.setParameters(parameter)
    response = httpClint.post(BaseBubboTest.ACCESS_KEY_SECRET, apiRequest)
    print('ID:%s' % (apiRequest.requestId))
    print('Timestamp:%s' % (apiRequest.timestamp))
    print('[Response]...')
    print('tradeCode:%s' % (response['code']))
    print('tradeMsg:%s' % (response['msg']))
    print('tradeMsg:%s' % (response.get('msg')))






