from django.urls import path
from . views import home, singup, tasks, singout, singin, create_task, task_detail, complete_task, delete_task, tasks_complete

urlpatterns = [
    path('', home, name='home'),
    path('singup/', singup, name='singup'),
    path('tasks/', tasks, name='tasks'),
    path('tasks_complete', tasks_complete, name='tasks_complete'),
    path('logout/', singout, name='logout'),
    path('login/', singin, name='login'),
    path('create_task/', create_task, name='create_task'),
    path('task_detail/<int:task_id>', task_detail, name='task_detail'),
    path('task_detail/<int:task_id>/complete', complete_task, name='complete_task'),
    path('task_detail/<int:task_id>/delete', delete_task, name='delete_task'),



]