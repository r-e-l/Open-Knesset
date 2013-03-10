from django.db import models
from django.utils.translation import ugettext_lazy as _


ICON_CHOICES = (
    ('qoute', _('Quote')),
    ('stat', _('Statistic')),
    ('hand', _('Hand')),
)


class Tidbit(models.Model):
    """Entries for 'Did you know ?' section in the index page"""

    title = models.CharField(_('title'), max_length=40,
                             default=_('Did you know ?'))
    icon = models.CharField(_('Icon'), max_length=15, choices=ICON_CHOICES)
    content = models.TextField(_('Content'))
    button_text = models.CharField(_('Button text'), max_length=100)
    button_link = models.CharField(_('Button link'), max_length=255)

    active = models.BooleanField(_('Active'), default=True)
    ordering = models.IntegerField(_('Ordering'), default=20, db_index=True)

    class Meta:
        verbose_name = _('Tidbit')
        verbose_name_plural = _('Tidbits')
