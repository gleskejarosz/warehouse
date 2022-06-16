from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(
        request,
        template_name="index.html"
    )


class HomePage(TemplateView):
    template_name = 'index.html'
