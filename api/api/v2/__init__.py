from flask import Blueprint
from flask_restplus import Api

from simple import api as simple_api

api = Blueprint('v2 api', __name__)
Api(api).add_namespace(simple_api)
