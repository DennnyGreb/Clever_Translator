#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Controller for blog post functionality.
"""



from flask import Flask, jsonify

from json import dumps, loads

from app import db

from app.models.User import User

#from app.models.Word import Word


class WordController(object):
    """ Controller, that provide word saving and sending functionality. """

    def save_word(self, word):
        db.session.add(User(name="Losha", surname="Grebenets", email="losha@gmail.com", password="pass", role_id=1))
        db.session.commit()
        return dumps({'a':1})
