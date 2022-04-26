from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView

from customer.models import Customer
from customer.forms import CustomerForm



# Create your views here.

def customer_form(request):
    if request.method == "POST":

        form = CustomerForm(request.POST)  # bound form

        if form.is_valid():
            form.save()

        return redirect('customer:list-customer')


    form = CustomerForm()  # unbound form
    return render(
        request,
        'customer/customer_form.html',
        context={
            'form': form
        }

    )


class CustomerListView(ListView):
    model = Customer


def customer_detail_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    return render(
        request,
        'customer/customer_detail.html',
        context={
            'customer': customer,
        }
    )


def customer_update_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)  # bound form

        if form.is_valid():
            form.save()

        return redirect('customer:details-customer', customer.id)

    form = CustomerForm(instance=customer)
    return render(
        request,
        'customer/customer_form.html',
        context={
            'customer': customer,
            'form': form,
        }
    )


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer:list-customer')

