from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User


def index(request):
    return render(request, "AppTwo/index.html")


def users(request):
    user_list = User.objects.all()
    return render(request, "AppTwo/users.html", {"user_list": user_list})


# Create your views here.
