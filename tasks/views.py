from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')


def singup(request):
    if request.method == 'get':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.post['password1'] == request.post['password2']:
            try:
                user = User.objects.create_user(username=request.post['username'], password=request.post['password2'])
                user.save()
                return HttpResponse('Usuario Creado Sastifactoriamente')
            except:
                return HttpResponse('El usuario ya existe')
        else:
            return HttpResponse('Las contraseñas no coinsiden')


