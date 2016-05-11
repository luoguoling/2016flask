__author__ = 'luoguoling'
from flask import Blueprint
excommand = Blueprint('excommand',__name__)
from . import views,errors