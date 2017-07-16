# encoding: utf-8
"""
The settings of this module is pretty straightforward dictionary with some keys and values.

Default values
--------------

.. code-block:: python

    MULTI_CURRENCY = {
        'base': 'RUB',
        'currencies': ['USD', 'EUR'],
        'precent_to_add': 0
    }

Available params
----------------

:param base str: Base currency code, will be used for default language
:param currencies list: List of currencies to be parsed by management command
    and first currency in the list will be used as default currency when user
    switches language to non-default
:param percent_to_add int: Add extra value to total value (in percent)

Overwriting
-----------

To overwrite settings put **MULTI_CURRENCY** dictionary in your local settings and
overwrite any key.

E.g. you don't need to copy paste all settings:

.. code-block:: python

    MULTI_CURRENCY = {
        'percent_to_add': 3,
    }
"""

DEFAULT_CURRENCY = 'RUB'
DEFAULT_SETTINGS = {
    'base': DEFAULT_CURRENCY,
    'currencies': ['USD', 'EUR'],
    'percent_to_add': 0,
}
