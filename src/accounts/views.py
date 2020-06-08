from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic import View, CreateView
import re
from .forms import UserCreateForm

# Create your views here.

def cleanText(phrase):
    '''
        This function removes the special characters from the string so that we can get simple string for operation
    '''
    pattern=['[^!.?]+']

    for pat in pattern:
        return(re.findall(pat,phrase))


class SignupView(CreateView):
    form_class = UserCreateForm
    success_url = '/accounts/login/'
    template_name = "accounts/signup.html"
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 401
        return response


class LoginView(LoginView):
    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 401
        return response