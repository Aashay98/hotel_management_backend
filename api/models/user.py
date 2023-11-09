from datetime import datetime
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
                                     'view_staff',
                                     'edit_staff',
                                     'add_reservation'
                                     'change_reservation',
                                     'delete_reservation',
                                     'view_reservation',
                                     'charge_customers',
                                     'change_customer_room',
                                     'add_room',
                                     'change_room'
                                     'delete_room',
                                     'view_room',
                                     'assign_customer_room',
                                     'add_customer',
                                     'view_customer'
                                     'delete_customer',
                                     'edit_customer',
                                     'add_payments',
                                     'edit_payments',
                                     'view_payments',
                                     'extra_charge_customers',
                                     'refund_payments'])


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
                            default=['add_reservation'
                                     'change_reservation',
                                     'delete_reservation',
                                     'view_reservation',
                                     'charge_customers',
                                     'change_customer_room',
                                     'add_room',
                                     'change_room'
                                     'delete_room',
                                     'view_room',
                                     'assign_customer_room',
                                     'add_customer',
                                     'view_customer'
                                     'delete_customer',
                                     'edit_customer',
                                     'add_payments',
                                     'edit_payments',
                                     'view_payments',
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
