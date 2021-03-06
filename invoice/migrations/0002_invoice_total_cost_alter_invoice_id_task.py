# Generated by Django 4.0.3 on 2022-04-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_requestchangetask_created_date'),
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='id_task',
            field=models.ManyToManyField(limit_choices_to={'invoiced': False, 'is_active': False}, related_name='invoice_tasks', to='task.task'),
        ),
    ]
