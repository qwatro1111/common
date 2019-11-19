from flask import Blueprint, request, json
from flask_restful import Api, Resource, fields, marshal_with
from db import db
from rooms.models import RoomModel
from .models import StaffModel, staff_and_room
from .structure import staff_structure


class StaffResource(Resource):
    @marshal_with(staff_structure)
    def get(self, passport_id=None):
        if passport_id:
            return StaffModel.query.get(passport_id)
        return StaffModel.query.all()

    @marshal_with(staff_structure)
    def post(self):
        data = request.json
        for staff in data:
            new_staff = StaffModel(**staff)
            db.session.add(new_staff)
        db.session.commit()
        return data

    @marshal_with(staff_structure)
    def patch(self, passport_id):
        data = json.loads(request.data)[0]
        staff = StaffModel.query.get(passport_id)
        if staff:
            staff.name = data['name']
            staff.position = data['position']
            staff.salary = data['salary']
            db.session.commit()
        return StaffModel.query.get(passport_id)

    @marshal_with(staff_structure)
    def delete(self, passport_id):
        staff = StaffModel.query.get(passport_id)
        if staff:
            db.session.delete(staff)
            db.session.commit()
        return StaffModel.query.all()

class StaffAndRoom(Resource):
    def post(self):
        data = json.loads(request.data)
        for dataSAR in data:
            staff = StaffModel.query.get(dataSAR['staff_id'])
            room = RoomModel.query.get(dataSAR['room_id'])
            staff.rooms.append(room)
            db.session.commit()
        return "ok"
