from django.contrib import admin
from soundcheck.addresses import models
from django.utils.translation import ugettext as _


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    fieldsets = (
        ( None, {'fields': ('name',),}, ),
    )


admin.site.register(models.Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)

    fieldsets = (
        ( None, {'fields': ('name', 'country',),}, ),
    )


admin.site.register(models.State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name','state', )

    fieldsets = (
        ( None, {'fields': ('name','state', ),}, ),
    )


admin.site.register(models.City, CityAdmin)


class StreetAdmin(admin.ModelAdmin):
    list_display = ('name','city', )

    fieldsets = (
        ( None, {'fields': ('name','city', ),}, ),
    )


admin.site.register(models.Street, StreetAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('street','building', 'room',)

    fieldsets = (
        ( None, {'fields': ('street','building', 'room', ),}, ),
    )


admin.site.register(models.Address, AddressAdmin)