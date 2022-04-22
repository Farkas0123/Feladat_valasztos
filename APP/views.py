from django.shortcuts import redirect
from django.shortcuts import render
from .models import Diak, Feladat

felhasz = ""
def index(request):
    template = "login.html"
    context = {}
    if request.method == "POST":
        dnev = request.POST['nev']
        djelszo = request.POST['jelszo']
        d = Diak.objects.filter(nev = dnev).first()
        if d != None and d.jelszo == djelszo:
            global felhasz
            felhasz = dnev
            return valasztas(request)
        else:
            context={'hiba':"Hibás felhasználó név vagy jelszó!"}
    return render(request, template, context)

def valasztas(request):
    template = "valasztas.html"
    for diak in list(Feladat.objects.all()):
        if diak.kie == "-":
            diak.kiesz = "Ez a feladat még szabad."
        else:
            diak.kiesz = "Ez a feladat már foglalt"
    
    
    if request.method == "POST":
        f = Feladat.objects.filter(feladat = "felnev").first()
        if f != None:
            f.kie = felhasz
        
    context = {'feladatok' : Feladat.objects.all}
            
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

            if Diak.objects.filter(nev=akt[0]).first() == None:
                Diak.objects.create(nev=akt[0],jelszo=akt[1])
    
    return render(request,template,{})