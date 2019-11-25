from flask import Blueprint, request, json
from flask_restful import Api, Resource, fields, marshal_with

from .routes import TenantResource, AddressResource

tenant = Blueprint('tenant', __name__)
api = Api(tenant)

api.add_resource(TenantResource, '/tenants', '/tenants/<id>')
api.add_resource(AddressResource, '/address', '/address/<id>')
