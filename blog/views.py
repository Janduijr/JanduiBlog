from django.shortcuts import render
from .models import Eu, jogadores, times
# Create your views here.
def index(request):
    jogador = jogadores.objects.all()
    time = times.objects.all()
    contexto = {
        'jogadores' : jogador,
        'times' : time
    }
    
    return render(request, 'blog/index.html', contexto)

def jogador(request, jogadores_id):
    detalhe = jogadores.objects.get(id=jogadores_id)
    contexto = {
        'detalhe' : detalhe
    }
    
    return render(request, 'blog/jogador.html', contexto)

def time(request, time_id):
    detalhe2 = times.objects.get(id=time_id)
    contexto = {
        'detalhe2' : detalhe2,
    }
    
    return render(request, 'blog/time.html', contexto)