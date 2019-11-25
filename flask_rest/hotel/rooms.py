from flask import Blueprint, request, json
from flask_restful import Api, Resource, fields, marshal_with

room = Blueprint('room', __name__)
api = Api(room)

class Room:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price

    def getValue(self, key):
        if key == 'number':
            return self.number
        if key == 'level':
            return self.level
        if key == 'status':
            return self.status
        if key == 'price':
            return self.price
        return None

resource = {
    'number': fields.Integer,
    'level': fields.String,
    'status': fields.String,
    'price': fields.Integer
}

room_list = [
    Room(1, 'first', 'open', 101),
    Room(2, 'first', 'closed', 102),
    Room(3, 'second', 'open', 103),
    Room(4, 'second', 'closed', 104)
]

class RoomResource(Resource):
    @marshal_with(resource)
    def get(self, id=None):
        if id:
            room = [room for room in room_list if str(room.number) == id]
            return room
        if request.args:
            for arg in request.args:
                new_room_list = [room for room in room_list if str(room.getValue(arg)) == request.args[arg]]
                return new_room_list
        return room_list

    @marshal_with(resource)
    def post(self):
        data = request.json
        for room in data:
            room_list.append(Room(
                room['number'],
                room['level'],
                room['status'],
                room['price']
            ))
        return room_list

    @marshal_with(resource)
    def patch(self):
        data = request.json
        for room_request in data:
            for room in room_list:
                if room_request['number'] == room.number:
                    room.number = room_request['number']
                    room.level = room_request['level']
                    room.status = room_request['status']
                    room.price = room_request['price']
                    break
        return room_list

    @marshal_with(resource)
    def delete(self, id):
        for room in room_list:
            if room.number == int(id):
                room_list.remove(room)
                break
        return room_list

api.add_resource(RoomResource, '/rooms', '/rooms/<id>')
