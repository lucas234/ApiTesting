# coding:utf-8
import json


# post方法调用接口
# 参数:url地址,参数
def requests_wrap_post(session, url, body, apikey='', sign="", timestamp=""):
    if apikey:
        session.headers.update({'apikey': str(apikey)})
    if sign:
        session.headers.update({'sign': sign})
    if timestamp:
        session.headers.update({'timestamp': str(timestamp)})
    try:
        response = session.post(url, headers=session.headers, data=json.dumps(body))
        # if 'fail\"' in response.text:
        #     if 'errorMsg' in response.text:
        #         Globals().GLOGGER.error('errorMsg: ' + response.json()['errorMsg'] + '\n')
        #         Env().execMsg = response.json()['errorMsg']
        #     elif 'content' in response.text:
        #         Globals().GLOGGER.error('errorMsg: ' + response.json()['content'] + '\n')
        #         Env().execMsg = response.json()['content']
        #     print Env().execMsg
        response.raise_for_status()
    except Exception as e:
        print e.message
        # if 'Server Error' in e.message:
        #     Env().execMsg = 'server Error'
        # return None
    else:
        return response.json()


