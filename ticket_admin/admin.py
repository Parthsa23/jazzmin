from django.contrib import admin
from django.contrib.admin.options import TabularInline
from import_export.admin import ImportExportModelAdmin
# from .models import RazorpayPayment

from ticket_admin import models

# Register your models here.


def make_deactive(self, request, queryset):
    queryset.update(status=0)


def make_active(self, request, queryset):
    queryset.update(status=1)


make_deactive.short_description = "Deactivate Selected Item"
make_active.short_description = "activate Selected Item"

class PortAdmin(admin.ModelAdmin):
    search_fields = ['city_name', 'port_type', 'contact_name']
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

class BoatTypeAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name', 'created_by', 'created_on', 'status']
    list_filter = ['name', 'created_by', 'created_on', 'status']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class BoatCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name', 'created_by', 'created_on', 'status']
    list_filter = ['name', 'created_by', 'created_on', 'status']
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
    'pet_capacity', 'boat_category', 'boat_type', 'lower_deck_seat', 
    'upper_deck_seat', 'created_by', 'created_on', 'status']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class TripAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['route', 'boat', 'departure_date_time']
    list_display = ['__str__', 'created_by', 'created_on', 'status', ]
    list_filter = ['departure_date', 'departure_time', 'created_by', 'created_on', 'status']
    readonly_fields = ['seat_booked_lower', 'seat_booked_upper', 'pet_booked', 'vehicle_booked']
    actions = [make_active, make_deactive]

    def save_model(self, request, obj, form, change):
        # obj.seat_available_lower = form.boat.lower_deck_seat
        # obj.seat_available_upper = form.boat.upper_deck_seat
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class RouteTypeAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name', 'created_by', 'created_on', 'status']
    list_filter = ['name', 'created_by', 'created_on', 'status']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

class RouteAdmin(admin.ModelAdmin):
    search_fields = ['source', 'destination']
    list_display = ['__str__', 'source', 'destination', 'duration', 'created_by', 'created_on', 'status']
    list_filter = ['duration', 'created_by', 'created_on', 'status']
    actions = [make_active, make_deactive]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

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
    jazzmin_logo = "jazzmin/static/info-solid.svg"

class PassAdmin(admin.ModelAdmin):
    search_fields = ['day', 'trip', 'price']
    list_display = ['__str__', 'day', 'trip', 'price', 'created_by', 'created_on', 'status' ]
    list_filter = ['day', 'trip', 'price', 'created_by', 'created_on', 'status']
    actions = [make_active, make_deactive]

class OrderAdmin(admin.ModelAdmin):
    search_fields = ['order_product']
    list_display = ['order_product']
    actions = [make_deactive, make_active]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        # obj.modifier = request.user
        obj.save()

admin.site.register(models.Order, OrderAdmin)
# admin.site.register(models.BoatCategory, BoatCategoryAdmin)
# admin.site.register(models.BoatType, BoatTypeAdmin)
admin.site.register(models.Port, PortAdmin)
admin.site.register(models.ValueAddedService, ValueAddedServiceAdmin)
# admin.site.register(models.Boat, BoatAdmin)
# admin.site.register(models.BoatOwner, BoatOwnerAdmin)
admin.site.register(models.Route, RouteAdmin)
admin.site.register(models.RouteType, RouteTypeAdmin)
admin.site.register(models.Trip, TripAdmin)
admin.site.register(models.Parcel, ParcelAdmin)
admin.site.register(models.Pet, PetAdmin)
admin.site.register(models.Vehicle, VehicleAdmin)
admin.site.register(models.Pass, PassAdmin)