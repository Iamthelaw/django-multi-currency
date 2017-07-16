# encoding: utf-8
"""
About
-----

This command is designed for use on regular busis with shedule management
like **cron**.

Basicly it goes to Bank open api, parse rates (defined in settings) and
stores result in database.

Command takes no external arguments.

Usage
-----

Run this command in shell to update currencies

.. code-block:: bash

    $ django-admin update_currency_rates

Helper functions
----------------
"""
from datetime import date
from contextlib import closing
from six import PY3
from xml.etree.ElementTree import ElementTree

from django.core.management.base import BaseCommand

from multi_currency.models import Currency
from multi_currency.helpers import get_settings

API_URL = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
TODAY = date.today().strftime('%d/%m/%Y')

CURRENCIES = get_settings()['currencies']


def fix_float_repr(tag):
    """
    Replaces "," with "." so we can convert value to float.
    
    :param tag: xml tag that contains rate as string
    :type tag: :class:`xml.etree.ElementTree.Element`

    :returns str: Fixed string
    """
    value = tag.text
    if ',' in value:
        value = value.replace(',', '.')
    return value


def get_rates(command):
    """Main function that make call to external xml api.
    
    :param command: instance of current command
    :type command: :class:`django.core.management.base.BaseCommand`

    Parser makes 3 steps:

    1. Gets response from bank open api with :class:`urllib` from standart
       library
    2. Uses :class:`xml.etree.ElementTree` to parse this xml response.
    3. Stores result in :class:`multi_currency.models.Currency`
    """
    if PY3:
        from urllib.request import urlopen
    else:
        from urllib import urlopen

    with closing(urlopen(API_URL + TODAY)) as f:
        tree = ElementTree()
        tree.parse(f)
        items = tree.findall('Valute')
        for item in items:
            currency_code = item.find('CharCode').text
            currency_rate = fix_float_repr(item.find('Value'))
            if currency_code in CURRENCIES:
                currency, _ = Currency.objects.get_or_create(
                    code=currency_code)
                currency.rate = currency_rate
                currency.save()
                command.stdout.write(
                    '{}: {}'.format(currency_code, currency_rate))


class Command(BaseCommand):
    """Actual Django management command class."""
    help = 'Get currency rates from bank api'

    def handle(self, *args, **options):
        get_rates(self)
        self.stdout.write('Successfully updated currencies')
