#coding=utf-8
from flask import render_template, redirect, request, url_for, flash,jsonify,send_from_directory, \
    current_app
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import paiche
from .. import db
from sqlalchemy import and_
from form import details_qupu,select_list
from app.leotool.bs64pic.pic_to_bs64 import get_picbase64
from ..models import Scores
from data.operatedb import check_qupu_name_todb,insert_qupu_todb
from datetime import datetime
import sys
from ..leotool.readexcel import readexcel_todict,readexcel_tolist,writeexcel_bykey
from math import ceil
import xlrd
import uuid
import os

reload(sys)
sys.setdefaultencoding('utf-8')

class Paginate:
    def __init__(self,total,per_page,page):
        self.total = total
        self.per_page = per_page
        self.page = page

    @property
    def pages(self):
        """The total number of pages"""
        if self.per_page == 0:
            pages = 0
        else:
            pages = int(ceil(self.total / float(self.per_page)))
        return pages

    @property
    def prev_num(self):
        """Number of the previous page."""
        if not self.has_prev:
            return None
        return self.page - 1

    @property
    def has_prev(self):
        """True if a previous page exists"""
        return self.page > 1

    @property
    def next_num(self):
        """Number of the next page"""
        if not self.has_next:
            return None
        return self.page + 1

    @property
    def has_next(self):
        """True if a next page exists."""
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
                    (num > self.page - left_current - 1 and \
                     num < self.page + right_current) or \
                    num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num

# 曲谱主页
@paiche.route('/list',methods=['GET', 'POST'])
@login_required
def list():
    # # 检测是否带参数
    # qu_name = request.form.get('qu_name', "", type=str)
    # pagination_qu_name = request.args.get('qu_name', "", type=str)
    # # 存在搜索参数
    # if qu_name!="" or pagination_qu_name!="":
    #     form = select_list()
    #     if qu_name!="":
    #         pagination_qu_name = qu_name
    #     form.qu_name.data = pagination_qu_name
    #     page = request.args.get('page', 1, type=int)
    #     pagination = db.session.query(Scores.id,Scores.old_url,Scores.name,Scores.opreat_type,Scores.provider,Scores.user_name).filter(Scores.opreat_type!=2 , Scores.name.like('%' + pagination_qu_name + '%')).order_by(Scores.created_time.desc()).paginate(
    #         page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    #         error_out=False)
    #     posts = pagination.items
    #     listsize = pagination.total
    #     return render_template('editpu/list.html',posts=posts,pagination=pagination,listsize=listsize,form=form,qu_name=pagination_qu_name)
    # page = request.args.get('page', 1, type=int)
    # pagination = db.session.query(Scores.id,Scores.old_url,Scores.name,Scores.opreat_type,Scores.provider,Scores.user_name).filter(Scores.opreat_type!=2).order_by(Scores.created_time.desc()).paginate(
    #     page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    #     error_out=False)
    # posts = pagination.items
    # listsize = pagination.total
    # form = select_list()
    # return render_template('editpu/list.html',posts=posts,pagination=pagination,listsize=listsize,form=form)

    cus_name = request.form.get('cus_name', "", type=str)
    pagination_cus_name = request.args.get('cus_name', "", type=str)


    # user_num = request.form.get('user_num', "", type=str)
    # pagination_user_num = request.args.get('user_num', "", type=str)


    if cus_name!="" or pagination_cus_name!="":
        form = select_list()
        if cus_name!="":
            pagination_cus_name = cus_name
        form.cus_name.data = pagination_cus_name

        orign_list = readexcel_tolist(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], 'output.xlsx'),2,0,0)
        biaoti_list = orign_list[0]
        format_list = orign_list[1:]
        temp_list = []
        right_excel_num = []
        total_num = 1
        for key in format_list:

            if key[7] == pagination_cus_name:
                temp_list.append(key)
                right_excel_num.append(total_num)

            total_num = total_num + 1

        format_list = temp_list
        total =  len(format_list)
        per_page = current_app.config['FLASKY_POSTS_PER_PAGE']
        page = request.args.get('page', 1, type=int)
        format_list = format_list[(page-1)*per_page:(page)*per_page]
        right_excel_num = right_excel_num[(page-1)*per_page:(page)*per_page]
        paginate = Paginate(total,per_page,page)

        return render_template('paiche/list.html',biaoti_list=biaoti_list,pagination=paginate,posts=format_list,form=form,cus_name=pagination_cus_name,right_excel_num=right_excel_num)


    form = select_list()
    orign_list = readexcel_tolist(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], 'output.xlsx'),2,0,0)
    biaoti_list = orign_list[0]
    format_list = orign_list[1:]
    total =  len(format_list)
    per_page = current_app.config['FLASKY_POSTS_PER_PAGE']
    page = request.args.get('page', 1, type=int)
    format_list = format_list[(page-1)*per_page:(page)*per_page]
    paginate = Paginate(total,per_page,page)
        # self.total = total
        # self.per_page = per_page
        # self.page = page
        # self.next_num = next_num
        # self.total = total



    # pagination = dict.paginate(
    #     1, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
    #     error_out=False)
    # pagination=pagination
    return render_template('paiche/list.html',biaoti_list=biaoti_list,pagination=paginate,posts=format_list,form=form,qu_name="233")


# 改变选择
@paiche.route('/changeselect',methods=['GET', 'POST'])
@login_required
def changeselect():
    num_id = request.form.get('num_id', "", type=int)
    key_num = request.form.get('key_num', "", type=int)
    if num_id != "":
        writeexcel_bykey(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], 'output.xlsx'),10,current_user.username,key_num)
        return jsonify(data=True)
    else:
        writeexcel_bykey(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], 'output.xlsx'),10,"",key_num)
        return jsonify(data=True)
    return '''<h1>数据错误,联系吉吉米米解决<h1> <a href="/paiche/list">返回</a>'''





from flask import send_from_directory
from werkzeug.utils import secure_filename
@paiche.route('/get_attachment/<path:filename>')
def get_attachment(filename):
    print filename
    return send_from_directory(current_app.config['UPLOADED_PHOTOS_DEST'],filename,as_attachment=True)

# 上传
ALLOWED_EXTENSIONS = ['xls', 'xlsx']
def allowe_file(filename):
    '''
    限制上传的文件格式
    :param filename:
    :return:
    '''
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


@paiche.route('/upload', methods=['GET', 'POST'])
@login_required
def updata():
    return render_template('paiche/upload.html')


@paiche.route('/upload_file', methods=['GET', 'POST'])
@login_required
def upload_file():
    # file = request.files.get('文件名') # 获取文件
    file = request.files['file']
    filename = secure_filename(file.filename)  # 获取文件名
    #file.save(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], filename)) # 保存文件
    excel_dict = {}
    try:
        f = file.read()    #文件内容
        excel_workbook = xlrd.open_workbook(file_contents=f)
        excel_sheet01 = excel_workbook.sheets()[0]
        terminal_num_nrows = excel_sheet01.nrows
        terminal_num_ncols = excel_sheet01.ncols

        print terminal_num_nrows,terminal_num_ncols

        orign_list = readexcel_tolist(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], 'output.xlsx'),2,0,0)
        biaoti_list = orign_list[0]
        format_list = orign_list[1:]

        dict_check = {}
        total_num = 1
        for data_key in format_list:
            dict_check[data_key[2]] = [data_key[10],total_num]
            total_num = total_num + 1


        error_list = []
        for r in range(1,terminal_num_nrows):
            # print str((excel_sheet01.cell(r,2).value))
            if str((excel_sheet01.cell(r,10).value))!=None and str((excel_sheet01.cell(r,10).value))!='':
                # print repr(str((excel_sheet01.cell(r,10).value)))
                # print str((excel_sheet01.cell(r,10).value))
                print dict_check[excel_sheet01.cell(r,2).value][0]
                if dict_check[excel_sheet01.cell(r,2).value][0]==None or dict_check[excel_sheet01.cell(r,2).value][0]=='':
                    writeexcel_bykey(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], 'output.xlsx'),10,excel_sheet01.cell(r,10).value,dict_check[excel_sheet01.cell(r,2).value][1])
                else:
                    if dict_check[excel_sheet01.cell(r,2).value][0] == excel_sheet01.cell(r,10).value:
                        pass
                    else:
                        error_list.append(str(excel_sheet01.cell(r,10).value) + ':' + str(excel_sheet01.cell(r,2).value) )



    except:
        return "上传格式不正确"


    return render_template('paiche/uploadtips.html',error_list=error_list)