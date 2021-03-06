# Generated by Django 4.0.3 on 2022-04-27 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('consumed_time', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('is_active', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)),
                ('invoiced', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=models.SET('Former employee'), to=settings.AUTH_USER_MODEL)),
                ('id_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='TeamTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task.task')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestChangeTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_of_change', models.TextField(null=True)),
                ('consumed_time', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('is_active', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('status', models.CharField(choices=[('1', 'Waiting'), ('2', 'Accepted'), ('3', 'Denied')], default='1', max_length=1)),
                ('requested_by', models.ForeignKey(null=True, on_delete=models.SET('Former employee'), related_name='employee', to=settings.AUTH_USER_MODEL)),
                ('review_by', models.ForeignKey(null=True, on_delete=models.SET('Former manager'), related_name='manager', to=settings.AUTH_USER_MODEL)),
                ('task_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
    ]
