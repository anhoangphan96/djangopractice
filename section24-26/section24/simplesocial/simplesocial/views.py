from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "index.html"


class TestPAge(TemplateView):
    template_name = "test.html"


class ThankPage(TemplateView):
    template_name = "thank.html"
