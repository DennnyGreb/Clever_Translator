#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This module is for URL routing.
"""

import json

from flask import request, render_template, redirect, url_for, session, g

from app import app

from app.controllers.word_controller import WordController

_word = WordController()

@app.route('/', methods=['GET'])
def render_base():
    """ Root routing function """
    return render_template("index.html")
    
@app.route('/save_word', methods=['POST'])
def save_word():
    """ Word saving function """
    word = request.form['word']
    return _word.save_word(word)