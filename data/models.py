from .db import db


class Lamp(db.Document):
    enlightenerName = db.StringField(required=True, unique=False)
    status = db.BooleanField(required=True, unique=False)
    priority = db.IntField(required=False, unique=True)
    porfilePic = db.StringField(required=False, unique=False)
