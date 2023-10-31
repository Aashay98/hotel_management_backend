from datetime import datetime, timedelta
from mongoengine import connect
from api.models.reservation import AdditionalChargeDetail, CardDetails, GuestReservation, PaymentTransaction, RefundDetails

from api.models.room import Room, RoomType
from api.models.user import Customer, Staff, Admin
connect('test_db')

room_type1 = RoomType()
room_type1.date=datetime.today().date()
room_type1.type='Single queen bed'
room_type1.no_of_available_room=9
room_type1.created=datetime.now()
room_type1.save()

room_type2 = RoomType()
room_type2.date=datetime.today().date()
room_type2.type='Double queen bed'
room_type2.no_of_available_room=9
room_type2.created=datetime.now()
room_type2.save()


room_type3 = RoomType()
room_type3.date=datetime.today().date()
room_type3.type='Single king bed'
room_type3.no_of_available_room=5
room_type3.created=datetime.now()
room_type3.save()

room0 = Room(
    room_type = room_type1.pk,
    max_capacity = 2,
    rate = 75.15,
    room_no = '101',
    availabilty_status = "Available",
    description = "Have Free wifi, fridge, microwave and cable tv with complimentary breakfast"
)
room0.save()
room1 = Room(
    room_type = room_type2.pk,
    max_capacity = 4,
    rate = 95.15,
    room_no = '102',
    availabilty_status = "Blocked",
    description = "Have Free wifi, fridge, microwave and smart tv with complimentary breakfast"
)
room1.save()
room2 = Room(
    room_type = room_type3,
    max_capacity = 2,
    rate = 85.15,
    room_no = '118',
    availabilty_status = "Available",
    description = "Have Free wifi, fridge, microwave and smart tv with complimentary breakfast"
)
room2.save()
admin = Admin(
            first_name = "Admin",
            last_name = "1233",
            password = "admin@123",
            username = "admin123",
            email='admin123@gmail.com')
admin.save()
staff = Staff(
            first_name = "staff",
            last_name = "123",
            password = "staff@123",
            username = "staff1",
            email='staff1@gmail.com'
        )
staff.save()
for x in range(10):
    if x%2 ==0:
        guest_profile = Customer(
            first_name = "Sherlock"+str(x),
            last_name = "Holmes",
            phone = "816-647-291"+str(x),
            email = "sholmes"+str(x)+"@gmail.com",
            address1 = "221 B Bakers St",
            state = "NY",
            country = "US",
            zip_code = "12345",
            username = 'sholmes'+str(x),
            password = "sholmes@"+str(x)
        )
        guest_profile.save()
        reservation = GuestReservation(
            nights = 3,
            customer = guest_profile.pk,
            room = room0.pk,
            total_price = 81.22,
            status="Arrival",
            reservation_type = "online",
            reserved_by = staff.username,
            expected_check_in_date = datetime.today().date(),
            expected_check_out_date = (datetime.now()+timedelta(days=x)).date(),
            no_of_people=1,
            notes="Need extra pillow and 1 pet.",
        )
        reservation.save()

    else:
        guest_profile = Customer(
            first_name = "Hercule",
            last_name = "Poirot",
            phone = "816-647-291"+str(x),
            email = "sholmes"+str(x)+"@gmail.com",
            address1 = "221 B Bakers St",
            address2 = "APT 20",
            state = "NY",
            country = "US",
            zip_code = "12345",
            modified=datetime.now()
        )
        guest_profile.save()
        reservation = GuestReservation(
            nights = 3,
            customer = guest_profile.pk,
            room = room1.pk,
            total_price = 112.22,
            status="In-House",
            reservation_type = "in-person",
            reserved_by = admin.username,
            expected_check_in_date = datetime.today().date(),
            expected_check_out_date = (datetime.now()+timedelta(days=x)).date(),
            guest_check_in_date=datetime.now(),
            guest_check_out_date=datetime.now()+timedelta(days=x),
            no_of_people=3,
        )
        reservation.save()
        payment = PaymentTransaction(
            payment_date = datetime.now(),
            refund_details= [RefundDetails(
                date=datetime.now(),
                reason='Window not broke by customer',
                amount=150.00,
                refunded_by=admin.username
            )],
            customer = guest_profile.pk,
            reservation=reservation.pk,
            total_amount_paid=112.22,
            payment_status = 'Success',
            payment_type='card',
            payment_taken_by = staff.username,
            card_details = CardDetails(
                  type='Visa',
                  card_number='0000000000001234',
                  expire_date='09/22',
                  name_on_card='Agatha Christe',
                  billing_address='221B Bakers Street',
                  billing_postal_code='12345'
            ),
            additional_charges = [AdditionalChargeDetail(
                type='Incidentals',
                charge = 150.00,
                date = datetime.now(),
                note="broken Window."
            ),
            AdditionalChargeDetail(
                type='Pet Fee',
                charge = 45.00,
                date = datetime.now(),
                note="$15 per night for pet."
            )]
        )
        payment.save()
