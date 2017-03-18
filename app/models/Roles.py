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


    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='roles', lazy='dynamic')

