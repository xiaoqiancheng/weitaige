# -*- coding: UTF-8 -*-

import hashlib
import hmac


MD5='MD5'
HMACSHA1='HMACSHA1'



class signature(object):
    def __init__(self,key,msg,signType):
        self.key=key
        self.msg=msg
        self.signType=signType



    def sign(self):
        if self.signType == 'MD5':
            return self.MD5()
        else:
            return self.HMACSHA1()

    def MD5(self):
        # 待加密信息
        str = self.msg

        # 创建md5对象
        hl = hashlib.md5()

        # Tips
        # 此处必须声明encode
        # 若写法为hl.update(str)  报错为： Unicode-objects must be encoded before hashing
        hl.update(str.encode(encoding='utf-8'))


        return hl.hexdigest()

    def HMACSHA1(self):
        hmac_code = hmac.new(self.key, self.msg.encode(encoding='utf-8'), hashlib.sha1)
        return hmac_code.hexdigest()






