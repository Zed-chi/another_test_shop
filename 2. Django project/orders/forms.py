from django import forms

from .models import Order


class OrderShippingForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "payment",
            "firstname",
            "lastname",
            "phonenumber",
            "comment",
            "address",
        ]

    firstname = forms.CharField(
        label="Имя получателя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    lastname = forms.CharField(
        label="Фамилия получателя",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    phonenumber = forms.CharField(
        label="телефон для подтверждения",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    comment = forms.CharField(
        label="Комментарий к заказу",
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )
    address = forms.CharField(
        label="Адрес доставки",
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )
