from flask import Blueprint, request, json
from flask_restful import Api, Resource, current_app, marshal_with
from db import db
from .structure import tenant_structure, address_structure

from .models import TenantModel, AddressModel


class TenantResource(Resource):
    @marshal_with(tenant_structure)
    def get(self, id=None):
        if id:
            return TenantModel.query.get(id)
        return TenantModel.query.all()

    @marshal_with(tenant_structure)
    def post(self):
        data = json.loads(request.data)
        for dataTenant in data:
            db.session.add(TenantModel(**dataTenant))
            db.session.commit()
        return TenantModel.query.all()

    @marshal_with(tenant_structure)
    def patch(self, id=None):
        data = json.loads(request.data)[0]
        tenant = TenantModel.query.get(id)
        if tenant:
            tenant.name = data['name']
            tenant.age = data['age']
            tenant.sex = data['sex']
            db.session.commit()
        return TenantModel.query.get(id)

    @marshal_with(tenant_structure)
    def delete(self, id):
        tenants = TenantModel.query.get(id)
        if tenants:
            db.session.delete(tenants)
            db.session.commit()
        return TenantModel.query.all()

class AddressResource(Resource):
    @marshal_with(address_structure)
    def get(self, id=None):
        if id:
            return AddressModel.query.get(id)
        return AddressModel.query.all()

    @marshal_with(address_structure)
    def post(self):
        data = json.loads(request.data)
        for addressTenant in data:
            address = AddressModel(**addressTenant)
            db.session.add(address)
        db.session.commit()
        return AddressModel.query.all()

    @marshal_with(address_structure)
    def patch(self, id=None):
        data = json.loads(request.data)[0]
        address = AddressModel.query.get(id)
        if address:
            address.city = data['city']
            address.street = data['street']
            address.tenant_id = data['tenant_id']
            db.session.commit()
        return AddressModel.query.get(id)

    @marshal_with(address_structure)
    def delete(self, id):
        address = AddressModel.query.get(id)
        if address:
            db.session.delete(address)
            db.session.commit()
        return AddressModel.query.all()
