#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Roles table model.

Class Roles implements model of the role table in database.

"""

from app import db


class Roles(db.Model):

    """Class Roles represents role model in database.

    Attributes:
        id: Internal role id in database.
        name: Role name.
    """


    __tablename__ = 'Roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    user = db.relationship('User', backref=db.backref('roles', lazy='joined'), lazy='dynamic')