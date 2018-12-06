from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from todosApp.models import ToDo

# Create your views here.
def index(request):
    template='todosApp/view.html'
    context= {
    'todolist':ToDo.objects.all(),
     'length':len(ToDo.objects.all())
    }
    return render(request,template,context)

def todo(request):
    if request.method == 'POST':
        getUserInput=ToDo.objects.create(description=request.POST['toDos'])
        getUserInput.save()
        return HttpResponseRedirect("/")
        

def deleteToDo(request,todoID):
        if request.method=='POST':
                delDoto=ToDo.objects.get(id=todoID).delete()
                return HttpResponseRedirect("/")
