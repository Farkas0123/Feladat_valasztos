from django.shortcuts import render

def index(request):
    template = "valasztas.html"
    return render(request, template, {})