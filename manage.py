#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Manager
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db
from app.models.Roles import Roles
from app.models.User import User

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()