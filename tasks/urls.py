from django.urls import path
from . views import home, singup, tasks, singout, singin, create_task

urlpatterns = [
    path('', home, name='home'),
    path('singup/', singup, name='singup'),
    path('tasks/', tasks, name='tasks'),
    path('logout/', singout, name='logout'),
    path('login/', singin, name='login'),
    path('create_task/', create_task, name='create_task'),
]