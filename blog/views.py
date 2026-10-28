from django.shortcuts import render
from django.http import HttpResponse

OWNER = "Mr. Robot"

def index(request):
    return HttpResponse("<h1>Привет из Django 6.1!</h1>")

def experiment(request):
    return HttpResponse(f"<p>Это экспериментальная страница. Владелец: {OWNER}</p>")