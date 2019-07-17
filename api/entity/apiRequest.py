import json


class apiRequest(object):
    def __init__(self,serviceCode,version,requester,accessKeyId):
        self.serviceCode = serviceCode
        self.version = version
        self.requester = requester
        self.accessKeyId = accessKeyId
        self.requestId = None
        self.timestamp = None
        self.signType = None
        self.parameters:dict = None

    def buildTruncatedUri(self):
        seg = '/%s/%s/%s/%s/%s/%s/' % (self.serviceCode,self.version,self.requester,self.accessKeyId,self.requestId,self.timestamp)
        if self.signType:
            seg = seg+self.signType+'/'
        else:
            seg
        return seg

    def setRequestId(self,requestId):
        self.requestId = requestId

    def setTimestamp(self,timestamp):
        self.timestamp = timestamp

    def setParameters(self,parameters:dict):
        self.parameters = parameters

    def setSignType(self,signType):
        self.signType=signType
