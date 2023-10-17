from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["injectme"] = "BASIC INJECTION"
        return context
