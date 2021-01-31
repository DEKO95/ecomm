import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth

# TODO: app factory pattern
app = Flask(__name__, root_path=os.getcwd())

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
auth = HTTPBasicAuth()

from server.api import bp as api_bp
# blueprint is used only for url prefix for now
app.register_blueprint(api_bp, url_prefix='/api')

from server import models
from server import routes