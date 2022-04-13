from django.urls import path

from accounts.views import SignUpView, profile_update_view, profile_detail_view

app_name = 'accounts'


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('update/profile/', profile_update_view, name='update-profile'),
    path('detail/profile/<int:pk>', profile_detail_view, name='detail-profile')
]
