from django.db.models import F
from django.db import models

# Create your models here.
from django.urls import reverse


class Task(models.Model):
    name = models.CharField(max_length=128)
    consumed_time = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)
    # id_customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    rate = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)
    total_cost = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=1)
