from django.urls import path

from customer import views


app_name = 'customer'

urlpatterns = [
    path('list/', views.CustomerListView.as_view(), name='list-customer'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='details-customer'),
    path('form/', views.CustomerFormView.as_view(), name='form-customer'),
    path('update/<int:pk>/', views.CustomerUpdateView.as_view(), name='update-customer'),
    path('delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='delete-customer'),

]
