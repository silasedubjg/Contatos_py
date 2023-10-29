from django.shortcuts import render
from templates import *
# Create your views here.

def home(request):
    return render(request, 'index.html')
