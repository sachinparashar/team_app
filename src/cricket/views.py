from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView

def myhandler404(request,exception=None):
    template = '404.html'
    return render(request,template)

def myhandler500(request,exception=None):
    template = '500.html'
    return render(request,template)

class HomeView(TemplateView):
    template_name = 'index.html'