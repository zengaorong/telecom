#coding=utf-8
from flask import render_template, redirect, request, url_for, flash,jsonify,send_from_directory, \
    current_app
from ..models import Activationlist
from datetime import datetime
import sys
import flask_excel as excel
from . import activation
from .. import db
# from ..leotool.readexcel import readexcel_todict,readexcel_tolist,writeexcel_bykey
from form import select_list
from math import ceil
import xlrd
import uuid
import os

reload(sys)
sys.setdefaultencoding('utf-8')


@activation.route('/active')
def active():
    time = request.form
    ip = request.headers['X-Real-Ip']
    print time

    activationlist = Activationlist.query.filter_by(ip=ip).first()

    dt = datetime.now()
    now_time = dt.strftime('%Y-%m-%d %H:%M:%S')
    if activationlist is None:
        activationlist = Activationlist()
        activationlist.ip = ip
        activationlist.created_time = now_time
        activationlist.updated_time = now_time
        activationlist.opreat_type = 0
        db.session.add(activationlist)
        db.session.commit()
    else:
        activationlist.updated_time = now_time
        activationlist.opreat_type = 0
        db.session.add(activationlist)
        db.session.commit()

    # logbook = Logbook.query.filter_by(id=logbookid).first()

    data_json_return = {
        "type": "ok",
        "ip": ip,
        "id": activationlist.Id
    }
    return  jsonify(data_json_return)



@activation.route('/list',methods=['GET', 'POST'])
# @login_required
def list():
    # # 检测是否带参数
    qu_name = request.form.get('user_ip', "", type=str)
    pagination_qu_name = request.args.get('user_ip', "", type=str)
    # 存在搜索参数
    if qu_name!="" or pagination_qu_name!="":
        form = select_list()
        if qu_name!="":
            pagination_qu_name = qu_name
        form.user_ip.data = pagination_qu_name
        page = request.args.get('page', 1, type=int)
        pagination = db.session.query(Activationlist.ip,Activationlist.Id,Activationlist.created_time,Activationlist.updated_time).filter(Activationlist.opreat_type!=2, Activationlist.ip==pagination_qu_name).order_by(Activationlist.created_time.desc()).paginate(
            page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
            error_out=False)
        posts = pagination.items
        listsize = pagination.total
        return render_template('activation/list.html',posts=posts,pagination=pagination,listsize=listsize,form=form,qu_name=pagination_qu_name)
    page = request.args.get('page', 1, type=int)
    # Scores.id,Scores.old_url,Scores.name,Scores.opreat_type,Scores.provider,Scores.user_name
    pagination = db.session.query(Activationlist.ip,Activationlist.Id,Activationlist.created_time,Activationlist.updated_time).filter(Activationlist.opreat_type!=2).order_by(Activationlist.created_time.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items
    listsize = pagination.total
    form = select_list()

    return render_template('activation/list.html',posts=posts,pagination=pagination,listsize=listsize,form=form)



@activation.route('/exp_excel/', methods=['GET'])
def exp_excel():
    q = db.session.query(
        Activationlist.ip.label('ip'),
        Activationlist.Id.label('Id'),
        Activationlist.created_time.label('created_time'),
        Activationlist.updated_time.label('updated_time')
    ).order_by(Activationlist.updated_time.asc())
    query_sets = q.all()
    excel.make_response_from_query_sets(
        query_sets,
        column_names=[
            'ip',
            'Id',
            'created_time',
            'updated_time',
        ],
        file_type='xlsx',
        file_name='activationlist',
    )