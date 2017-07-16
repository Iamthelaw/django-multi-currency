# encoding: utf-8
from __future__ import absolute_import

from django.http import HttpResponseRedirect

from .settings import DEFAULT_CURRENCY

def select_currency(request, currency_code):
    request.session['selected_currency'] = (
        currency_code or DEFAULT_CURRENCY)
    next = request.META.get('HTTP_REFERER')

    # We don't need circular redirects
    if not next or next == request.path:
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect(next)
