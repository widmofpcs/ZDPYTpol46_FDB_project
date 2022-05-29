from django import forms
from customer.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        labels = {
            "name": "Customer name",
            "address": "Street",
            "zip_code": "Zip code",
            "city": "City",
            "country": "Country",
            "tax_number": "Tax number",
            "regon_number": "Regon number",
            "email": "Email",
        }

    def clean(self):
        tax_number = self.cleaned_data.get('tax_number')
        if Customer.objects.filter(tax_number=tax_number).exists():
            self.add_error('email', 'Customer with this tax number already exists')
