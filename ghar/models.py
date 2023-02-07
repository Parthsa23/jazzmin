import secrets
from datetime import datetime

from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# from .manager import UserManager

PORT_TYPE = (('OD pair', 'OD pair'), ('OO pair', 'OO pair'))
BOAT_CATEGORY = (('AC', 'AC'), ('Non-AC', 'Non-AC'))
BOAT_TYPE = (('TYP1', 'TYP1'), ('TYP2', 'TYP2'), ('TYP3', 'TYP3'))

def generate_pnr():
    return secrets.token_hex(3).upper()

# class CustomUser(AbstractUser):
#     phone_number = models.CharField(max_length=12, unique=True)
#     is_phone_verified = models. BooleanField (default=False)
#     otp = models.CharField(max_length=6)
#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []
#     objects = UserManager()

#     def __str__(self):
#         return self.phone_number

# User = get_user_model()

# Create your models here.

class Order(models.Model):
    order_product = models.CharField(max_length=100)
    order_amount = models.CharField(max_length=25)
    order_payment_id = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_product


class Port(models.Model):
    city_name = models.CharField(max_length=100, verbose_name="Port's City Name", default='')
    port_name = models.CharField(max_length=100, verbose_name="Port's Name", default=None)
    location_url = models.CharField(max_length=100, verbose_name="Port's Location URL", default=None)
    port_type = models.CharField(max_length = 100, verbose_name = "Port's Type", choices = PORT_TYPE, default = None)
    pet_allowed = models.BooleanField(default=1, verbose_name = "Pets Allowed")
    vehicle_allowed = models.BooleanField(default=1, verbose_name = "Vehicle Allowed")
    contact_number = models.CharField(max_length = 100, verbose_name = "Port's Contact Number", default = None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Port'
        verbose_name_plural = 'Ports'

    def __str__(self):
        return str(self.port_name)

class ValueAddedService(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name", default=None)
    type = models.CharField(max_length=100, verbose_name="Type", default=None)
    price = models.CharField(max_length=100, verbose_name="Price", default=None)
    gst_rate = models.CharField(max_length=100, verbose_name="GST % applicable", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Value Added Service'
        verbose_name_plural = 'Value Added Services'

    def __str__(self):
        return str(self.name)

class BoatOwner(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="Company's name", default=None)
    owner_name = models.CharField(max_length=100, verbose_name="owneer's name", default=None)
    company_address = models.TextField(verbose_name="Address", default=None)
    company_mobile = models.CharField(max_length=100, verbose_name="Mobile Number", default=None)
    company_email = models.EmailField(max_length=100, verbose_name="Mobile E-mail", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Boat Owner'
        verbose_name_plural = 'Boat Owners'

    def __str__(self):
        return str(self.company_name)

class Boat(models.Model):
    number = models.CharField(max_length=100, verbose_name="Number", default=None)
    name = models.CharField(max_length=100, verbose_name="Name", default=None)
    pax_capacity = models.IntegerField(verbose_name="PAX Capacity", default=None)
    vehicle_capacity = models.IntegerField(verbose_name="Vehicle Capacity", default=None)
    pet_capacity = models.IntegerField(verbose_name="Pet Capacity", default=None)
    boat_category = models.CharField(max_length = 100, verbose_name = "Port's Type", choices = BOAT_CATEGORY, default = None)
    boat_type = models.CharField(max_length=100, verbose_name="Boat Type", choices = BOAT_TYPE ,default=None)
    lower_deck_fare = models.IntegerField(verbose_name="Lower Deck Fare", default=None)
    upper_deck_fare = models.IntegerField(verbose_name="Upper Deck Fare", default=None)
    boat_owner = models.ForeignKey(BoatOwner, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Boat'
        verbose_name_plural = 'Boats'

    def __str__(self):
        return str(self.name)

class Vehicle(models.Model):
    type = models.CharField(max_length=100, verbose_name="Vehicle Type", default=None)
    model = models.CharField(max_length=100, verbose_name="Vehicle Model", default=None)
    price = models.CharField(max_length=100, verbose_name="Vehicle Price", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Vehicle Type'
        verbose_name_plural = 'Vehicle Types'

    def __str__(self):
        return str(self.type)

class Pet(models.Model):
    type = models.CharField(max_length=100, verbose_name="Pet Type", default=None)
    weight = models.CharField(max_length=100, verbose_name="Pet Weight", default=None)
    price = models.CharField(max_length=100, verbose_name="Pet Price", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Pet Type'
        verbose_name_plural = 'Pet Types'

    def __str__(self):
        return str(self.type)

class Route(models.Model):
    source = models.ForeignKey(Port, on_delete=models.PROTECT, related_name='source', null=False, default=None)
    destination = models.ForeignKey(Port, on_delete=models.PROTECT, related_name='destination', null=False, default=None)
    duration = models.IntegerField(verbose_name="Journey Duration in Minutes", null=False, default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

    def __str__(self):
        return f"{self.source} - {self.destination}"

class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.PROTECT, related_name='route_id', null=False, default=None)
    boat = models.ForeignKey(Boat, on_delete=models.PROTECT, related_name='boat_id', default=None, null=False)
    departure_date = models.DateField(default=datetime.now, verbose_name="Departure Date")
    departure_time = models.TimeField(default=datetime.now, verbose_name="Departure Time")
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'

    def __str__(self):
        return f"{self.route} by  {self.boat} on {self.departure_date} at {self.departure_time}"

class Parcel(models.Model):
    type = models.CharField(max_length=100, verbose_name="Parcel Type", default=None)
    weight = models.CharField(max_length=100, verbose_name="Parcel Weight", default=None)
    price = models.CharField(max_length=100, verbose_name="Parcel Price", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Parcel Type'
        verbose_name_plural = 'Parcel Types'

    def __str__(self):
        return str(self.type)

class ParcelBooking(models.Model):
    route = models.ForeignKey(Route, default=None, on_delete=models.PROTECT, related_name='parcel_route', editable=True)
    tracking_id = models.CharField(max_length=100, verbose_name="Tracking ID", default=generate_pnr, editable=False)
    sender_name = models.CharField(max_length=100, verbose_name="Sender Name", default=None)
    sender_email = models.EmailField(verbose_name="Sender Email", default=None)
    sender_mobile = models.CharField(max_length=100, verbose_name="Sender Mobile", default=None)
    receiver_name = models.CharField(max_length=100, verbose_name="Receiver Name", default=None)
    receiver_email = models.EmailField(verbose_name="Receiver Email", default=None)
    receiver_mobile = models.CharField(max_length=100, verbose_name="Receiver Mobile", default=None)
    gst_number = models.CharField(max_length=100, verbose_name="GST Number (if applicable)", default=None, null=True)
    discount_percentage = models.IntegerField(verbose_name="Discount %", default=None)
    discount_amount = models.IntegerField(verbose_name="Discount Amount", default=None)
    amount_payable = models.IntegerField(verbose_name="Amount Payable", default=None)
    bank_transection_id = models.CharField(max_length=100, verbose_name="Bank Transection ID", default=None, editable=False)
    payment_success = models.BooleanField(default=False, verbose_name="Payment Success", editable=False)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)
    class Meta:
        verbose_name = 'Parcel Booking'
        verbose_name_plural = 'Parcel Bookings'

    def __str__(self):
        return str(self.tracking_id)

class ParcelInfo(models.Model):
    parcel = models.ForeignKey(ParcelBooking, default=None, on_delete=models.CASCADE, related_name='parcel_info', editable=False)
    type = models.CharField(max_length=100, verbose_name="Parcel Type", default=None)
    weight = models.CharField(max_length=100, verbose_name="Parcel Weight", default=None)
    quantity = models.IntegerField(verbose_name="Parcel Quantity", default=None)
    price = models.IntegerField(verbose_name="Parcel Price", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Parcel Info'
        verbose_name_plural = 'Parcels Info'

    def __str__(self):
        return str(self.type)

class Pass(models.Model):
    day = models.IntegerField(verbose_name="Validity Days", default=None)
    trip = models.IntegerField(verbose_name="Trips count", default=None)
    price = models.IntegerField(verbose_name="Pass Price", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Pass Info'
        verbose_name_plural = 'Passes Info'

    def __str__(self):
        return f"{self.day} days/{self.trip} trips"

class PassBooking(models.Model):
    route = models.ForeignKey(Route, default=None, on_delete=models.PROTECT, related_name='pass_route')
    pass_number = models.CharField(max_length=100, verbose_name="Pass Number", default=generate_pnr, editable=False)
    pax_count = models.IntegerField(verbose_name="PAX Count", default=None)
    vehicle_count = models.IntegerField(verbose_name="Vehicle Count", default=None, null=True)
    pet_count = models.IntegerField(verbose_name="Pet Count", default=None, null=True)
    trips_allowed = models.IntegerField(verbose_name="Trips Allowed", default=None)
    validity_days = models.IntegerField(verbose_name="Validity", default=None)
    pass_start_timestamp = models.DateTimeField(default=datetime.now, verbose_name="Pass Start Timestamp")
    pass_expiry_timestamp = models.DateTimeField(default=datetime.now, verbose_name="Pass Expiry Timestamp")
    coupon_code = models.CharField(max_length=100, verbose_name="Coupon Code", default=None)
    total_fare = models.IntegerField(verbose_name="Total Fare", default=None)
    tax  = models.IntegerField(verbose_name="Tax applied", default=None)
    gst_number = models.CharField(max_length=100, verbose_name="GST Number (if applicable)", default=None, null=True)
    discount_percentage = models.IntegerField(verbose_name="Discount %", default=None)
    discount_amount = models.IntegerField(verbose_name="Discount Amount", default=None)
    payable_amount = models.IntegerField(verbose_name="Payable Amount", default=None)
    bank_transection_id = models.CharField(max_length=100, verbose_name="Bank Transection ID", default=None, editable=False)
    payment_success = models.BooleanField(default=False, verbose_name="Payment Success", editable=False)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Pass Booking'
        verbose_name_plural = 'Pass Bookings'

    def __str__(self):
        return f"{self.pass_number}"

class PassCustomerInfo(models.Model):
    pass_id = models.ForeignKey(PassBooking, default=None, on_delete=models.CASCADE, related_name='pass_customer_info')
    name = models.CharField(max_length=100, verbose_name="Customer Name", default=None, null=True)
    mobile = models.CharField(max_length=100, verbose_name="Customer Mobile", default=None, null=True)
    email = models.EmailField(verbose_name="Customer Email", default=None, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Pass Customer Info'
        verbose_name_plural = 'Pass Customers Info'

    def __str__(self):
        return str(self.name)

class PassVehicleInfo(models.Model):
    pass_id = models.ForeignKey(PassBooking, default=None, on_delete=models.CASCADE, related_name='pass_vehicle_info')
    model = models.CharField(max_length=100, verbose_name="Vehicle Model", default=None, null=True)
    type = models.CharField(max_length=100, verbose_name="Vehicle Type", default=None, null=True)
    registration_number = models.CharField(max_length=100, verbose_name="Vehicle Registration number", default=None, null=True)
    price = models.CharField(max_length=100, verbose_name="Price", default=None, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Pass Vehicle Info'
        verbose_name_plural = 'Pass Vehicles Info'

    def __str__(self):
        return str(self.type)

class PassPetInfo(models.Model):
    pass_id = models.ForeignKey(PassBooking, default=None, on_delete=models.CASCADE, related_name='pass_pet_info')
    name = models.CharField(max_length=100, verbose_name="Pet Name", default=None, null=True)
    type = models.CharField(max_length=100, verbose_name="Pet Type", default=None, null=True)
    weight = models.CharField(max_length=100, verbose_name="Pet Weight", default=None, null=True)
    price = models.CharField(max_length=100, verbose_name="Price", default=None, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Pass Pet Info'
        verbose_name_plural = 'Pass Pets Info'

    def __str__(self):
        return str(self.type)

class BoatBooking(models.Model):
    trip = models.ForeignKey(Trip, default=None, on_delete=models.PROTECT, related_name='boat_booking_trip')
    pnr = models.CharField(max_length=100, verbose_name="PNR Number", default=generate_pnr, editable=False)
    booking_duration = models.IntegerField(verbose_name="Booking Durtion (Minuts)", default=None)
    booking_start_timestamp = models.CharField(max_length=100, default=None, verbose_name="Booking Start Timestamp")
    booking_end_timestamp = models.CharField(max_length=100, default=None, verbose_name="Booking End Timestamp")
    pax_count = models.IntegerField(verbose_name="PAX Count", default=None)
    vehicle_count = models.IntegerField(verbose_name="Vehicle Count", default=None, null=True)
    pet_count = models.IntegerField(verbose_name="Pet Count", default=None, null=True)
    vas_count = models.IntegerField(verbose_name="Value Added Service Count", default=None)
    coupon_code = models.CharField(max_length=100, verbose_name="Coupon Code", default=None)
    total_fare = models.IntegerField(verbose_name="Total Fare", default=None)
    tax = models.IntegerField(verbose_name="Tax Applied", default=None)
    cess = models.IntegerField(verbose_name="Cess Applied", default=None)
    port_levy = models.IntegerField(verbose_name="Port Levy Applied", default=None)
    gst_number = models.CharField(max_length=100, verbose_name="GST Number (if applicable)", default=None, null=True)
    discount_percentage = models.IntegerField(verbose_name="Discount %", default=None)
    discount_amount = models.IntegerField(verbose_name="Discount Amount", default=None)
    payable_amount = models.IntegerField(verbose_name="Payable Amount", default=None)
    bank_transection_id = models.CharField(max_length=100, verbose_name="Bank Transection ID", default=None, editable=False)
    payment_success = models.BooleanField(default=False, verbose_name="Payment Success", editable=False)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Boat Booking'
        verbose_name_plural = 'Boat Bookings'

    def __str__(self):
        return f"{self.pnr}"

class BoatCustomerInfo(models.Model):
    boat_booking_id = models.ForeignKey(BoatBooking, default=None, on_delete=models.CASCADE, related_name='boat_customer_info')
    name = models.CharField(max_length=100, verbose_name="Customer Name", default=None, null=True)
    mobile = models.CharField(max_length=100, verbose_name="Customer Mobile", default=None, null=True)
    email = models.EmailField(verbose_name="Customer Email", default=None, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Boat Customer Info'
        verbose_name_plural = 'Boat Customers Info'

    def __str__(self):
        return str(self.name)

class BoatVehicleInfo(models.Model):
    boat_booking_id = models.ForeignKey(BoatBooking, default=None, on_delete=models.CASCADE, related_name='boat_vehicle_info')
    type = models.CharField(max_length=100, verbose_name="Vehicle Type", default=None, null=True)
    model = models.CharField(max_length=100, verbose_name="Vehicle Model", default=None, null=True)
    registration_number = models.CharField(max_length=100, verbose_name="Vehicle Registration number", default=None, null=True)
    price = models.CharField(max_length=100, verbose_name="Price", default=None, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Boat Vehicle Info'
        verbose_name_plural = 'Boat Vehicles Info'

    def __str__(self):
        return str(self.type)

class BoatPetInfo(models.Model):
    boat_booking_id = models.ForeignKey(BoatBooking, default=None, on_delete=models.CASCADE, related_name='boat_pet_info')
    name = models.CharField(max_length=100, verbose_name="Pet Name", default=None, null=True)
    type = models.CharField(max_length=100, verbose_name="Pet Type", default=None, null=True)
    weight = models.CharField(max_length=100, verbose_name="Pet Weight", default=None, null=True)
    price = models.CharField(max_length=100, verbose_name="Price", default=None, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Boat Pet Info'
        verbose_name_plural = 'Boat Pets Info'

    def __str__(self):
        return str(self.name)

class BoatVASInfo(models.Model):
    boat_booking_id = models.ForeignKey(BoatBooking, default=None, on_delete=models.CASCADE, related_name='boat_vas_info')
    name = models.CharField(max_length=100, verbose_name="Service Name", default=None, null=True)
    type = models.CharField(max_length=100, verbose_name="Service Type", default=None, null=True)
    price = models.CharField(max_length=100, verbose_name="Price", default=None, null=True)
    tax = models.CharField(max_length=100, verbose_name="Service Tax", default=None, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Boat Value Added Service Info'
        verbose_name_plural = 'Boat Value Added Services Info'

    def __str__(self):
        return str(self.name)

class TicketBooking(models.Model):
    pnr = models.CharField(max_length=10, verbose_name="PNR Number", default=generate_pnr, unique=True, editable=False)
    pax_count = models.IntegerField(verbose_name="PAX Count", default=None)
    vehicle_count = models.IntegerField(verbose_name="Vehicle Count", default=None, null=True)
    pet_count = models.IntegerField(verbose_name="Pet Count", default=None, null=True)
    vas_count = models.IntegerField(verbose_name="Value Added Service Count", default=None)
    coupon_code = models.CharField(max_length=100, verbose_name="Coupon Code", default=None)
    pass_number = models.CharField(max_length=100, verbose_name="Pass Number", default=None)
    total_fare = models.IntegerField(verbose_name="Total Fare", default=None)
    tax = models.IntegerField(verbose_name="Tax Applied", default=None)
    cess = models.IntegerField(verbose_name="Cess Applied", default=None)
    port_levy = models.IntegerField(verbose_name="Port Levy Applied", default=None)
    gst_number = models.CharField(max_length=100, verbose_name="GST Number (if applicable)", default=None, null=True)
    discount_percentage = models.IntegerField(verbose_name="Discount %", default=None)
    discount_amount = models.IntegerField(verbose_name="Discount Amount", default=None)
    payable_amount = models.IntegerField(verbose_name="Payable Amount", default=None)
    bank_transection_id = models.CharField(max_length=100, verbose_name="Bank Transection ID", default=None, editable=False)
    payment_success = models.BooleanField(default=False, verbose_name="Payment Success", editable=False)
    created_by = models.ForeignKey(User, default=None, null=True, editable=False, on_delete=models.PROTECT)
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Ticket Booking'
        verbose_name_plural = 'Ticket Bookings'

    def __str__(self):
        return f"{self.pnr}"

class TicketTripInfo(models.Model):
    ticket_id = models.ForeignKey(TicketBooking, default=None, on_delete=models.CASCADE, related_name='ticket_trip_info')
    trip = models.ForeignKey(Trip, default=None, on_delete=models.PROTECT, related_name='ticket_booking_trip')
    created_by = models.ForeignKey(User, default=None, null=True, editable=False, on_delete=models.PROTECT)
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Ticket Trip Info'
        verbose_name_plural = 'Ticket Trips Info'

    def __str__(self):
        return f"{self.trip}"

class TicketCustomerInfo(models.Model):
    ticket_id = models.ForeignKey(TicketBooking, default=None, on_delete=models.CASCADE, related_name='ticket_customer_info')
    name = models.CharField(max_length=100, verbose_name="Customer Name", default=None)
    mobile = models.CharField(max_length=100, verbose_name="Customer Mobile", default=None)
    email = models.EmailField(verbose_name="Customer Email", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Ticket Customer Info'
        verbose_name_plural = 'Ticket Customers Info'

    def __str__(self):
        return str(self.name)

class TicketVehicleInfo(models.Model):
    ticket_id = models.ForeignKey(TicketBooking, default=None, on_delete=models.CASCADE, related_name='ticket_vehicle_info')
    type = models.CharField(max_length=100, verbose_name="Vehicle Type", default=None, null=True)
    model = models.CharField(max_length=100, verbose_name="Vehicle Model", default=None, null=True)
    registration_number = models.CharField(max_length=100, verbose_name="Vehicle Registration number", default=None, null=True)
    price = models.CharField(max_length=100, verbose_name="Price", default=None, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Ticket Vehicle Info'
        verbose_name_plural = 'Ticket Vehicles Info'

    def __str__(self):
        return str(self.type)

class TicketPetInfo(models.Model):
    ticket_id = models.ForeignKey(TicketBooking, default=None, on_delete=models.CASCADE, related_name='ticket_pet_info')
    name = models.CharField(max_length=100, verbose_name="Pet Name", default=None, null=True)
    type = models.CharField(max_length=100, verbose_name="Pet Type", default=None, null=True)
    weight = models.CharField(max_length=100, verbose_name="Pet Weight", default=None, null=True)
    price = models.CharField(max_length=100, verbose_name="Price", default=None, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Ticket Pet Info'
        verbose_name_plural = 'Ticket Pets Info'

    def __str__(self):
        return str(self.name)

class TicketVASInfo(models.Model):
    ticket_id = models.ForeignKey(TicketBooking, default=None, on_delete=models.CASCADE, related_name='ticket_vas_info')
    name = models.CharField(max_length=100, verbose_name="Service Name", default=None, null=True)
    type = models.CharField(max_length=100, verbose_name="Service Type", default=None, null=True)
    price = models.CharField(max_length=100, verbose_name="Price", default=None, null=True)
    tax = models.CharField(max_length=100, verbose_name="Service Tax", default=None, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Ticket Value Added Service Info'
        verbose_name_plural = 'Ticket Value Added Services Info'

    def __str__(self):
        return str(self.name)