from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from task.models import Task


@receiver(post_save, sender=Task)
def update_total_cost(sender, instance, created, **kwargs):
    Task.objects.filter(id=instance.id).update(total_cost=F('consumed_time') * F('rate'))

