from datetime import datetime
from mongoengine.fields import (
    StringField,
    IntField,
    DecimalField,
    DateTimeField,
    DateField,
    ReferenceField,
    BooleanField,
    EmbeddedDocumentField
)
from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentListField


class GuestReservation(Document):
    expected_check_out_date = DateField()
    expected_check_in_date = DateField()
    total_price = DecimalField()
    nights = IntField()
    room = ReferenceField("Room")
    status = StringField()
    customer = ReferenceField("Customer")
    reservation_type = StringField()
    reserved_by = StringField()
    notes = StringField()
    is_deleted = BooleanField(default=False)
    no_of_people = IntField()
    guest_check_in_date = DateTimeField()
    guest_check_out_date = DateTimeField()
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField()


class AdditionalChargeDetail(EmbeddedDocument):
    type = StringField()
    note = StringField()
    charge = DecimalField()
    date = DateTimeField()


class RefundDetails(EmbeddedDocument):
    date=DateTimeField()
    reason=StringField()
    amount=DecimalField()
    refunded_by=StringField()


class CardDetails(EmbeddedDocument):
    type=StringField()
    card_number = StringField()
    expire_date = StringField()
    name_on_card=StringField()
    billing_address = StringField()
    billing_postal_code= StringField()


class PaymentTransaction(Document):
    payment_date = DateTimeField()
    refund_details = EmbeddedDocumentListField(RefundDetails)
    total_amount_paid = DecimalField()
    additional_charges = EmbeddedDocumentListField(AdditionalChargeDetail)
    customer = ReferenceField("Customer")
    reservation = ReferenceField("GuestReservation")
    payment_status = StringField()
    payment_type = StringField()
    payment_taken_by = StringField()
    card_details=EmbeddedDocumentField(CardDetails)
    created = DateTimeField(default=datetime.now)
    modified = DateTimeField()
