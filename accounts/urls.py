from django.urls import path

from accounts import views
from accounts.views import SignUpView, profile_update_view, profile_detail_view, profile_list_view, UserCreateView

app_name = 'accounts'


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('update/profile/', profile_update_view, name='update-profile'),
    path('detail/profile/<int:pk>', profile_detail_view, name='detail-profile'),
    path('list/', profile_list_view, name='list-profile'),
    path('form/', UserCreateView.as_view(), name='form-profile'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete-profile'),
]
