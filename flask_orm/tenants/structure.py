from flask_restful import fields
from rooms.structure import room_structure

address_structure = {
    'city': fields.String,
    'street': fields.String
}

tenant_structure = {
    'passport_id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'sex': fields.String,
    'address': fields.Nested(address_structure),
    'rooms': fields.Nested(room_structure)
}
