#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""User table model.

Class User implements model of the user table in database.

"""

from app import db


class User(db.Model):

    """Class represents user model in database.

    Attributes:
        id: Internal user id in database.
        name: User name.
	    surname: User surname
        email: User email.
        password: user pass.
	    role_id: User role id.
    """


    __tablename__ = 'User'

    id = db.Column(db.Integer, db.ForeignKey('word.user_id'), primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role_id = db.relationship('Roles', backref='user', lazy='dynamic')
