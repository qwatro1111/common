from flask import Blueprint, request, json
from flask_restful import Api, Resource, fields, marshal_with

tenant = Blueprint('tenant', __name__)
api = Api(tenant)

class Tenant:
    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number

addresss_resource = {
    'city': fields.String,
    'street': fields.String
}

resource = {
    'name': fields.String,
    'passport_id': fields.String,
    'age': fields.Integer,
    'sex': fields.String,
    'address': fields.Nested(addresss_resource),
    'room_number': fields.Integer
}

tenant_list = [
    Tenant('Frodo', 'ID101', 51, 'male', {'city': 'Mordor', 'street': 'Sauron 22'}, 12),
    Tenant('Sam', 'ID102', 36, 'male', {'city': 'Mordor', 'street': 'Sauron 22'}, 11),
    Tenant('Merry', 'ID103', 26, 'male', {'city': 'Fangorn', 'street': 'entova 33'}, 10),
    Tenant('Pippin', 'ID104', 25, 'male', {'city': 'Fangorn', 'street': 'entova 33'}, 22)
]

class TenantResource(Resource):
    @marshal_with(resource)
    def get(self, passport_id=None):
        if passport_id:
            new_tenant_list = [tenant for tenant in tenant_list if str(tenant.passport_id) == passport_id]
            return new_tenant_list
        return tenant_list

    @marshal_with(resource)
    def patch(self):
        data = request.json
        for tenant_request in data:
            for tenant in tenant_list:
                if tenant.passport_id == tenant_request['passport_id']:
                    tenant.name = tenant_request['name']
                    tenant.passport_id = tenant_request['passport_id']
                    tenant.age = tenant_request['age']
                    tenant.sex = tenant_request['sex']
                    tenant.address = tenant_request['address']
                    tenant.room_number = tenant_request['room_number']
                    break
        return tenant_list

    @marshal_with(resource)
    def delete(self, passport_id):
        for tenant in tenant_list:
            if tenant.passport_id == passport_id:
                tenant_list.remove(tenant)
                break
        return tenant_list

api.add_resource(TenantResource, '/tenants', '/tenants/<passport_id>')
