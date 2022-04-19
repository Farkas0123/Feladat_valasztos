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
            return redirect('/valasztas/')
        else:
            context={'hiba':"Hibás felhasználó név vagy jelszó!"}
    return render(request, template, context)

def valasztas(request):
    template = "valasztas.html"
    i = 0
    while i < len(list(Feladat.objects.all())):
        if list(Feladat.objects.all())[i].kie == "-":
            list(Feladat.objects.all())[i].kiesz = "Ez a feladat még szabad."
        else:
            list(Feladat.objects.all())[i].kiesz = "Ez a feladat már foglalt"
        i += 1
    
    context = {'feladatok' : Feladat.objects.all}
            
    print(list(Feladat.objects.all())[0].kiesz)
    
    if request.method == "POST":
        f = Feladat.objects.filter(feladat = "felnev").first()
        if f != None:
            f.kie = felhasz
        
            
    return render(request,template,context)

def regisztracio(request):
    template = "diak_regisztracio.html"
    if request.method == "POST":
        tabla = request.POST['adatok'].split("\t")
        for diak in tabla:
            akt = diak.split(",")
            print(akt[0] == "")
            print(akt[1] != None)
            print(akt)
            if akt[0] == "" or akt[1] == None:
                return render(request, template, {'hiba': "Az egyik adat hibás!"})
            # print(akt[0]+akt[1])
            
            if Diak.objects.filter(nev=akt[0]).first() == None:
                print("itt vok")
                Diak.objects.create(nev=akt[0],jelszo=akt[1])
    
    return render(request,template,{})