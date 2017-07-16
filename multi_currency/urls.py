# encoding: utf-8
from __future__ import absolute_import

from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^currency/(?P<currency_code>\w{3})/$',
        views.select_currency, name='select_currency'),
]
