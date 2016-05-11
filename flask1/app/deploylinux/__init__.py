__author__ = 'luoguoling'
from flask import Blueprint
deploylinux = Blueprint('deploylinux',__name__)
from . import views,errors