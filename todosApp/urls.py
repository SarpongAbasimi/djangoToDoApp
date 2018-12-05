from django.urls import path
from .import views


urlpatterns = [
    path('',views.FormsView.as_view()),
    path('list/',views.AllToDosList.as_view(),name='todo_list')
]