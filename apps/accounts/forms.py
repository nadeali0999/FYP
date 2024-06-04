from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class loginForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
