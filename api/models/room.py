from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    StringField,
    IntField,
    DecimalField,
    DateTimeField
)


class Rooms(Document):
    room_type = StringField()
    max_capacity = IntField()
    rate = DecimalField()
    room_no = StringField()
    availabilty_status = StringField()
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField()
    description = StringField()
