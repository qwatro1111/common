from flask_restful import fields
from rooms.structure import room_structure

staff_structure = {
    'passport_id': fields.String,
    'name': fields.String,
    'position': fields.String,
    'salary': fields.String,
    'rooms': fields.Nested(room_structure)
}
