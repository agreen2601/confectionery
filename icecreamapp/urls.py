from django.urls import path
from icecreamapp.views import *
from icecreamapp.models import *

app_name = "icecreamapp"

urlpatterns = [
    path('', variety_list , name='varieties'),
    path('variety/form', variety_form , name='variety_form'),
    path('varieties/<int:variety_id>/', variety_detail, name="variety"),
    path('varieties/<int:variety_id>/form', variety_edit_form, name='variety_edit_form'),
]
