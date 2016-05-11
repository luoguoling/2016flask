__author__ = 'luoguoling'
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from . import main
from .. import db
from ..models import User,Alticle
@main.route('/')
def show_entries():
    entries=Alticle.query.with_entities(Alticle.title,Alticle.text).all()
    return render_template('main/show_entries.html', entries=entries)
@main.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    print request.form['title']
    new_alticlee=Alticle(userId=12,title=request.form['title'],text=request.form['text'])
    db.session.add(new_alticlee)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('main.show_entries'))
@main.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        res=User.query.filter_by(username=request.form['username'],password=request.form['password']).first()
        print res
        if res==None:
            error = 'Invalid username or password11'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('main.show_entries'))
    return render_template('main/login.html', error=error)
@main.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('main.show_entries'))