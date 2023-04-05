from django import forms

# from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(
        label="никнейм",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    email = forms.EmailField(
        label="почта",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = UserProfile
        fields = ["name", "email", "password"]


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="почта",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = UserProfile
        fields = ["email", "password"]
