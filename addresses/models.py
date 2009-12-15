from django.db import models
from django.utils.translation import ugettext as _


class Dict(models.Model):
    name = models.CharField(_('name'), max_length=100, unique=True)

    class Meta:
        abstract = True
        ordering = ('name', )

    def __unicode__(self):
        return self.name


class Country(Dict):

    class Meta:
        ordering = ('name', )
        verbose_name = _('country')
        verbose_name_plural = _('countries')


class State(Dict):
    country = models.ForeignKey(Country)

    class Meta:
        unique_together = ('name', 'country')
        ordering = ('name', )
        verbose_name = _('state')
        verbose_name_plural = _('states')


class City(Dict):
    state = models.ForeignKey(State)

    class Meta:
        unique_together = ('name', 'state')
        ordering = ('name', )
        verbose_name = _('city')
        verbose_name_plural = _('cities')


class Street(Dict):
    city = models.ForeignKey(City)

    class Meta:
        unique_together = ('name', 'city')
        ordering = ('name', )
        verbose_name = _('street')
        verbose_name_plural = _('streets')


class Address(models.Model):
    street = models.ForeignKey(Street)
    building = models.CharField(_('building'), max_length=10)
    room = models.CharField(_('room'), max_length=10, blank=True,)

    class Meta:
        unique_together = ('street', 'building', 'room',)
        ordering = ('street', )
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __unicode__(self):
        return '%s, %s' % (self.building, self.street)
