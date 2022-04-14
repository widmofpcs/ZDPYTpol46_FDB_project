
from django.shortcuts import render, redirect
from customer.models import Customer
from customer.forms import CustomerForm

# Create your views here.

def customer_form(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            Customer.objects.create(
                name=data.get('name'),
                address=data.get('address'),
                zip_code=data.get('zip_code'),
                city=data.get('city'),
                country=data.get('country'),
                tax_number=data.get('tax_number'),
                regon_number=data.get('regon_number'),
                email=data.get('email')
            )

            return redirect(to='home')

    form = CustomerForm()  # unbound form
    return render(
        request,
        'customer/customer_form.html',
        context={
            'form': form
        }
        )