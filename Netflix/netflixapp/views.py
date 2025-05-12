from django.shortcuts import render, redirect
from .models import Movies

def homepage(request):
    Movieslists = Movies.objects.all()
    return render(request, "home.html", {'Movieslists': Movieslists})
