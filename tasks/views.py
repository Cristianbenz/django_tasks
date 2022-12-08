from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import TaskForm
from .models import Tasks
# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    try:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        user.save()
        login(request, user)
        return redirect('tasks')
    except IntegrityError:
        return render(request, 'signup.html', {
            "error": "User already exists"
        })

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render(request, 'login.html', {
            "error": 'Username or Password is incorrect'
        })
    login(request, user)
    return redirect('tasks')

@login_required
def signout(request):
    logout(request)
    return redirect('index')

@login_required
def render_tasks(request):
    tasks = Tasks.objects.filter(user=request.user)
    return render(request, 'tasks.html', {
        "tasks": tasks
    })

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'createTask.html', {
            "form": TaskForm 
        })
    task = TaskForm(request.POST)
    new_task = task.save(commit=False)
    new_task.user = request.user
    new_task.save()

    return redirect('tasks')