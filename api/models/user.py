from datetime import datetime
from tokenize import String
from mongoengine import Document
from mongoengine.fields import (
    StringField,
    BooleanField,
    EmailField,
    DateTimeField,
    ListField
)

class Admin(Document):
    email = EmailField()
    first_name = StringField()
    last_name = StringField()
    password = StringField()
    username = StringField()
    created = DateTimeField(default=datetime.now)
    role = StringField(default='admin')
    permissions = ListField(StringField(),
                            default=['delete_staff',
                                     'assign_persimssions',
                                     'create_staff',
                                     'change_reservations',
                                     'charge_customers',
                                     'assign_rooms',
                                     'change_rooms',
                                     'extra_charge_customers',
                                     'refund_customers'])


class Staff(Document):
    email = EmailField()
    first_name = StringField()
    last_name = StringField()
    password = StringField()
    username = StringField()
    is_deleted=BooleanField(default=False)
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField()
    role = StringField(default='front_desk')
    permissions = ListField(StringField(),
                            default=['change_reservations',
                                    'charge_customers',
                                     'assign_rooms',
                                     'change_rooms',
                                     'extra_charge_customers',
                                     'refund_customers'])


class Customer(Document):
    username = StringField()
    password = StringField()
    first_name = StringField()
    last_name = StringField()
    phone = StringField()
    email = EmailField()
    address1 = StringField()
    address2 = StringField()
    state = StringField()
    zip_code = StringField()
    country = StringField()
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField()
    is_deleted = BooleanField(default=False)
