from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Task(models.Model):
    name = models.CharField(max_length=128)
