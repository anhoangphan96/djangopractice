from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from . import forms


def index(request):
    return render(request, "AppTwo/index.html")


def users(request):
    user_form = forms.UserForm()
    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        if user_form.is_valid():
            user_form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")

    return render(request, "AppTwo/users.html", {"user_form": user_form})


# Create your views here.
