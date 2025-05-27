from django.urls import path
from galeria.views import index,imagem

urlpatterns = [
    path('index/',index,name='index'),
    path('imagem/',imagem, name='imagem')
]