from django.urls import path

from invoice import views
from invoice.views import InvoiceListView, InvoiceTaskChoiceView, InvoiceCustomerChoiceView, InvoiceDetailView

app_name = 'invoice'

urlpatterns = [
    path('detail/<int:number>/', InvoiceDetailView.as_view(), name='invoice-detail'),
    path('list/', InvoiceListView.as_view(), name='invoice-list'),
    path('customer-choice/', InvoiceCustomerChoiceView.as_view(), name='customer-choice'),
    path('create/', InvoiceTaskChoiceView.as_view(), name='task_choice_view'),
]