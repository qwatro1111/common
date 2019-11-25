from flask import Blueprint, request, json
from flask_restful import Api, Resource, fields, marshal_with
from db import db

from .models import RoomModel
from .structure import room_structure


class RoomResource(Resource):
    @marshal_with(room_structure)
    def get(self, id=None):
        if id:
            return RoomModel.query.get(id)
        if request.args.get('level'):
            print('level')
            return RoomModel.query.filter_by(level=request.args['level']).all()
        if request.args.get('status'):
            print('status')
            return RoomModel.query.filter_by(status=request.args['status']).all()
        if request.args.get('price'):
            print('price')
            return RoomModel.query.filter_by(price=request.args['price']).all()
        return RoomModel.query.all()

    @marshal_with(room_structure)
    def post(self):
        data = json.loads(request.data)
        for dataRoom in data:
            room = RoomModel(**dataRoom)
            db.session.add(room)
            db.session.commit()
        return data

    @marshal_with(room_structure)
    def patch(self, id):
        data = json.loads(request.data)[0]
        room = RoomModel.query.get(id)
        if room:
            room.level = data['level']
            room.status = data['status']
            room.price = data['price']
            room.tenant_id = data['tenant_id']
            db.session.commit()
        return RoomModel.query.get(id)

    @marshal_with(room_structure)
    def delete(self, id):
        room = RoomModel.query.get(id)
        if room:
            db.session.delete(room)
            db.session.commit()
        return RoomModel.query.all()
