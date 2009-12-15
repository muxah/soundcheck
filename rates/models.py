from django.db import models
from django.utils.translation import ugettext as _
from soundcheck.bases.models import Base



class Currency(models.Model):
    name = models.CharField(_('name'), max_length=3)

    class Meta:
        ordering = ('name', )
        verbose_name = _('currency')
        verbose_name_plural = _('currencies')

    def __unicode__(self):
        return self.name


class Rate(models.Model):
    w = {
         1: _('Monday'),
         2: _('Tuesday'),
         3: _('Wednesday'),
         4: _('Thursday'),
         5: _('Friday'),
         6: _('Saturday'),
         7: _('Sunday'),
        }
    DAYS = (
            (w[1], _('on %ss' % w[1])),
            (w[2], _('on %ss' % w[2])),
            (w[3], _('on %ss' % w[3])),
            (w[4], _('on %ss' % w[4])),
            (w[5], _('on %ss' % w[5])),
            (w[6], _('on %ss' % w[6])),
            (w[7], _('on %ss' % w[7])),
            (' '.join( [w[i] for i in range (1, 6)] ), _('from %s till %s' % (w[1], w[5]) )),
            ('%s %s' % (w[6], w[7]), _('on %ss and %ss' % (w[6], w[7]) )),
            ('%s %s %s' % (w[1], w[3], w[5]), _('on %ss, %ss and %ss' % (w[1], w[3], w[5]) )),
            ('%s %s' % (w[2], w[4]), _('on %ss and %ss' % (w[2], w[4]))),
            (' '.join( [w[i] for i in range (1, 8)] ), _('any day')),
    )

    price_per_hour = models.PositiveIntegerField(_('price per hour'))
    from_time = models.TimeField(_('from time'))
    till_time = models.TimeField(_('till time'))
    day_of_the_week = models.CharField(
                                        _('day of the week'),
                                        max_length=100,
                                        choices=DAYS,
    )
    currency = models.ForeignKey(Currency)
    base = models.ForeignKey(Base)

    class Meta:
        ordering = ('currency', 'price_per_hour', 'day_of_the_week',)
        verbose_name = _('rate')
        verbose_name_plural = _('rates')

    def __unicode__(self):
        return "%s %s from %s till %s on %s" % (
                                                self.price_per_hour,
                                                self.currency,
                                                self.from_time,
                                                self.till_time,
                                                self.day_of_the_week
                                                )