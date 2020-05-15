import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from icecreamapp.models import Variety, model_factory
from ..connection import Connection


def variety_form(request):
    if request.method == 'GET':
        template = 'varieties/variety_form.html'

        return render(request, template)
