from django import forms
from django_countries.fields import CountryField


class CustomerForm(forms.Form):
    name = forms.CharField(label="Customer name")
    address = forms.CharField(label="Street")
    zip_code = forms.CharField(label="Zip code")
    city = forms.CharField(label="City")
    country = CountryField().formfield()
    tax_number = forms.CharField(label="Tax number")
    regon_number = forms.CharField(label="Regon number")
    email = forms.EmailField(label="Email")
