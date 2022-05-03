from multiprocessing import context
from django.shortcuts import render
from .models import Feladat
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
        if diak.kie == None:
            diak.kiesz="Ez a feladat még szabad."
            diak.save()
        else:
            diak.kiesz="Ez a feladat már foglalt"
            if diak.kie == request.user.username:
                diak.egyezzik = True
            diak.save()  
    context = {'feladatok' : Feladat.objects.all()}    
    
    if request.method == "POST":
        print(request.POST['le'])
        if request.POST['le'] == "le":
            Feladat.objects.filter(feladat = request.POST['felnev']).update(kie=None)
        else:
            Feladat.objects.filter(feladat = request.POST['felnev']).update(kie=request.user.username) 
            
        for diak in list(Feladat.objects.all()):
            if diak.kie == None:
                diak.kiesz="Ez a feladat még szabad."
                diak.save()
            else:
                diak.kiesz="Ez a feladat már foglalt."
                diak.save()
        
        joe = bool(Feladat.objects.filter(feladat = request.POST['felnev']).first().kie == request.user.username)
        print(joe)
        context = {'feladatok' : Feladat.objects.all(), 'kie': joe}    
        
    return render(request,template,context)

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

