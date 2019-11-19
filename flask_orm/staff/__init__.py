from flask import Blueprint, request, json
from flask_restful import Api, Resource, fields, marshal_with

from .routes import StaffResource, StaffAndRoom

staff = Blueprint('staff', __name__)
api = Api(staff)

api.add_resource(StaffResource, '/staff', '/staff/<passport_id>')
api.add_resource(StaffAndRoom, '/staff_and_room')
