from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    StringField,
    IntField,
    DecimalField,
    DateTimeField,
    DateField,
    BooleanField,
    ReferenceField
)

class RoomType(Document):
    date=DateField()
    type=StringField()
    no_of_available_room=IntField()
    is_deleted=BooleanField(default=False)
    created=DateTimeField(default=datetime.now)
    modified=DateTimeField()


class Room(Document):
    room_type = ReferenceField("RoomType")
    max_capacity = IntField()
    room_no = StringField()
    rate=DecimalField()
    availabilty_status = StringField()
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField()
    description = StringField()
