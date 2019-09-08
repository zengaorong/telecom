#coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:7monthdleo@120.79.217.238/telecom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# id 首次上线时间 最近上线时间
# IP 状态（是否离线）
# 重连次数（默认三次 如果未收到重连 改变状态为离线）
class activationlist(db.Model):
    __tablename__ = 'activationlist'
    Id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    created_time = db.Column(db.DATETIME)
    updated_time = db.Column(db.DATETIME)

    ip = db.Column(db.String(24))
    opreat_type = db.Column(db.String(1))
    def __repr__(self):
        return '<activationlist %r>' % self.id

db.create_all()
db.session.commit()