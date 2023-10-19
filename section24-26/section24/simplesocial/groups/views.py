from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from groups.models import Group, GroupMember

# Create your views here.


class CreateGroup(LoginRequiredMixin, CreateView):
    fields = ("name", "description")
    model = Group


class SingleGroup(DetailView):
    model = Group


class ListGroup(ListView):
    model = Group
