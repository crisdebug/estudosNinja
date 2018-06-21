from django.shortcuts import render

# Create your views here.

def logar(request):
    render(request, 'atividades/logou.html')