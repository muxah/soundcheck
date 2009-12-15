from django.contrib import admin
from soundcheck.rates import models
from django.utils.translation import ugettext as _



class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)

    fieldsets = (
        ( None, {'fields': ('name',),}, ),
    )


admin.site.register(models.Currency, CurrencyAdmin)


class RateAdmin(admin.ModelAdmin):
    list_display = ('price_per_hour', 'currency', 'day_of_the_week', 'from_time', 'till_time', 'base',)

    fieldsets = (
        ( None, {'fields': ('price_per_hour', 'currency', 'day_of_the_week', 'from_time', 'till_time', 'base',),}, ),
    )


admin.site.register(models.Rate, RateAdmin)



class RateInline(admin.TabularInline):
    model = models.Rate
    extra = 1