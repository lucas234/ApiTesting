# coding=utf-8
import json
from base64 import b64encode
from Crypto.Cipher import AES
import hashlib
import time
import datetime
from locust.clients import HttpSession

session = HttpSession("http://121.41.30.64:8888")
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


def get_sign(dict_param, time_stamp, api_security="5941A997F4684889A2BD57C4D3AF05F65EA56F2C7EBC4466B2DF2335934474DC"):
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
    url = "/account/pwd"
    payload = {"phone": phone, "pwd": get_aes_pwd(pwd)}
    time_stamp = get_time_stamp()
    sign = get_sign(payload, time_stamp)
    headers = {
        'apikey': "anon_viphrm_com",
        'content-type': "application/json; charset=UTF-8",
        'devicetoken': "a61dc05ebd9b8b61",
        'devicetype': "0",
        'location': "121.428572,31.228383",
        'sign': sign,
        'timestamp': time_stamp,
    }
    response = session.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)
# login("15566778800", "123456")


def salary_detail(salary_id="343"):
    """发薪详情"""
    url = "/salary/querySalaryDetailByUser"
    payload = {"openId": "baa46b199e5cf9811a53ab89eaca3c9f", "salaryId": salary_id}
    headers = {
        'content-type': "application/json; charset=UTF-8",
    }
    response = session.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)
# salary_detail("34")


def query_salary_list(open_id):
    """发薪列表"""
    url = "/salary/querySalaryListByUser"
    payload = {"openId": open_id, "pageIndex": 1, "pageSize": 12 }
    headers = {
        'content-type': "application/json; charset=UTF-8",
    }
    response = session.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)
# query_salary_list("baa46b199e5cf9811a53ab89eaca3c9f")


# --------------企业专场（与其他域名不同）-----------------------------------------------
enterprise_session = HttpSession("http://121.40.94.182:8000")


def activity(uid, cid, name, mobile):
    """活动专题"""
    url = "/open/enterprise/activity.htm"
    querystring = {"uid": uid, "cid": cid, "name": name, "mobile": mobile}
    response = enterprise_session.get(url, params=querystring)
    print(response.text)
# activity("148452187", "245127430", "都会", "17900000007")


def activity_combo(uid, cid, name, mobile, activity_id):
    """活动套餐"""
    import requests
    url = "/open/enterprise/combo.htm"
    querystring = {"uid": uid, "cid": cid, "name": name, "mobile": mobile,
                   "activityId": activity_id}
    response = enterprise_session.get(url, params=querystring)
    print(response.text)
# activity_combo("148452187", "245127430", "都会", "17900000007", "1123")


def goods(uid, cid, name, mobile, activity_id, package_id):
    """套餐商品"""
    url = "/open/enterprise/goods.htm"
    querystring = {"uid": uid, "cid": cid, "name": name, "mobile": mobile,
                   "activityId": activity_id, "packageId": package_id}
    response = enterprise_session.get(url, params=querystring)
    print(response.text)
# goods("148452187", "245127430", "都会", "17900000007", "1123", "1834")


def exchange_info(uid, cid, name, mobile):
    """兑换记录"""
    url = "/open/enterprise/exchangeInfo.htm"
    querystring = {"uid": uid, "cid": cid, "name": name, "mobile": mobile}
    response = enterprise_session.get(url, params=querystring)
    print(response.text)
# exchange_info("148452187", "245127430", "都会", "17900000007")


def exchange_detail(uid, cid, name, mobile, order_code):
    """兑换详情"""
    url = "/open/enterprise/detail/exchange.htm"
    querystring = {"uid": uid, "cid": cid, "name": name, "mobile": mobile,
                   "orderCode": order_code}
    response = enterprise_session.get(url, params=querystring)
    print(response.text)
# exchange_detail("148452187", "245127430", "都会", "17900000007", "")


def pre_exchange(uid, cid, name, mobile, activity_id, package_id):
    """兑换校验"""
    url = "/open/enterprise/pre/exchange.htm"
    querystring = {"uid": uid, "cid": cid, "name": name, "mobile": mobile,
                   "activityId": activity_id, "packageId": package_id}
    response = enterprise_session.get(url, params=querystring)
    print(response.text)
# pre_exchange("148452187", "245127430", "都会", "17900000007", "1123", "1834")


def goods_geted(uid, cid, name, mobile, order_code):
    """已领商品"""
    url = "/open/enterprise/goods/geted.htm"
    querystring = {"uid": uid, "cid": cid, "name": name, "mobile": mobile,
                   "orderCode": order_code}
    response = enterprise_session.get(url, params=querystring)
    print(response.text)
# goods_geted("148452187", "245127430", "都会", "17900000007", "")


def user_birthday(uid, cid, name, mobile):
    """获取活动名单年龄"""
    url = "/open/enterprise/user/birthday.htm"
    querystring = {"uid": uid, "cid": cid, "name": name, "mobile": mobile}
    response = enterprise_session.get(url, params=querystring)
    print(response.text)
# user_birthday("148452187", "245127430", "都会", "17900000007")

# ---------------考勤打卡（与其他域名不同）-----------------------------------------


employ_session = HttpSession("http://testtime.viphrm.com")


def query_list(cid, uid):
    """打卡查询"""
    url = "/AppServlet"
    querystring = {"method": "appSpace.getExceptionList", "cid": cid, "uid": uid, "year": "2018",
                   "month": "7", "currentPage": "1", "limit": "10"}
    response = employ_session.get(url, params=querystring)
    print(response.text)
# query_list("286836", "147893000")


def clock(cid, uid, orgid,):
    """打卡 orgid部门ID"""
    url = "/AppServlet"
    querystring = {"method": "procApp.newInsertTAttendFlow", "cid": cid, "uid": uid, "orgId": orgid,
                   "talentNo": "18030002", "procDate": datetime.datetime.now().strftime('%Y-%m-%d'), "procFlag": "1", "lon": "121.428304",
                   "lat": "31.228359", "SSID": "", "BSSID": "", "QRCode": "0",
                   "systemInfo": "%7B%22height%22%3A%222034%22%2C%22model%22%3A%22vivo+X20A%22%2C%22osVersion%22%3A%2225%22%2C%22pixelRatio%22%3A%223.0%22%2C%22platform%22%3A%22android%22%2C%22udid%22%3A%22ffffffff-9ede-c4b5-59b7-07370033c587%22%2C%22version%22%3A%221.6.3%22%2C%22width%22%3A%221080%22%7D"}

    response = employ_session.get(url, params=querystring)
    print(response.text)
# clock("286836", "147893000", "93274")
# --------------------差旅项目-----------------------------------------------------


server_sign = "OTE0YmViMDczODVkNDIwODhkZTIwNDM2Y2I0MzcyMDdiMjk2N2IzYzAyMmQ0NjBkYTZhOWM0NTM2OWIzN2VkZGU5MjkwZTQzMmY5NzRjNGI4NzZhMTg0NDRhNWNhZWE4YzU3M2QyM2M3NWZhNDRmN2E5MmQyYzNlZjhkZTFhNjY="


def my_rule(api_security):
    """我的规则"""
    url = "/trip/rule/mine"
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
# my_rule(server_sign)


def city_list(api_security):
    """城市列表"""
    url = "/trip/city/2"
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
# city_list(server_sign)


def air_ticket_query(api_security):
    """机票搜索"""
    url = "/trip/air"

    payload = {"arrCity": "110100", "fromCity": "310106", "sort": "", "sortBy": "", "takeOffDate": "2018-08-30"}
    _time = get_time_stamp()
    _sign = get_sign(payload, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'content-type': "application/json; charset=UTF-8",
        'devicetoken': "a61dc05ebd9b8b61",
        'devicetype': "0",
        'location': "121.428281,31.22833",
        'sign': _sign,
        'timestamp': _time,
        }
    response = session.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)
# air_ticket_query(server_sign)


def air_query_info(api_security):
    """机票搜索首页"""
    url = "/trip/air"
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
# air_query_info(server_sign)


def air_ticket_order(api_security):
    """机票订单"""
    url = "/trip/air/order"
    payload = {"numberPerPage": 10, "orderState": "0", "pageNumber": 1}
    _time = get_time_stamp()
    _sign = get_sign(payload, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'content-type': "application/json; charset=UTF-8",
        'devicetoken': "a61dc05ebd9b8b61",
        'devicetype': "0",
        'location': "121.428281,31.22833",
        'sign': _sign,
        'timestamp': _time,
        }
    response = session.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)
# air_ticket_order(server_sign)


def order_detail(api_security, order_id="201808146710003077"):
    """订单详情"""
    url = "/trip/air/order/%s" % order_id
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
# order_detail(server_sign)


def insurance_detail(api_security):
    """保险详情"""
    url = "/trip/air/insurance"
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
# insurance_detail(server_sign)


def hotel_order_list(api_security):
    """酒店订单列表"""
    url = "/trip/hotel/order"
    payload = {"numberPerPage": 10, "orderState": "0", "pageNumber": 1}
    _time = get_time_stamp()
    _sign = get_sign(payload, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'content-type': "application/json; charset=UTF-8",
        'devicetoken': "a61dc05ebd9b8b61",
        'devicetype': "0",
        'location': "121.428281,31.22833",
        'sign': _sign,
        'timestamp': _time,
        }
    response = session.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)
# hotel_order_list(server_sign)


def hotel_order_detail(api_security, order_id="201808146610002533"):
    """酒店订单详情"""
    url = "/trip/hotel/order/%s" % order_id
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
# hotel_order_detail(server_sign)


def hotel_query_stars(api_security):
    """酒店星级规则查询"""
    url = "/trip/hotels/stars"
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
# hotel_query_stars(server_sign)


def server_index(api_security):
    """服务窗首页"""
    url = "/work/index"
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
# server_index(server_sign)


def salary_index(api_security):
    """薪资贷首页"""
    url = "/salary/index"
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
# salary_index(server_sign)


def strategy_index(api_security):
    """头条首页"""
    url = "/strategy/index"
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
# strategy_index(server_sign)


def userbase_index(api_security):
    """我的"""
    url = "/user/base"
    _time = get_time_stamp()
    _sign = get_sign({}, _time, api_security)
    headers = {
        'apikey': "baa46b199e5cf9811a53ab89eaca3c9f",
        'sign': _sign,
        'timestamp': _time,
    }
    response = session.get(url, headers=headers)
    print(response.text)
userbase_index(server_sign)
# login("15566778800", "123456")








