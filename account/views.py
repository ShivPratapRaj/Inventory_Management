from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully !!')
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    
    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username = uname, password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/')
        else:
            form = AuthenticationForm()

        return render(request, 'account/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
