from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def hello_word(request):
    return render(request, 'singup.html', {
        'form': UserCreationForm
    })