import secrets
from datetime import datetime
from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from ticket_admin import models as ticket_admin_models

# from .manager import UserManager

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

DECK_TYPE = (('LOWER', 'LOWER'), ('UPPER', 'UPPER'))

class ParcelBooking(models.Model):
    route = models.ForeignKey(ticket_admin_models.Route, default=None, on_delete=models.PROTECT, related_name='parcel_route', editable=True)
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


class PassBooking(models.Model):
    route = models.ForeignKey(ticket_admin_models.Route, default=None, on_delete=models.PROTECT, related_name='pass_route')
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
    trip = models.ForeignKey(ticket_admin_models.Trip, default=None, on_delete=models.PROTECT, related_name='boat_booking_trip')
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
    deck_type = models.CharField(max_length = 100, verbose_name = "Lower Deck/Upper Deck", choices = DECK_TYPE, default = 'LOWER')
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
    trip = models.ForeignKey(ticket_admin_models.Trip, default=None, on_delete=models.PROTECT, related_name='ticket_booking_trip')
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