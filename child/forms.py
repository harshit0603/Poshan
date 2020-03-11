from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import account
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,help_text='Required')

    class Meta:
        model = account
        fields=("email","username","password1","password2")