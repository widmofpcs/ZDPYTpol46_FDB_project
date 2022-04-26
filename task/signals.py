from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from task.models import Task, TeamTask


@receiver(post_save, sender=Task)
def update_total_cost(sender, instance, created, **kwargs):
    Task.objects.filter(id=instance.id).update(total_cost=F('consumed_time') * F('rate'))


@receiver(post_save, sender=Task)
def create_team_task(sender, instance, created, **kwargs):
    if created:
        TeamTask.objects.create(
            name=f'{instance.title} - {instance.created_by.first_name} {instance.created_by.last_name}',
            task_id=instance,
            user_id=instance.created_by
        )
