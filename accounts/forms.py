from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from .models import CustomUser, CustomUserProfile
from django import forms


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join([
            '<div class="error alert alert-danger mt-1">%s</div>' % e for e in self])


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


class CustomUserCreationFormFirst2(forms.ModelForm):
    username = forms.CharField(max_length=20, min_length=5, required=True)
    email = forms.EmailField(required=True)

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

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            self.add_error('email', 'User with this email already exists')
        if CustomUser.objects.filter(username=username).exists():
            self.add_error('username', 'This username is already in use')


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')
        help_texts = {
            "username": ""
        }


class CustomUserProfileChangeForm(forms.ModelForm):
    brith_date = forms.DateTimeField()

    class Meta:
        model = CustomUserProfile
        fields = ('specialization', 'brith_date', 'country', 'city', 'address', 'phone_number', 'upload')
