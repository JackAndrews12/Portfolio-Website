from django.http import HttpResponse
from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})


def current(request):
    return HttpResponse("Current Projects.")
