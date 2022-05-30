from django import views
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView

from accounts.forms import DivErrorList
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
            messages.add_message(request, messages.SUCCESS, 'Customer created successfully')
            return redirect('customer:list-customer')
        else:
            form = CustomerForm(request.POST, error_class=DivErrorList)
            return render(
                request,
                'customer/customer_form.html',
                context={
                    'form': form
                }
            )


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
        messages.add_message(request, messages.SUCCESS, 'Updated successfully!')
        return redirect('customer:details-customer', customer.id)


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer:list-customer')
