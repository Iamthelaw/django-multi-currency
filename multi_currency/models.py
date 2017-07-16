# encoding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _


@python_2_unicode_compatible
class Currency(models.Model):
    code = models.CharField(
        _('Currency code'), max_length=3, unique=True,
        help_text=_('For example: USD, EUR, RUB'))
    rate = models.FloatField(
        _('Currency rate'), default=0)
    last_modified = models.DateTimeField(
        _('Last modified'), auto_now=True, editable=False)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('code', 'last_modified')
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')
