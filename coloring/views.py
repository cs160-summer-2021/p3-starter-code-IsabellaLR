from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def social(request):
    return render(request, 'coloring/social.html')

def competitions(request):
    return render(request, 'coloring/competitions.html')

def library(request):
    return render(request, 'coloring/library.html')

def personal(request):
    return render(request, 'coloring/personal.html')