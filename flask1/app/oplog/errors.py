__author__ = 'luoguoling'
from flask import  render_template
from . import oplog
@oplog.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
@oplog.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')

