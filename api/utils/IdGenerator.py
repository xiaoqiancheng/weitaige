
import uuid

class IdGenerator(object):
    None

def getRequestId():
    return str(uuid.uuid1()).replace('-','')[0:20]



