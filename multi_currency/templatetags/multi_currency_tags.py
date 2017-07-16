# encoding: utf-8
"""
There are 2 main tags: for converting integers
and for rendering currency chooser template.

Usage
-----

Like with all django templates tag - add
**{% load multi_currency_tags %}** to desired template

Next to render currency chooser place **{% currency chooser %}**
anywhere in template, preferably in some base template.

To convert integers to selected currency use local_currency
tag like so **{% local_currency object.price %}**.

Members
-------
"""
from decimal import Decimal

from django import template
from django.conf import settings

from multi_currency.helpers import get_settings
from multi_currency.helpers import convert_with_currency

register = template.Library()


@register.simple_tag(takes_context=True)
def local_currency(context, value):
    """
    For non default languages converts value with currency

    :param value: Price value
    :type value: str

    :returns: Formatted and (optionaly) converted value
    :rtype: str
    """
    needs_coversion = (
        context['request'].LANGUAGE_CODE != settings.LANGUAGE_CODE
    )
    if needs_coversion:
        rate = context['currency_rate']
        value = convert_with_currency(rate, value)
    return '{0:.2f}'.format(float(value))


@register.inclusion_tag('multi_currency/currency_chooser.html', takes_context=True)
def currency_chooser(context):
    """Renders currency chooser from template."""

    currencies = get_settings()['currencies']
    return {
        'currencies': [{'code': curr, 'active': False} for curr in currencies],
        'needs_conversion': settings.LANGUAGE_CODE != context['request'].LANGUAGE_CODE
    }

