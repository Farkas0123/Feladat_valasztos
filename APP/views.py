from django.shortcuts import render
from .models import Diak, Feladat
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

@login_required
def index(request):
    template = "registration/login.html"
    return render(request, template, {})

@login_required
def valasztas(request):
    template = "valasztas.html"
    for diak in list(Feladat.objects.all()):
        if diak.kie == "-":
            diak.kiesz = "Ez a feladat még szabad."
        else:
            diak.kiesz = "Ez a feladat már foglalt"
    
    
            
    return render(request,template,{})

def regisztracio(request):
    template = "diak_regisztracio.html"
    if request.method == "POST":
        tabla = request.POST['adatok'].split("\t")
        for diak in tabla:
            akt = diak.split(",")
            try:
                a = str(akt[0])
                b = akt[1]
            except:
                return render(request, template, {'hiba': "Valamelyik adat hibás"})

            if User.objects.filter(nev=akt[0]).first() == None:
                User.objects.create(nev=akt[0],jelszo=akt[1])
    
    return render(request,template,{})

