from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='index-view'),
    path('todo/',views.todo,name='todo-view'),
    path('deleteToDo/<int:todoID>',views.deleteToDo,name='delete-todo')
]