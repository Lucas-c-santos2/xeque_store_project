from django.shortcuts import render

def home(request):
    return render(request, 'loja/home.html')

def colecoes(request):
    return render(request, 'loja/colecoes.html')

def kits(request):
    return render(request, 'loja/kits.html')

def produtos(request):
    return render(request, 'loja/produtos.html')