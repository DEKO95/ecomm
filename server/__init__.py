from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app = Flask(__name__, root_path=os.getcwd())
# a little template for the future
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

from server import routes
from server import errors