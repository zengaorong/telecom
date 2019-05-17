#coding=utf-8
from app.leotool.readexcel import readexcel_tolist
import sys
import MySQLdb
import uuid
import subprocess
import xlwt
import xlrd
import os
from datetime import  datetime,timedelta
from xlutils.copy import copy;

reload(sys)
sys.setdefaultencoding('utf-8')




def formate_excel(filename):
    orign_list = readexcel_tolist('read.xlsx',2,0,0)
    table_name = "01"
    workbook = xlwt.Workbook(encoding = 'utf-8')
    sheet = workbook.add_sheet('table_'+table_name,cell_overwrite_ok=True)

    biaoti_list = orign_list[0]
    format_list = orign_list[1:]

    fields_list = biaoti_list
    for field in range(0,len(fields_list)):
        sheet.write(0,field,fields_list[field])

    td_time = None
    work_for_strs = ""
    watcher_name_strs = ""
    write_list = []
    num = 0

    for row in range(1,len(format_list)):

        for col in range(0,len(format_list[row])):
            sheet.write(row,col,u'%s'%format_list[row][col])
    workbook.save("output.xlsx")


def writeexcel_bykey(addr_str,key,change_str,change_num):
    oldWb = xlrd.open_workbook(addr_str);
    newWb = copy(oldWb);

    newWs = newWb.get_sheet(0);
    newWs.write(change_num, key, change_str);
    newWb.save(addr_str);

# writeexcel_bykey('output.xlsx',10,'abc',1)