# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import ContactForms


# Create your views here.
def home(request):
    if request.method == "POST":
        form = ContactForms(request.POST)

        if form.is_valid():
            pass

    else:
        form = ContactForms()

    return render(request, "home.html", {"form": form})
