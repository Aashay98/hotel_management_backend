from datetime import datetime
from mongoengine import Document
from mongoengine.fields import (
    StringField,
    BooleanField,
    EmailField,
    DateTimeField,
    ReferenceField
)


class User(Document):
    first_name = StringField()
    last_name = StringField()
    phone = StringField()
    email = EmailField()
    password = StringField()
    username = StringField()
    user_type = StringField()
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField()



class GuestProfile(Document):
    first_name = StringField()
    last_name = StringField()
    phone = StringField()
    email = EmailField()
    address1 = StringField()
    address2 = StringField()
    state = StringField()
    zip_code = StringField()
    country = StringField()
    user = ReferenceField("User")
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField()
    is_deleted = BooleanField(default=False)
