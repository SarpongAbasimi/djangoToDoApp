from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from todosApp.models import ToDo

# Create your views here.
""" template view just redenders an html template"""
class FormsView(TemplateView):
    template_name='todosApp/formtemplate.html'


""" List View displays all the objects in our database"""
class AllToDosList(ListView):
    model= ToDo
    template_name='todosApp/todo_list.html'
    queryset=ToDo.objects.all()

