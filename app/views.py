# site/views.py
from django.shortcuts import render

def home(request):
    return render(request, "app/home.html")

def coach(request):
    return render(request, "app/coach.html")
