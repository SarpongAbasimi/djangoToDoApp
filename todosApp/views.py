from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from todosApp.models import ToDo

# Create your views here.
def index(request):
    template='todosApp/view.html'
    context= {
    'todolist':ToDo.objects.all()
    }
    return render(request,template,context)

def todo(request):
    if request.method == 'POST':
        template='todosApp/todo.html'
        getUserInput=ToDo.objects.create(description=request.POST['toDos'])
        getUserInput.save()
        return HttpResponseRedirect("/")
        

