from django.contrib import admin
from soundcheck.bases import models
from soundcheck.rates.admin import RateInline
from django.utils.translation import ugettext as _



class BaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)

    fieldsets = (
        ( None, {'fields': ('name', 'address',),}, ),
    )

    inlines = [
        RateInline,
    ]


admin.site.register(models.Base, BaseAdmin)


