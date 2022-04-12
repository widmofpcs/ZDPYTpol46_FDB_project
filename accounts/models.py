from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy


class CustomUser(AbstractUser):
    is_manager = models.BooleanField('Manager status', default=False)
    is_employee = models.BooleanField('Employee status', default=False)

    def __str__(self):
        return self.username


class CustomUserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    specialization = models.CharField(max_length=128, blank=True, null=True)
    brith_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)

    def user_directory_path(self, filename):
        return f'{self.user.username}/{filename}'

    upload = models.ImageField(
        upload_to=user_directory_path, height_field=40, width_field=40, blank=True, null=True
    )


