from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html')

def elenco(request):
    context = {"clubes": Clube.objects.all(), 'jogadores': Jogadores.objects.all()}
    return render (request, 'elenco.html', context)

def sobre(request):
    return render(request, 'sobre.html',)