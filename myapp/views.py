from django.shortcuts import redirect, render, HttpResponse
from .models import TodoItem
from .forms import *

# Create your views here.

# def home(request):
#     return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def todos(request):
    items = TodoItem.objects.all()
    form = TodoForm()

    if request.method == 'POST':      

        # for updation and deletion
        todo_id = request.POST.get('todo_id')
        if todo_id:
            todo = TodoItem.objects.get(id=todo_id)

            if 'complete' in request.POST:
                todo.completed = True
            elif 'uncomplete' in request.POST:
                todo.completed = False
            elif 'delete' in request.POST:
                todo.delete()
                return redirect("/")
            
            todo.save()
            return redirect('/')
        
        # for insertion
        form = TodoForm(request.POST)  
        if form.is_valid():
            form.save()
        return redirect("/")
    
    return render(request, "todos.html", {"todos": items, 'form': form})


def edit(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    form = TodoForm(instance=todo)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, "edit.html", {"todo": todo, 'form': form})