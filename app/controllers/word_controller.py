#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Controller for blog post functionality.
"""



from flask import Flask, jsonify

from json import dumps, loads

from app.models.User import User

from app.models.Word import Word


class WordController(object):
    """ Controller, that provide word saving and sending functionality. """

    def save_word(self, word):
        return dumps({'a':1})
