from django import forms
from django.forms import ModelForm

from .models import Discount, Invoice
from customer.models import Customer
from task.models import Task


class InvoiceCreateForm(ModelForm):
    id_customer = forms.ModelChoiceField(queryset=None, widget=forms.HiddenInput()),
    id_discount = forms.ModelChoiceField(queryset=Discount.objects.all(),
                                         empty_label='Select discount',
                                         required=False)
    id_task = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Invoice
        fields = ('id_discount', 'id_task')
        labels = {
            'id_discount': 'Discount: ',
            'id_task': 'Choose task: ',
        }


class ChooseCustomerForm(ModelForm):
    id_customer = forms.ModelChoiceField(queryset=Customer.objects.all(), empty_label='Select customer')

    class Meta:
        model = Invoice
        fields= ('id_customer',)
        labels = {
            'id_customer': 'Choose customer'
        }
