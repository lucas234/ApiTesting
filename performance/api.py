# coding=utf-8
import json
from base64 import b64encode
from Crypto.Cipher import AES
import hashlib
import time
import datetime
from locust.clients import HttpSession

session = HttpSession("xxxx")
# adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
# session.mount('http://', adapter)


def get_aes_pwd(value):
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


def get_sign(dict_param, time_stamp, api_security=""):
    """签名算法"""
    dict_param.update({"timestamp": time_stamp})
    api_security = "apiSecurity=%s" % api_security
    dict_sort = sorted(dict_param.items(), key=lambda c: c[0])
    # 生成apisign的md5码
    api_str = ''
    for y in dict_sort:
        api_str += str(y[0]) + "=" + str(y[1]) + "&"
    sign_str = api_str + api_security
    # print sign_str
    apisg = hashlib.md5(sign_str)
    api_sign = apisg.hexdigest()
    # print api_sign
    del dict_param["timestamp"]
    return api_sign


def get_api_key(user_id, phone):
    """apikey 算法"""
    _str = str(user_id) + str(phone)
    m = hashlib.md5(_str)
    api_key = m.hexdigest()
    return api_key


def get_time_stamp():
    """获取当前时间戳"""
    _time = str(int(time.time())) + "000"
    return _time


def login(phone, pwd):
    """登录"""
    url = "XXXX"
    payload = {"phone": phone, "pwd": get_aes_pwd(pwd)}
    time_stamp = get_time_stamp()
    sign = get_sign(payload, time_stamp)
    headers = {
        'apikey': "",
        'content-type': "application/json; charset=UTF-8",
        'devicetoken': "",
        'devicetype': "0",
        'location': "",
        'sign': sign,
        'timestamp': time_stamp,
    }
    response = session.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)
# login("XXX", "XXX")











