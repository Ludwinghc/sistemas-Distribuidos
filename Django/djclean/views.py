from django.shortcuts import render, redirect
# importacion de libreria para log in
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def inicio(request):
    return render(request,"pages/inicio.html",{})

@login_required
def resumen(request):
    return render(request,"pages/resume.html",{})

def exit(request):
    logout(request)
    return redirect('inicio')