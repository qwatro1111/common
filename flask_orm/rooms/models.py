from db import db

from tenants.models import TenantModel

class RoomModel(db.Model):
    __tablename__ = "rooms"

    number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.passport_id'))
