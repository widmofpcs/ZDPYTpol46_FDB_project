from django.db.models import F
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from accounts.models import CustomUser
from task.models import Task


@receiver(post_save, sender=Task)
def update_total_cost(sender, instance, created, **kwargs):
    # if instance.consumed_time and instance.rate:
    # # instance.total_cost = F('consumed_time') * F('rate')
    #     temp_inst = Task.objects.get(id=instance.id)
    #     temp_inst.total_cost = 55
    #     temp_inst.save()
    if created:
        # if instance.consumed_time != 0:
        # new_obj = Task.objects.get(id=instance.id)
        new_obj = instance
        new_obj.total_cost = float(new_obj.consumed_time) * float(new_obj.rate)
        new_obj.save()

@receiver(post_save, sender=Task)
def save_total_cost(sender, instance, created, **kwargs):

    new_obj = instance
    new_obj.total_cost = float(new_obj.consumed_time) * float(new_obj.rate)
    new_obj.save()


