# encoding: utf-8
from django.conf import settings

from .models import Currency

from .helpers import get_settings
from .helpers import get_currency_code_from_request

from .settings import DEFAULT_CURRENCY 


def currency(request):
    """Populates context with currency code and rate."""

    is_favicon = 'favicon' in request.path
    is_static = request.path.startswith(settings.STATIC_URL)
    is_media = request.path.startswith(settings.MEDIA_URL)

    dev_urls = (is_favicon, is_static, is_media)

    selected_currency = DEFAULT_CURRENCY

    if not any(dev_urls):
        prev_currency_code = request.session.get(
            'selected_currency', DEFAULT_CURRENCY)
        selected_currency = get_currency_code_from_request(
            request.LANGUAGE_CODE, prev_currency_code)
        request.session['selected_currency'] = selected_currency

    currency, _ = Currency.objects.get_or_create(
        code=selected_currency)

    return {
        'currency_code': currency.code,
        'currency_rate': currency.rate,
    }

