from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    return render(request, 'home.html')


def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'singup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinsiden'
            })

def tasks(request):
    return render(request, 'tasks.html')

def singout(request):
    logout(request)
    return redirect('home')

def singin(request):
    if request.method == 'get':
        return render(request, 'singin.html',{
            'form': AuthenticationForm
        })
    else:
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], 
            password=request.POST['password'])
        
        if user is None:
            return render(request, 'singin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o Clave incarrecta'
        })
        else:
            login(request, user)
            return redirect('tasks')