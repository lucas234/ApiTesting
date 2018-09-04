# coding:utf-8
from base64 import b64encode
from Crypto.Cipher import AES
import hashlib
import time
from commons.requests_wrap import requests_wrap_post
from data.account_data import AccountData


class AccountApi:
    def __init__(self, session):
        self.session = session

    def get_aes_pwd(self, value):
        """密码加密算法"""
        key = "16BytesWeiZhiKey"
        text = value
        cryptor = AES.new(key, AES.MODE_CBC, "16-Bytes--String")
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            text += (chr(add) * add)
        ciphertext = cryptor.encrypt(text)
        return b64encode(ciphertext)

    def get_sign(self, dict_param, time_stamp, salt=""):
        """签名算法"""
        dict_param.update({"timestamp": time_stamp})
        api_security = "apiSecurity=5941A997F4684889A2BD57C4D3AF05F65EA56F2C7EBC4466B2DF2335934474DC"
        dict_sort = sorted(dict_param.items(), key=lambda c: c[0])
        # 生成apisign的md5码
        api_str = ''
        for x, y in dict(dict_sort).items():
            api_str += str(x) + "=" + str(y) + "&"
        sign_str = api_str + salt + api_security
        apisg = hashlib.md5(sign_str)
        api_sign = apisg.hexdigest()
        del dict_param["timestamp"]
        return api_sign

    def get_api_key(self, user_id, phone):
        """apikey 算法"""
        _str = str(user_id) + str(phone)
        m = hashlib.md5(_str)
        api_key = m.hexdigest()
        return api_key

    def get_time_stamp(self):
        """获取当前时间戳"""
        _time = str(int(time.time())) + "000"
        return _time

    def login(self, phone, pwd):
        AccountData.LOGIN_PARAMS["phone"] = phone
        AccountData.LOGIN_PARAMS["pwd"] = self.get_aes_pwd(pwd)
        time_stamp = self.get_time_stamp()
        sign = self.get_sign(AccountData.LOGIN_PARAMS, time_stamp)
        response = requests_wrap_post(self.session, self.session.base_url + AccountData.LOGIN, AccountData.LOGIN_PARAMS,
                                      sign=sign, timestamp=time_stamp)
        return response


