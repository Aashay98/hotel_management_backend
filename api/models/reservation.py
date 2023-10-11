from datetime import datetime
from mongoengine.fields import (
    StringField,
    IntField,
    DecimalField,
    DateTimeField,
    DateField,
    ReferenceField,
    BooleanField,
    ListField,
    EmbeddedDocumentField
)
from mongoengine import Document, EmbeddedDocument


class GuestReservation(Document):
    check_out_date = DateField()
    check_in_date = DateField()
    total_price = DecimalField()
    nights = IntField()
    room = ReferenceField("Rooms")
    status = StringField()
    guest = ReferenceField("GuestProfile")
    reservation_type = StringField()
    reserved_by = StringField()
    notes = StringField()
    is_deleted = BooleanField()
    no_of_people = IntField()
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField()


class AdditionalChargeDetail(EmbeddedDocument):
    type = StringField()
    note = StringField()
    charge = DecimalField()
    date = DateTimeField()


class PaymentTransaction(Document):
    payment_date = DateTimeField()
    refund_date = DateTimeField()
    total_amount_paid = DecimalField()
    additional_charges = EmbeddedDocumentField(ListField(AdditionalChargeDetail))
    guest = ReferenceField("GuestProfile")
    reservation = ReferenceField("GuestReservation")
    payment_status = StringField()
    payment_type = StringField()
    card_number = StringField()
    card_expire_date = StringField()
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField()
