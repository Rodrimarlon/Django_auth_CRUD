from django.urls import path
from . views import home, singup, tasks

urlpatterns = [
    path('', home, name='home'),
    path('singup/', singup, name='singup'),
    path('tasks/', tasks, name='tasks')
]