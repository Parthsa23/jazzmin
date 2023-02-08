import secrets
from datetime import datetime
from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# from .manager import UserManager

PORT_TYPE = (('OD pair', 'OD pair'), ('OO pair', 'OO pair'))
BOAT_TYPE = (('Hire', 'Hire'), ('Charter', 'Charter'))

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
    contact_name = models.CharField(max_length=100, verbose_name="Port's Contact Person", default=None)
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
    sub_company_name = models.CharField(max_length=100, verbose_name="Sub-Company's name", default=None)
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

class BoatCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Boat's Category", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Boat Category Master'
        verbose_name_plural = 'Boat Categories Master'

    def __str__(self):
        return str(self.name)

class BoatType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Boat's Type", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Boat Type Master'
        verbose_name_plural = 'Boats Type Master'

    def __str__(self):
        return str(self.name)

class Boat(models.Model):
    number = models.CharField(max_length=100, verbose_name="Number", default=None)
    name = models.CharField(max_length=100, verbose_name="Name", default=None)
    pax_capacity = models.IntegerField(verbose_name="PAX Capacity", default=None)
    vehicle_capacity = models.IntegerField(verbose_name="Vehicle Capacity", default=None)
    pet_capacity = models.IntegerField(verbose_name="Pet Capacity", default=None)
    boat_category = models.ForeignKey(BoatCategory, on_delete=models.PROTECT)
    boat_type = models.ForeignKey(BoatType, on_delete=models.PROTECT)
    hire_type = models.CharField(max_length = 100, verbose_name = "Hire/Charter", choices = BOAT_TYPE, default = None)
    lower_deck_seat = models.IntegerField(verbose_name="Lower Deck Seat", default=None)
    upper_deck_seat = models.IntegerField(verbose_name="Upper Deck Seat", default=None)
    commission = models.IntegerField(verbose_name="Commission %", default=None, null=True)
    flat_rate = models.IntegerField(verbose_name="Flat Rate", default=None, blank=True, null=True)
    boat_owner = models.ForeignKey(BoatOwner, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    def clean(self):
        cleaned_data = super().clean()
        seats = self.lower_deck_seat + self.upper_deck_seat
        print(self.pax_capacity == seats)
        if self.pax_capacity != seats:
            raise forms.ValidationError("PAX capacity should be equal to total seats in boat.")
        if self.flat_rate and self.commission:
            raise forms.ValidationError("Rates can be either commission or Flat. Can not be both.")
        

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

class RouteType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Boat's Type", default=None)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
    created_on = models.DateTimeField(default=datetime.now, editable=False)
    status = models.BooleanField(default=1, editable=False)

    class Meta:
        verbose_name = 'Route Return Type Master'
        verbose_name_plural = 'Route Return Type Master'

    def __str__(self):
        return str(self.name)

class Route(models.Model):
    source = models.ForeignKey(Port, on_delete=models.PROTECT, related_name='source', null=False, default=None)
    destination = models.ForeignKey(Port, on_delete=models.PROTECT, related_name='destination', null=False, default=None)
    route_return = models.ForeignKey(RouteType, on_delete=models.PROTECT, related_name='Route_Return_Type', null=False, default=None)
    duration = models.IntegerField(verbose_name="Journey Duration in Minutes", null=False, default=None)
    lower_deck_fare = models.IntegerField(verbose_name="Lower Deck Fare", default=None)
    upper_deck_fare = models.IntegerField(verbose_name="upper Deck Fare", null=True, default=None, blank=True)
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
    pet_booked = models.IntegerField(verbose_name="Pet Slots Booked", default=0, blank=True)
    vehicle_booked = models.IntegerField(verbose_name="Vehicle Slots Booked", default=0, blank=True)
    seat_booked_lower = models.IntegerField(verbose_name="Lower Deck Booked Sets", default=0, blank=True)
    seat_booked_upper = models.IntegerField(verbose_name="upper Deck Booked Sets", default=0, blank=True)
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

class Pass(models.Model):
    route = models.ForeignKey(Route, on_delete=models.PROTECT, related_name='pass_route_id', null=False, default=None)
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

# class AvailableSeats(models.Model):
#     trip = models.ForeignKey(Trip on_delete=models.PROTECT, related_name='seattrip_id', null=False, default=None)
#     boat = models.ForeignKey(Boat, on_delete=models.PROTECT, related_name='boat_id', default=None, null=False)
#     departure_date = models.DateField(default=datetime.now, verbose_name="Departure Date")
#     departure_time = models.TimeField(default=datetime.now, verbose_name="Departure Time")
#     pet_booked = models.IntegerField(verbose_name="Pet Slots Booked", default=0, blank=True)
#     vehicle_booked = models.IntegerField(verbose_name="Vehicle Slots Booked", default=0, blank=True)
#     seat_booked_lower = models.IntegerField(verbose_name="Lower Deck Booked Sets", default=0, blank=True)
#     seat_booked_upper = models.IntegerField(verbose_name="upper Deck Booked Sets", default=0, blank=True)
#     created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, editable=False, related_name='+')
#     created_on = models.DateTimeField(default=datetime.now, editable=False)
#     status = models.BooleanField(default=1, editable=False)

#     class Meta:
#         verbose_name = 'Trip'
#         verbose_name_plural = 'Trips'

#     def __str__(self):
#         return f"{self.route} by  {self.boat} on {self.departure_date} at {self.departure_time}"