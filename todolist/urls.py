from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('/login', login_user, name='login'),
    path('/register', register, name="register"),
    path('/create-task', create_task, name="create_task"),
    path('/logout', logout_user, name="logout"),
    path('/delete-task/<task_id>', delete_task, name="delete_task"),
    path('/update-task-status/<task_id>', update_task_status, name="update_task_status"),
    path('/json', show_todolist_json, name="show_todolist_json"),
    path('/ajax', show_todolist_ajax, name='show_todolist_ajax'),
    path('/add', add, name='add'),
    path('/delete/<task_id>', delete, name='add')
]
