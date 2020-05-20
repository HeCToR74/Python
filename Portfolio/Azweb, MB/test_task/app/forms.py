from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class ProductForm(forms.Form):
    name = forms.CharField(label="Name of a Product", min_length=2)
    price = forms.DecimalField(label="Price", min_value=0)

