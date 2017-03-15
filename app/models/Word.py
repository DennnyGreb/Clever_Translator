#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Word table model.

Class Word implements model of the word table in database.

"""

from app import db


class Word(db.Model):

    """Class represents word model in database.

    Attributes:
        id: Internal word id in database.
        user_id: User's(who owns that word) id.
    	word_text: Word.
    """


    __tablename__ = 'USER'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.relationship('User', backref='word', lazy='dynamic')
    word_text = db.Column(db.String(255))
