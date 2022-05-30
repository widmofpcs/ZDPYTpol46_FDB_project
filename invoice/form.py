from django import forms
from django.forms import ModelForm

from .models import Discount, Invoice
from customer.models import Customer
from task.models import Task


class InvoiceCreateForm(ModelForm):
    customer = forms.ModelChoiceField(queryset=None, required=True),
    discount = forms.ModelChoiceField(queryset=Discount.objects.all(),
                                         empty_label='Select discount',
                                         required=False)
    tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Invoice
        fields = ('discount', 'tasks', 'customer')
        labels = {
            'discount': 'Discount: ',
            'tasks': 'Choose task: ',
        }


class ChooseCustomerForm(ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label='Select customer')

    class Meta:
        model = Invoice
        fields = ('customer',)
        labels = {
            'customer': 'Choose customer'
        }
