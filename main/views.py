from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'Title':'Главная страница сайта','tasks':tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была не верной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)