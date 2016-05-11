__author__ = 'luoguoling'
from flask import Blueprint
oplog = Blueprint('oplog',__name__)
from . import views,errors