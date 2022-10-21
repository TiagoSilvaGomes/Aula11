from django.shortcuts import render
from viagens.forms import ViagemForms
from django import forms


def index(request):
    form= ViagemForms()
    contexto= {'form': form}
    return render(request, 'index.html', contexto)

def revConsulta(request):
    if request.method =='POST':
        form = ViagemForms(request.POST)
        contexto={'form': form}
        return render(request, 'consulta.html', contexto)

def revConsulta(request):
    if request.method == 'POST':
        form = ViagemForms(request.POST)
        if form.is_valid():
            contexto={'forms': form}
            return render(request, 'consulta.html', contexto)

        else:
            print('Form Inválido')
            contexto = {'form': form}
            return render(request, 'index.html', contexto)

# Create your views here.
