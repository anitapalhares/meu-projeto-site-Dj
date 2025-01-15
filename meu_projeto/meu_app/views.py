from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Bem-vindo ao Django!</h1>")


def home(request):
    return render(request, 'meu_app/home.html')
