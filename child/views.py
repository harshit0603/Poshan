from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm

def registration_view(request):
    context={}
    if request.POST:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save(
            email= form.cleaned_data.get('email')
