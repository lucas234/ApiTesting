# _*_ coding=utf-8 _*_
# __author__ = 'lucas'
import smtplib, sys
from email.mime.text import MIMEText


def send_mail(sub, content):
    #############
    # 要发给谁，这里发给1个人
    mailto_list = ["xxxxxx@qq.com"]
    #####################
    # 设置服务器，用户名、口令以及邮箱的后缀
    mail_host = "smtp.163.com"
    mail_user = "xxxx@163.com"
    mail_pass = "xxxxxxxxx"
    mail_postfix = "163.com"
    ######################
    '''''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me = mail_user + "<" + mail_user + ">"
    msg = MIMEText(content, _charset='gbk')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(mailto_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user, mail_pass)
        s.sendmail(me, mailto_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(u'这是python测试邮件', u'python发送邮件'):
        print u'发送成功'
    else:
        print u'发送失败'