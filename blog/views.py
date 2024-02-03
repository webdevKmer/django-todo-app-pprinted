from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def home(request):
    todos = Todo.objects.all().order_by('-id')
    form = TodoForm()
    context = {
        'form' : form,
        'todos' : todos,
    }
    return render(request, 'index.html', context)

def add_todo(request):
    form = TodoForm()
    context = {
        'form' : form,
        'todos' : todos,
    }
    if request.method == 'POST':
        print('post')
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'index.html', context)

def todos(request):
    context = {}
    return render(request, 'todos/index.html', context)

def delete_all(request):
    todos_todelete = Todo.objects.all().delete()
    return redirect('home')

def delete_completed(request):
    todos_todelete = Todo.objects.filter(completed__exact=True).delete()
    return redirect('home')