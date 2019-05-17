#coding=utf-8
import xlrd
import sys
import xlwt
from xlutils.copy import copy;
from collections import OrderedDict
reload(sys)
sys.setdefaultencoding('utf-8')

# 放于不通目录下的路径方式 dic1 = readexcel_todict("./leotool/num.xls",1,1,0)
# addr_str 路径 key_num 字典唯一项为表第一项 begin_num 行开始位置（起始为0） 0表示Excel第一张（sheet）表

def readexcel_todict(addr_str,key_num,begin_num,sheetnum):
    excel_workbook = xlrd.open_workbook(addr_str)
    excel_sheet01 = excel_workbook.sheets()[sheetnum]
    terminal_num_nrows = excel_sheet01.nrows
    terminal_num_ncols = excel_sheet01.ncols
    excel_dict = OrderedDict()
    for r in range(begin_num,terminal_num_nrows):
        key_str = excel_sheet01.cell(r,key_num).value
        if type(key_str) is float:
            key_str = str(int(key_str))
        if check_is_nums(key_str):
            #print key_str + "123"
            key_str = int(key_str)
        hold = []
        #print int(key_str)
        for c in range(0,terminal_num_ncols):
            if type(excel_sheet01.cell(r,c).value) is float:
                hold.append(str((excel_sheet01.cell(r,c).value)))
            else:
                hold.append(excel_sheet01.cell(r,c).value)
        # 存入字典中
        excel_dict[key_str] =  hold
    return excel_dict


def readexcel_tolist(addr_str,key_num,begin_num,sheetnum):
    excel_workbook = xlrd.open_workbook(addr_str)
    excel_sheet01 = excel_workbook.sheets()[sheetnum]
    terminal_num_nrows = excel_sheet01.nrows
    terminal_num_ncols = excel_sheet01.ncols
    excel_dict = OrderedDict()
    for r in range(begin_num,terminal_num_nrows):
        key_str = excel_sheet01.cell(r,key_num).value
        if type(key_str) is float:
            key_str = str(int(key_str))
        if check_is_nums(key_str):
            #print key_str + "123"
            key_str = int(key_str)
        hold = []
        #print int(key_str)
        for c in range(0,terminal_num_ncols):
            if type(excel_sheet01.cell(r,c).value) is float:
                hold.append(str((excel_sheet01.cell(r,c).value)))
            else:
                hold.append(excel_sheet01.cell(r,c).value)
        # 存入字典中
        excel_dict[key_str] =  hold

    excel_list = []
    for key in excel_dict:
        excel_list.append(excel_dict[key])
    return excel_list


def writeexcel_bykey(addr_str,key,change_str,change_num):
    oldWb = xlrd.open_workbook(addr_str);
    newWb = copy(oldWb);
    newWs = newWb.get_sheet(0);
    newWs.write(change_num, key, change_str);
    newWb.save(addr_str);


def check_is_nums(str_check):
    isnum = True
    for key in str_check.decode('utf-8'):
        if u'\u0030'<=key<=u'\u0039':
            pass
        else:
            isnum = False
            return isnum

    if str_check == "":
        isnum = False
    return isnum


