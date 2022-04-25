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



