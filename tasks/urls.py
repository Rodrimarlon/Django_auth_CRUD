from django.urls import path
from . views import home, singup

urlpatterns = [
    path('', home, name='home'),
    path('singup/', singup, name='singup')
]