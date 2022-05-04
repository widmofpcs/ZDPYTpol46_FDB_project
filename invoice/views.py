from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django import views

from django.views.generic import ListView
from django.db.models import Sum


from customer.models import Customer
from task.models import Task
from invoice.models import Invoice
from invoice.form import InvoiceCreateForm, ChooseCustomerForm


class InvoiceListView(ListView):
    model = Invoice

    def get_queryset(self, *args, **kwargs):
        qs = super(InvoiceListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-number")
        return qs


class InvoiceDetailView(views.View):

    def get(self, request, number):
        invoice = get_object_or_404(Invoice, number=number)

        sum = invoice.get_tasks().aggregate(total_cost=Sum('total_cost'))['total_cost']
        return render(
            request,
            'invoice/invoice_detail.html',
            context={
                'invoice': invoice,
                'sum': sum
            }
        )


class InvoiceCustomerChoiceView(views.View):

    def get(self, request):
        customer = request.GET.get('id_customer')
        if customer:
            task_qs_len = len(Task.objects.filter(id_customer=customer, is_active=False, invoiced=False))
            if not task_qs_len:
                messages.info(request,
                              'Selected customer doesn\'t have any tasks to be invoiced or no tasks selected', )
                return redirect('invoice:customer-choice')
            else:
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

        form = InvoiceCreateForm(initial={'id_customer': customer})
        form.fields['id_task'].queryset = Task.objects.filter(id_customer=customer, is_active=False, invoiced=False)
        form.fields['id_customer'].queryset = Customer.objects.filter(id=customer)

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
        task_ids = request.POST.getlist('id_task')
        customer = request.POST.get('customer')
        form = InvoiceCreateForm(request.POST)
        if len(task_ids) == 0:
            messages.error(
                request,
                'Please select at least one task',
                extra_tags='create_view'
            )
            return redirect('invoice:customer-choice')

        else:
            if form.is_valid():
                form.save()
                # zmiana is_invoiced z False na True:
                for task in task_ids:
                    Task.objects.filter(pk=task).update(invoiced=True)
                return redirect('invoice:invoice-list')
