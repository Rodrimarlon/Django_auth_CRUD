from django.urls import path
from .views import hello_word

urlpatterns = [
    path('', hello_word, name='tasks'),
    path('singup/', hello_word)
]