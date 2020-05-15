from django.urls import path
from icecreamapp.views import *
from icecreamapp.models import *

app_name = "icecreamapp"

urlpatterns = [
    path('', variety_list , name='varieties'),

]
