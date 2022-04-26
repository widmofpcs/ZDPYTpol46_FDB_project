from django.db import models

from accounts.models import CustomUser
from customer.models import Customer


class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET('Former employee'), null=True)
    consumed_time = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)
    id_customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    rate = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)
    total_cost = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    is_active = models.BooleanField(default=True)
    invoiced = models.BooleanField(default=False)

    def __str__(self):

        return self.title

class RequestChangeTask(models.Model):
    STATUS = (
        ('1', 'Waiting'),
        ('2', 'Accepted'),
        ('3', 'Denied'),
    )
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128, null=True)
    description = models.TextField(null=True, blank=True)
    description_of_change = models.TextField(null=True)
    consumed_time = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)
    rate = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)
    is_active = models.BooleanField(default=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    requested_by = models.ForeignKey(
        CustomUser, on_delete=models.SET('Former employee'), null=True, related_name='employee'
    )
    review_by = models.ForeignKey(
        CustomUser, on_delete=models.SET('Former manager'), null=True, related_name='manager'
    )