from django.db.models import F
from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=128)
    consumed_time = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)
    # id_customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    rate = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=1)
    total_cost = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=1)

    # def multiply(self, pk):
    #     cost = Task.objects.get(id=pk)
    #     # cost.total_cost = F('consumed_time') * F('rate')
    #     cost.total_cost = 55
    #     cost.save()




    # reporter = Reporters.objects.get(name='Tintin')
    # reporter.stories_filed = F('stories_filed') + 1
    # reporter.save()