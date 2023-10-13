from django.urls import path
from . import views

urlpatterns = [path("", views.help_func, name="help")]
