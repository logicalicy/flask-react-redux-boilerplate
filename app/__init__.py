# Created with tutorials:
# https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
# http://flask.pocoo.org/docs/0.12/tutorial

from flask import Flask, g, render_template

from flask_sqlalchemy import SQLAlchemy

import sqlite3

# Define WSGI application object.
app = Flask(__name__)

# Configurations
app.config.from_object('config')
app.config.from_envvar('CONFIG', silent=True)

# Define database object.
db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.api.entries.controllers import mod as entries_module
from app.site.controllers import mod as site_module

# Register blueprint(s)
app.register_blueprint(entries_module)
app.register_blueprint(site_module)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
