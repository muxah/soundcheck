from django.db import models
from django.utils.translation import ugettext as _
from soundcheck.addresses.models import Address


class Base(models.Model):
    name = models.CharField(_('name'), max_length=100, unique=True)
    address = models.ForeignKey(Address)
    
    
    class Meta:
        ordering = ('name', )
        verbose_name = _('base')
        verbose_name_plural = _('bases')
        
    def __unicode__(self):
        return self.name


