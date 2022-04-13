from django.db import models


class Invoice(models.Model):
    # id_customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    # id_task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    pass


class CustomerTask(models.Model):
    pass