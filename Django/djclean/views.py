from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,"pages/inicio.html",{})


def portafolio(request):
    return render(request,"pages/portafolio.html",{})