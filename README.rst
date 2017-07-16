Full Documentation: http://django-multi-currency.readthedocs.io/en/latest/

Quickstart
==========

Installation
------------

Install it with pip **`pip install django_multi_currency`**

Set up project
--------------
Then you need to update some of your project settings.

1. Add **'multi_currency',** to **INSTALLED_APPS**
2. Add **'multi_currency.context_processors.currency',** to template
   context processors
3. (Optional) Overwrite this module settings adding **MULTI_CURRENCY**
   dict to your local settigns

Example Settings
----------------

.. code-block:: python

    INSTALLED_APPS = {
        # ...
        'multi_currency',
        # ...
    }

    TEMPLATES = [
        {
            # ...
            'OPTIONS': {
                'context_processors': [
                    # ...
                    'multi_currency.context_processors.currency'
                ]
            }
        }
    ]

    MULTI_CURRENCY = {
        'percent_to_add': 3
    }

Usage
-----

1. Place **{% load multi_currency_tags %}** in some base template to render currency switch.
2. Use **{% local_currency object.price %}** tag to convert value approprietly for the user

Development
===========

Run server with `$ django-admin runserver`

Bump version
------------

1. Test version change with `$ bumpversion --dry-run [patch, minor, major] --verbose`
2. Bump version with `$ bumpversion [patch, minor, major]`

Update metadata and publish to PyPi
-----------------------------------
If you have not registered package in PyPi, run `$ python setup.py register`.

Then use this command to create a source distribution `$ python setup.py sdist`.
Lastly, upload to PyPi server `$ python setup.py upload`
