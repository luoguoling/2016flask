__author__ = 'luoguoling'
from . import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32),nullable=False)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User '{:s}'>".format(self.username)

class Alticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100),nullable=False)
    text = db.Column(db.String(3000),nullable=False)

    def __init__(self,userId,title,text):
        self.userid = userId
        self.title = title
        self.text = text
