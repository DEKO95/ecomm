from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api', __name__)

api = Api(bp)

from server.api import endpoints, errors, auth

api.add_resource(endpoints.ItemResource, '/items/<int:id>')