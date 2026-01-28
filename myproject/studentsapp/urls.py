from django.urls import path
from studentsapp.views import std, about

urlpatterns = [
    path('', std, name='std'),
    path('about/', about, name='about'),
]