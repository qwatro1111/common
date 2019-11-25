from flask_restful import Resource, request, marshal_with
from db import School, db
from structures import fields_structure

class SchoolResource(Resource):

    method_decorators = [marshal_with(fields_structure)]

    def get(self):
        return "Ok"

    def post(self):
        data = request.json
        school = School(**data)
        db.session.add(school)
        db.session.commit()

        return School.query.first(), 201
