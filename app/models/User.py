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


    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    words = db.relationship('Word', backref='user', lazy='dynamic')

    # def __init__(self, name, surname, email, password, role_id):
    #     self.name = name
    #     self.surname = surname
    #     self.email = email
    #     self.password = password
    #     self.role_id = role_id

    def __repr__(self):
        return '<User %r>' % self.name
