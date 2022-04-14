from django.urls import path

from customer import views

app_name = 'customer'

urlpatterns = [
    path('form/', views.customer_form, name='form-customer'),

]