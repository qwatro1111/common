from db import db

class AddressModel(db.Model):
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(80), nullable=False)
    street = db.Column(db.String(), nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.passport_id'))

class TenantModel(db.Model):
    __tablename__ = "tenants"

    passport_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer())
    sex = db.Column(db.String(80))
    address = db.relationship('AddressModel', backref='address')
    rooms = db.relationship('RoomModel', backref='rooms')

