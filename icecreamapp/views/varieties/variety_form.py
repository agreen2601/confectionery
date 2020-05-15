import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from icecreamapp.models import Variety, model_factory
from ..connection import Connection
from .variety_detail import get_variety

def variety_form(request):
    if request.method == 'GET':
        template = 'varieties/variety_form.html'

        return render(request, template)

def variety_edit_form(request, variety_id):

    if request.method == 'GET':
        variety = get_variety(variety_id)
        template = 'varieties/variety_form.html'
        context = {
            'variety': variety
        }
    
    return render(request, template, context)