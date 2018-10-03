# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from .models import Futures
import json


# Create your views here.
def index(request):
    table = Futures.objects.all()
    date = []
    price_close = []
    price_open = []
    for row in table:
        date += [row.date.isoformat()]
        price_close += [row.close]
        price_open += [row.open]

    return render_to_response('index.html', locals())
