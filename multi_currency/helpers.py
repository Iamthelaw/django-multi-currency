# encoding: utf-8
from django.conf import settings

from .settings import DEFAULT_CURRENCY

SETTINGS_KEYWORD = 'MULTI_CURRENCY'


def get_settings():
    """
    Get settings for current app

    :returns dict: A dict of settings
    """
    from django.conf import settings
    from .settings import DEFAULT_SETTINGS

    try:
        project_settings = getattr(
            settings, SETTINGS_KEYWORD)
    except AttributeError:
        return DEFAULT_SETTINGS
    else:
        for key in DEFAULT_SETTINGS:
            if not project_settings.get(key):
                project_settings.update(
                    {key: DEFAULT_SETTINGS[key]})
        return project_settings


def convert_with_currency(rate, value, extra=0):
    """
    Converts value with relation to currency rate

    :param rate int: currency rate
    :param value str: value to convert
    :param extra int: add extra to value (in percentage)

    :returns str: converted value
    """
    value = float(value)
    converted_value = value / rate if rate else value

    # Add extra % to total price
    percent_to_add = get_settings()['percent_to_add']
    if percent_to_add:
        converted_value += (converted_value / 100) * percent_to_add

    return converted_value


def get_currency_code_from_request(request_language, prev_currency):
    """Custom logic for returning currency code.
    
    Main reason - on non default language there must be
    a posibility to choose between currencies: e.g. USD and EUR.
    With default language however you can'y choose currency.

    Not a bug, a business logic feature.
    """
    default_language = settings.LANGUAGE_CODE

    if request_language == default_language:
        return DEFAULT_CURRENCY

    if prev_currency == DEFAULT_CURRENCY:
        try:
            return get_settings()['currencies'][0]
        except (IndexError, KeyError):
            return DEFAULT_CURRENCY

    return prev_currency

