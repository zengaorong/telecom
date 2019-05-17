import os
import platform
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.qq.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = os.environ.get('MAIL_USERNAME')
    FLASKY_ADMIN = '1904959670@qq.com'

    sysstr = platform.system()
    if(sysstr =="Windows"):
        UPLOADED_PHOTOS_DEST = os.getcwd() + '\\app\\paiche\\static_data'
    if(sysstr == "Linux"):
        UPLOADED_PHOTOS_DEST = os.getcwd() + '/app/paiche/static_data'


    # UPLOADED_PHOTOS_DEST = os.environ.get(os.getcwd(), 'app/static/uploads')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_POSTS_PER_PAGE = 10
    FLASKY_POSTS_CHAP_PAGE = 100
    FLASKY_SERTVER_ADDR = "http://127.0.0.1:8083"
    #FLASKY_SERTVER_ADDR = "http://120.79.217.238:8080"


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:7monthdleo@120.79.217.238/telecom'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:7monthdleo@120.79.217.238/telecom'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:7monthdleo@120.79.217.238/telecom'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
