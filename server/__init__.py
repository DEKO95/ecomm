import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# TODO: app factory pattern
app = Flask(__name__, root_path=os.getcwd())

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from server.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from server import models
from server import routes