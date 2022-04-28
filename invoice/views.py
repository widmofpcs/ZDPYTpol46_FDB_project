from django.shortcuts import render, redirect, get_object_or_404
from django import views
from django.views.generic import ListView

from customer.models import Customer
from task.models import Task
from invoice.models import Invoice
from invoice.form import InvoiceCreateForm, ChooseCustomerForm


class InvoiceListView(ListView):
    model = Invoice


class InvoiceDetailView(views.View):

    def get(self, request, number):
        invoice = get_object_or_404(Invoice, number=number)
        return render(
            request,
            'invoice/invoice_detail.html',
            context={
                'invoice': invoice
            }
        )


class InvoiceCustomerChoiceView(views.View):

    def get(self, request):
        customer = request.GET.get('id_customer')

        if customer:
            x = redirect('invoice:task_choice_view')
            x.set_cookie('customer', customer)
            return x

        form = ChooseCustomerForm()
        return render(
            request,
            'invoice/invoice_get_customer.html',
            context={
                'form': form
            }
        )


class InvoiceTaskChoiceView(views.View):

    def get(self, request):
        customer = request.COOKIES.get('customer')
        form = InvoiceCreateForm(initial={'id_customer_id': customer})
        form.fields['id_task'].queryset = Task.objects.filter(id_customer=customer, is_active=False, invoiced=False)

        res = render(
            request,
            'invoice/invoice_create.html',
            context={
                'form': form,
            }
        )
        res.delete_cookie('customer')
        return res

    def post(self, request):
        form = InvoiceCreateForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('invoice:invoice-list')
