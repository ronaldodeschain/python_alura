
from django.shortcuts import render,get_object_or_404
from galeria.models import Fotografia



def index(request):
    #exibe fotos na página index - Order by permite selecionar qual parametro
    #vai servir de indice para ordenação. Se colocar o - antes do texto
    # a ordem se torna inversa
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html',{"cards":fotografias})

def imagem(request,foto_id):
    fotografia = get_object_or_404(Fotografia,pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia":fotografia})
