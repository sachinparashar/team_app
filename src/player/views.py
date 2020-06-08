from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from . models import Players
# Create your views here.
class PlayerDetailView(LoginRequiredMixin,DetailView):
    model = Players

