#coding=utf-8
from flask import render_template, redirect, request, url_for, flash,jsonify,send_from_directory, \
    current_app
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import retired
from .. import db
from sqlalchemy import and_
from app.leotool.bs64pic.pic_to_bs64 import get_picbase64
# from ..models import Scores
from datetime import datetime
import sys
# from ..leotool.readexcel import readexcel_todict,readexcel_tolist,writeexcel_bykey
from math import ceil
import xlrd
import uuid
import os

reload(sys)
sys.setdefaultencoding('utf-8')


# 搜索漫画
@retired.route('/login', methods=['GET', 'POST'])
def retired_login():
    return render_template('retired/login.html')

# 搜索漫画
@retired.route('/test', methods=['GET', 'POST'])
def test():
    time = request.form
    print request.remote_addr
    print time
    data_json_return = {
        "type": "ok",
        "ip": request.remote_addr,
        "id": "0001"
    }
    return  "ok"
    # return jsonify({'code': -1, 'filename': '', 'msg': 'No file part'})

# 搜索漫画
@retired.route('/index', methods=['GET', 'POST'])
def retired_index():
    return render_template('retired/index.html')


# 搜索漫画
@retired.route('/infopage', methods=['GET', 'POST'])
def retired_infopage():
    return render_template('retired/infopage.html')

# 搜索漫画
@retired.route('/sethelp', methods=['GET', 'POST'])
def retired_sethelp():
    return render_template('retired/sethelp.html')
