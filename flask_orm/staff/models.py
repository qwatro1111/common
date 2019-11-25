from db import db

staff_and_room = db.Table(
    'staff_and_room',
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.passport_id')),
    db.Column('room_id', db.Integer, db.ForeignKey('rooms.number')),
)

class StaffModel(db.Model):
    __tablename__ = "staff"

    passport_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    rooms = db.relationship('RoomModel', secondary=staff_and_room, backref='staff')

    def __repr__(self):
        return f"<Staff {self.name}>"

