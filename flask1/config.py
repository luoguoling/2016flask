__author__ = 'luoguoling'
__author__ = 'luoguoling'
import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLCHEMY_COMMIT_ON_TEARDOWN = True
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG = True
#    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:abc123@127.0.0.1:3306/flask1?charset=utf8"
    SQLALCHEMY_DATABASE_URI = "mysql://root:abc123?@127.0.0.1:3306/MangeLinux?charset=utf8"

config = {
    'default':DevelopmentConfig
}
