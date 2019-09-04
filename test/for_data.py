#coding=utf-8
import sys
reload(sys)
import threading
import time
import xlrd
import requests
import json
import  re

# 获取欠费信息
def get_balance():
    data_position = {
        'user':'car136008',
        'token':'2FDF85153AAF1DF9F4BB56CA8A1B1368',
        'session':'68D5B890FC1FF8ADDF4CECE4D419A414',
        'jituan':'1',
        'account':'218.64.80.75',
        'type':'2',
        'reqtime':'20190826125334507',
        'encode':'E7AD9F10EF902145F6F6C8CF57CC1829'
    }

    header = {
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'JSESSIONID=CFA4B65178D710F416F66C10D2351F41',
        'Content-Length':'197',
        'Connection':'Keep-Alive',
        'User-Agent':'Apache-HttpClient/UNAVAILABLE(java1.4)'
    }
    url = " http://ayw.jxdxxt.com:6060/TFMS_MOBILE_SERVER/queryUserLineData.do"

    r2=requests.post(url ,data = data_position, headers=header)
    print r2.text

get_balance()