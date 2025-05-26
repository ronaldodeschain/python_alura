from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1> Alura Teste</h1><p>Mais um texto aqui para teste</p>')



