from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, CustomUserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", 'is_manager', 'is_employee')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", 'is_manager', 'is_employee')


class CustomUserProfileChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = ('specialization', 'brith_date', 'country', 'city', 'address', 'phone_number', 'upload')


