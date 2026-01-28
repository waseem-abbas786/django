from django.urls import path
from studentsapp.views import std

urlpatterns = [
    path('', std, name='std'),
]