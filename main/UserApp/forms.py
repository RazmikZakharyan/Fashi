from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username or email address', widget=forms.TextInput(attrs={'id': 'username'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'id': 'pass'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'id': 'con-pass'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username or email address', widget=forms.TextInput(attrs={'id': 'username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'id': 'pass'}))
