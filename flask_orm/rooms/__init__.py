from flask import Blueprint
from flask_restful import Api

from .routes import RoomResource

room = Blueprint('room', __name__)
api = Api(room)


api.add_resource(RoomResource, '/rooms', '/rooms/<id>')
