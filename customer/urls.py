from django.urls import path

from customer import views

app_name = 'customer'


urlpatterns = [
    path('list/', views.CustomerListView.as_view(), name='list-customer'),
    path('<int:pk>/', views.customer_detail_view, name='details-customer'),
    path('form/', views.customer_form, name='form-customer'),
    # path('update/<int:pk>/', views.CustomerUpdateView.as_view(), name='update-customer'),
    path('update/<int:pk>/', views.customer_update_view, name='update-customer'),
    path('delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='delete-customer'),
]
