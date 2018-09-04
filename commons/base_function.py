# coding:utf-8
import datetime


def today():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')


def today_seconds():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d%H%S%m')
