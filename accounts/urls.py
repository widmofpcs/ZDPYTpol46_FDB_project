from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('update/profile/<int:pk>/', views.ProfileUpdateView.as_view(), name='update-profile'),
    path('detail/profile/<int:pk>/', views.ProfileDetailView.as_view(), name='detail-profile'),
    path('list/', views.ProfileListView.as_view(), name='list-profile'),
    path('form/', views.UserCreateView.as_view(), name='form-profile'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete-profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="user_registration/password_reset.html"),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="user_registration/password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="user_registration/password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="user_registration/password_reset_done.html"),
         name='password_reset_complete')

]
