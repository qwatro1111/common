from flask import Blueprint, request, json
from flask_restful import Api, Resource, fields, marshal_with

staff = Blueprint('staff', __name__)
api = Api(staff)

class Staff:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary

resource = {
    'name': fields.String,
    'passport_id': fields.String,
    'position': fields.String,
    'salary': fields.String
}

staff_list = [
    Staff('Sauron', '001', 'administrator', 100),
    Staff('Saruman', '002', 'manager', 90),
]

class StaffResource(Resource):
    @marshal_with(resource)
    def get(self, passport_id=None):
        if passport_id:
            new_staff_list = [staff for staff in staff_list if str(staff.passport_id) == passport_id]
            return new_staff_list
        return staff_list

    @marshal_with(resource)
    def patch(self):
        data = request.json
        for staff_request in data:
            for staff in staff_list:
                if staff.passport_id == staff_request['passport_id']:
                    staff.name = staff_request['name']
                    staff.passport_id = staff_request['passport_id']
                    staff.position = staff_request['position']
                    staff.salary = staff_request['salary']
                    break
        return staff_list

    @marshal_with(resource)
    def delete(self, passport_id):
        for tenant in staff_list:
            if tenant.passport_id == passport_id:
                staff_list.remove(tenant)
                break
        return staff_list

api.add_resource(StaffResource, '/staff', '/staff/<passport_id>')
