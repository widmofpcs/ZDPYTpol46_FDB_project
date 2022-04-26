from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, CustomUserProfile


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    password1 = forms.CharField(max_length=128, widget=forms.HiddenInput)
    password2 = forms.CharField(max_length=128, widget=forms.HiddenInput)

    class Meta:
        model = CustomUser
        fields = ("username", "email", 'is_manager', 'is_employee')

        labels = {
            "username": "User name",
            "email": "Email",
            "is_manager": "Is manager",
            "is_employee": "Is employee",
        }
        help_texts = {
            "username": ""
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", 'is_manager', 'is_employee')


class CustomUserProfileCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = ('specialization', 'brith_date', 'country', 'city', 'address', 'phone_number', 'upload')


class CustomUserProfileChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = ('specialization', 'brith_date', 'country', 'city', 'address', 'phone_number', 'upload')
