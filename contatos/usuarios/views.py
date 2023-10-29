from django.shortcuts import render
from templates import *
from usuarios.models import usuario
from usuarios.forms import *
# Create your views here.

def home(request):
    form = cadastroForm()
    return render(request, 'index.html', {'form': form})
