from django.shortcuts import render

def inicio (request):
    data = {}
    return render (request, 'inicio.html', data)
