from django.urls import path

from invoice import views

app_name = 'invoice'

urlpatterns = [
    path('detail/<int:number>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    path('list/', views.InvoiceListView.as_view(), name='invoice-list'),
    path('customer/choice/', views.InvoiceCustomerChoiceView.as_view(), name='customer-choice'),
    path('create/', views.InvoiceTaskChoiceView.as_view(), name='task_choice_view'),
]
