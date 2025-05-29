
from django.shortcuts import render



def index(request):

    dados = {
    1: {"nome" : "Nebulosa de Andromeda!", "legenda": "poder furioso do Shun"},
    2: {"nome" : "Galaxia distante","legenda": "tchan tchammmm tchan tchan tchan tchaannnn tchan!"}
    }
    
    return render(request, 'galeria/index.html',{"cards":dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
