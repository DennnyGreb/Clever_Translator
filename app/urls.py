#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is for URL routing.
"""

import json

from flask import request, render_template, redirect, url_for, session, g

from app import app, db

from app.models.User import User

from app.models.Roles import Roles

from app.models.Word import Word

from app.controllers.word_controller import WordController

_word = WordController()

@app.route('/', methods=['GET'])
def render_base():
    """ Root routing function """
    return render_template("index.html")

@app.route('/test', methods=['GET'])
def test():    
    admin_role = db.session.query(Roles).get(1)
    db.session.add(User(name="Losha2", surname="Grebenets", 
    email="losha@gmail.com", password="pass", roles=admin_role))    
    db.session.commit()    
    return 'OK'

@app.route('/test2', methods=['GET'])
def test2():    
    db.session.add(Word(user_id=1, word_text="Russian Dimon"))
    db.session.commit()    
    return 'OK'

@app.route('/save_word', methods=['POST'])
def save_word():
    """ Word saving function """
    word = request.form['word']
    return _word.save_word(word)