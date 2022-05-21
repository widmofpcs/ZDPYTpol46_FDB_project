from django import views
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView

from customer.models import Customer
from customer.forms import CustomerForm


class CustomerFormView(views.View):

    def get(self, request):
        form = CustomerForm
        return render(
            request,
            'customer/customer_form.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('customer:list-customer')


class CustomerListView(ListView):
    model = Customer


class CustomerDetailView(views.View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)

        return render(
            request,
            'customer/customer_detail.html',
            context={
                'customer': customer,
            }
        )


class CustomerUpdateView(views.View):

    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(instance=customer)
        return render(
            request,
            'customer/customer_form.html',
            context={
                'customer': customer,
                'form': form,
            }
        )

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(request.POST, instance=customer)  # bound form

        if form.is_valid():
            form.save()

        return redirect('customer:details-customer', customer.id)


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer:list-customer')


class RegonTest(views.View):
    def get(self, request):
        return render(
            request,
            'customer/regon_test.html',
        )
