# Generated by Django 4.0.4 on 2022-05-29 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_requestchangetask_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='id_customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='teamtask',
            old_name='task_id',
            new_name='task',
        ),
    ]
