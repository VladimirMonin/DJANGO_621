from django.shortcuts import render
from django.http import HttpResponse
from django.template import context

OWNER = "Mr. Robot"


def index(request):
    return HttpResponse("<h1>Привет из Django 6.1!</h1>")


def experiment(request):
    context = {"owner": 'Маня Понич'}
    return render(request, "blog/experiment.html", context=context)
