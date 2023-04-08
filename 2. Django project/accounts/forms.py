from django import forms
from .models import UserProfile, ProfileInfo


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


class ProfileForm(forms.Form):
    firstname = forms.CharField(
        label="Имя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    lastname = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    phonenumber = forms.CharField(
        label="Контактный номер телефона",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    address = forms.CharField(
        label="Адрес доставки",
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )

    class Meta:
        model = ProfileInfo
        fields = [
            "firstname",
            "lastname",
            "phonenumber",
            "address",
        ]
