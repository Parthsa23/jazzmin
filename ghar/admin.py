from django.contrib import admin
from django.contrib.admin.options import TabularInline
from import_export.admin import ExportActionMixin
# from .models import RazorpayPayment

from ghar import models

# Register your models here.


def make_deactive(self, request, queryset):
    queryset.update(status=0)


def make_active(self, request, queryset):
    queryset.update(status=1)


make_deactive.short_description = "Deactivate Selected Item"
make_active.short_description = "activate Selected Item"


class PortAdmin(admin.ModelAdmin):
    search_fields = ['city_name', 'port_type']
    list_display = ['city_name', 'port_type', 'pet_allowed',
                    'vehicle_allowed', 'created_by', 'created_on', 'status']
    list_filter = ['city_name', 'port_type', 'pet_allowed', 'vehicle_allowed']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()


class ValueAddedServiceAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name', 'type', 'created_by', 'created_on', 'status']
    list_filter = ['name', 'type', 'created_by', 'created_on', 'status']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class BoatOwnerAdmin(admin.ModelAdmin):
    search_fields = ['company_name', 'owner_name']
    list_display = ['company_name', 'owner_name', 'created_by', 'created_on', 'status']
    list_filter = ['company_name', 'owner_name', 'created_by', 'created_on', 'status']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class BoatAdmin(admin.ModelAdmin):
    search_fields = ['name', 'number']
    list_display = ['name', 'boat_owner', 'created_by', 'created_on', 'status']
    list_filter = ['pax_capacity', 'vehicle_capacity', 
    'pet_capacity', 'boat_category', 'boat_type', 'lower_deck_fare', 
    'upper_deck_fare', 'created_by', 'created_on', 'status']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class TripAdmin(admin.ModelAdmin):
    search_fields = ['route', 'boat', 'departure_date_time']
    list_display = ['__str__', 'created_by', 'created_on', 'status', ]
    list_filter = ['departure_date', 'departure_time', 'created_by', 'created_on', 'status']
    actions = [make_active, make_deactive]

class RouteAdmin(admin.ModelAdmin):
    search_fields = ['source', 'destination']
    list_display = ['__str__', 'source', 'destination', 'duration', 'created_by', 'created_on', 'status']
    list_filter = ['duration', 'created_by', 'created_on', 'status']
    actions = [make_active, make_deactive]

class ParcelAdmin(admin.ModelAdmin):
    search_fields = ['type', 'weight', 'price']
    list_display = ['type', 'weight', 'price', 'created_by', 'created_on', 'status' ]
    list_filter = ['type', 'weight', 'price', 'created_by', 'created_on', 'status']
    actions = [make_active, make_deactive]

class PetAdmin(admin.ModelAdmin):
    search_fields = ['type', 'weight', 'price']
    list_display = ['type', 'weight', 'price', 'created_by', 'created_on', 'status' ]
    list_filter = ['type', 'weight', 'price', 'created_by', 'created_on', 'status']
    actions = [make_active, make_deactive]

class VehicleAdmin(admin.ModelAdmin):
    search_fields = ['type', 'model', 'price']
    list_display = ['type', 'model', 'price', 'created_by', 'created_on', 'status' ]
    list_filter = ['type', 'model', 'price', 'created_by', 'created_on', 'status']
    actions = [make_active, make_deactive]

class ParcelInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.ParcelInfo
        can_delete = False
        readonly_fields = ['type', 'weight', 'quantity', 'price', 'created_by', 'created_on', 'status']

class ParcelBookingAdmin(admin.ModelAdmin):
    inlines = (ParcelInfoAdminInline,)
    readonly_fields = ['route','tracking_id', 'gst_number', 'discount_percentage', 'discount_amount', 
    'sender_name', 'sender_email', 'sender_mobile', 'receiver_name', 'receiver_email', 
    'receiver_mobile', 'amount_payable', 'payment_success', 'bank_transection_id',
    'created_by', 'created_on', 'status']
    search_fields = ['route','tracking_id', 'sender_name', 'sender_email', 'sender_mobile', 'receiver_name', 'receiver_email', 'receiver_mobile', 'amount_payable', 'created_by', 'created_on', 'status']
    list_display = ['route', 'tracking_id', 'created_by', 'created_on', 'status']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class PassAdmin(admin.ModelAdmin):
    search_fields = ['day', 'trip', 'price']
    list_display = ['__str__', 'day', 'trip', 'price', 'created_by', 'created_on', 'status' ]
    list_filter = ['day', 'trip', 'price', 'created_by', 'created_on', 'status']
    actions = [make_active, make_deactive]

class PassCustomerInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.PassCustomerInfo
        can_delete = False
        readonly_fields = ['name', 'email', 'mobile', 'created_by', 'created_on', 'status']

class PassVehicleInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.PassVehicleInfo
        can_delete = False
        readonly_fields = ['model', 'type', 'registration_number', 'price', 'created_by', 'created_on', 'status']

class PassPetInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.PassPetInfo
        can_delete = False
        readonly_fields = ['name', 'type', 'weight', 'price', 'created_by', 'created_on', 'status']

class PassBookingAdmin(admin.ModelAdmin):
    inlines = (PassCustomerInfoAdminInline, PassVehicleInfoAdminInline, PassPetInfoAdminInline,)
    readonly_fields = ['route','pass_number', 'pax_count', 'vehicle_count', 'pet_count', 
        'coupon_code', 'total_fare', 'trips_allowed', 'validity_days', 'pass_start_timestamp', 
        'pass_expiry_timestamp', 'tax', 'gst_number', 'discount_percentage', 'discount_amount', 'payable_amount', 
        'bank_transection_id', 'payment_success', 'created_by', 'created_on', 'status']
    search_fields = ['route','pass_number', 'created_by', 'created_on', 'status']
    list_display = ['route','pass_number', 'created_by', 'created_on', 'status']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class BoatCustomerInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.BoatCustomerInfo
        can_delete = False
        readonly_fields = ['name', 'email', 'mobile', 'created_by', 'created_on', 'status']

class BoatVehicleInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.BoatVehicleInfo
        can_delete = False
        readonly_fields = ['model', 'type', 'registration_number', 'price', 'created_by', 'created_on', 'status']

class BoatPetInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.BoatPetInfo
        can_delete = False
        readonly_fields = ['name', 'type', 'weight', 'price', 'created_by', 'created_on', 'status']

class BoatVASInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.BoatVASInfo
        can_delete = False
        readonly_fields = ['name', 'type', 'tax', 'price', 'created_by', 'created_on', 'status']

class BoatBookingAdmin(admin.ModelAdmin):
    inlines = (BoatCustomerInfoAdminInline, BoatVehicleInfoAdminInline, 
    BoatPetInfoAdminInline, BoatVASInfoAdminInline,)
    readonly_fields = ['trip', 'pnr', 'booking_duration', 'booking_start_timestamp', 
        'booking_end_timestamp', 'pax_count', 'vehicle_count', 'pet_count', 'vas_count', 
        'coupon_code', 'total_fare', 'tax', 'cess', 'port_levy', 'gst_number', 
        'discount_percentage', 'discount_amount', 'payable_amount', 'bank_transection_id', 
        'payment_success', 'created_by', 'created_on', 'status']
    search_fields = ['trip','pnr', 'created_by', 'created_on', 'status']
    list_display = ['trip','pnr', 'created_by', 'created_on', 'status']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class TicketCustomerInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.TicketCustomerInfo
        can_delete = False
        readonly_fields = ['name', 'email', 'mobile', 'created_by', 'created_on', 'status']

class TicketVehicleInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.TicketVehicleInfo
        can_delete = False
        readonly_fields = ['model', 'type', 'registration_number', 'price', 'created_by', 'created_on', 'status']

class TicketPetInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.TicketPetInfo
        can_delete = False
        readonly_fields = ['name', 'type', 'weight', 'price', 'created_by', 'created_on', 'status']

class TicketVASInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.TicketVASInfo
        can_delete = False
        readonly_fields = ['name', 'type', 'tax', 'price', 'created_by', 'created_on', 'status']

class TicketTripInfoAdminInline(admin.StackedInline):
        extra = 0
        model = models.TicketTripInfo
        can_delete = False
        readonly_fields = ['trip', 'created_by', 'created_on', 'status']

class TicketBookingAdmin(admin.ModelAdmin):
    inlines = (TicketTripInfoAdminInline, TicketCustomerInfoAdminInline, TicketVehicleInfoAdminInline, 
        TicketPetInfoAdminInline, TicketVASInfoAdminInline)
    readonly_fields = ['pnr', 'pax_count', 'vehicle_count', 'pet_count', 'vas_count', 
        'coupon_code', 'pass_number', 'total_fare', 'tax', 'cess', 'port_levy', 'gst_number', 
        'discount_percentage', 'discount_amount', 'payable_amount', 'bank_transection_id', 
        'payment_success', 'created_by', 'created_on', 'status']
    search_fields = ['pnr', 'created_by', 'created_on', 'status']
    list_display = ['pnr', 'created_by', 'created_on', 'status']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class OrderAdmin(admin.ModelAdmin):
    search_fields = ['order_product']
    list_display = ['order_product']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

# class CustomUserAdmin(admin.ModelAdmin):

#     readonly_fields = ['password', 'last_login', 'username', 'first_name', 
#     'last_name', 'email', 'date_joined', 'phone_number', 
#     'is_phone_verified', 'otp']
#     search_fields = ['password', 'last_login', 'username', 'first_name', 
#     'last_name', 'email', 'date_joined', 'phone_number', 
#     'is_phone_verified', 'otp']
#     list_display = ['username', 'first_name', 
#     'last_name', 'email', 'is_phone_verified', 'otp']
#     # actions = [make_deactive, make_active]

# # admin.site.register(models.RazorpayPayment)
# admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Port, PortAdmin)
admin.site.register(models.ValueAddedService, ValueAddedServiceAdmin)
admin.site.register(models.Boat, BoatAdmin)
admin.site.register(models.BoatOwner, BoatOwnerAdmin)
admin.site.register(models.Route, RouteAdmin)
admin.site.register(models.Trip, TripAdmin)
admin.site.register(models.Parcel, ParcelAdmin)
admin.site.register(models.Pet, PetAdmin)
admin.site.register(models.Vehicle, VehicleAdmin)
admin.site.register(models.ParcelBooking, ParcelBookingAdmin)
admin.site.register(models.Pass, PassAdmin)
admin.site.register(models.PassBooking, PassBookingAdmin)
admin.site.register(models.BoatBooking, BoatBookingAdmin)
admin.site.register(models.TicketBooking, TicketBookingAdmin)