from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views
from accounts.views import SignUpView, profile_update_view, profile_detail_view, UserCreateView, \
    ProfileListView

app_name = 'accounts'

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('update/profile/', profile_update_view, name='update-profile'),
    path('detail/profile/<int:pk>', profile_detail_view, name='detail-profile'),
    path('list/', ProfileListView.as_view(), name='list-profile'),
    path('form/', UserCreateView.as_view(), name='form-profile'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete-profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="user_registration/password_reset.html"),
         name='reset_password'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name="user_registration/password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="user_registration/password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name="user_registration/password_reset_done.html"),
         name='password_reset_complete')
]
