#coding=utf-8
import sys
reload(sys)
import threading
import time
import xlrd
import requests

sys.setdefaultencoding('utf-8')

cookie = '''ys-ck_widget=s%3A%7B%22widgetPos%22%3A%5B%5B%22NoticeManage%22%2C%22Supervise%22%5D%2C%5B%22PointView%22%2C%22Task%22%5D%5D%7D; JSESSIONID=dDxkaGGjRTNxBGirfqRAE1eQNWUUtgwF7j_ErVdGJCan6tbVyu7Q!102638464!500311059'''
# #  获取稽核单
# header={
#     'Content-Type' : 'application/x-www-form-urlencoded',
#     'User-Agent' : 'Dalvik/2.1.0 (Linux; U; Android 6.0; EVA-AL10 Build/HUAWEIEVA-AL10)',
#     'Host' : 'ayw.jxdxxt.com:6060',
#     'cookie' :  cookie
# }
#
# # 账号解绑机顶盒
# data_position={
#     'domainCode' : '360800',
#     'latnId' : '10',
#     'unitId' : '',
#     'areaId' : '',
#     'olNbr' : '',
#     'ofrClassId' : '',
#     'isCurrentDate' : 'false',
#     'saleProName' : '',
#     'sysResult' : '',
#     'ofrClassId' : '',
#     'fstAuditResult' : '',
#     'saleUnitId' : '',
#     'saleStaff' : '',
#     'employName' : '',
#     'serviceNbr' : '',
#     'custName' : '',
#     'extCustOrderId' : '',
#     'jtExtCustOrderId' : '',
#     'fstAuditStaffId' : '',
#     'sedAuditStaffId' : '',
#     'developer' : '',
#     'auditStep' : '',
#     'auditResult' : '2',
#     'startDate' : '2019-07-13',
#     'workType' : '',
#     'endDate' : '2019-08-01',
#     'auditState' : '-1',
#     'auditState0' : '0',
#     'channelId' : '',
#     'chnOrgs' : '',
#     'caType' : '',
#     'errType' : '',
#     'productId' : '',
#     'start' : '0',
#     'loadType' : 'jump',
#     'loadPage' : '1',
#     'level' : '3',
#     'startConfidence' : '',
#     'endConfidence' : '',
#     'limit' : '10'
#
# }
# r2=requests.post("http://134.224.129.216/workflow/getAuditWorkListAuditYwjhAction.do",data = data_position ,headers=header)
# import json
# out_strs = r2.text.replace("total","\"total\"")
# out_strs = out_strs.replace("root","\"root\"")
# # print out_strs
# print len(json.loads(out_strs)['root'])
# OL_NBR = json.loads(out_strs)['root'][4]['OL_NBR']
# name = json.loads(out_strs)['root'][4]['AGENT_CUST_NAME']
# #AGENT_CUST_NAME=刘斌
# print name
# # print r2.json()
#
#
#
# #http://134.224.129.216/workflow/getYxzlInfosAuditYwjhAction.do
#
# #  获取人证合一
# header={
#     'Content-Type' : 'application/x-www-form-urlencoded',
#     'User-Agent' : 'Dalvik/2.1.0 (Linux; U; Android 6.0; EVA-AL10 Build/HUAWEIEVA-AL10)',
#     'Host' : 'ayw.jxdxxt.com:6060',
#     'cookie' :  cookie
# }
#
# # 获取人证合一
# data_position={
#     'OL_NBR' : OL_NBR,
#
# }
# r2=requests.post("http://134.224.129.216/workflow/getYxzlInfosAuditYwjhAction.do",data = data_position ,headers=header)
# # print r2.text
# out_strs = r2.text.replace("total","\"total\"")
# out_strs = out_strs.replace("root","\"root\"")
# CERTI_URL = json.loads(out_strs)['root'][0]['CERTI_URL']
# print CERTI_URL










