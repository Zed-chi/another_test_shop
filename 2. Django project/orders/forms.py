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

    # payment = forms.ChoiceField()
