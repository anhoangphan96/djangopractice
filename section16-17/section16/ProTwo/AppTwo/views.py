from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<em>My Second App </em>")


def help_func(request):
    my_dict = {"help_insert": "Help page"}
    return render(request, "AppTwo/help.html", my_dict)


# Create your views here.
