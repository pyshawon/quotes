# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, UserLoginForm
from django.shortcuts import render, redirect
# Create your views here.


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('quotes')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("quotes")
    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def logout_view(request):
	logout(request)
	return redirect("/")