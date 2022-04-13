# Generated by Django 4.0.3 on 2022-04-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('consumed_time', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('total_cost', models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True)),
            ],
        ),
    ]
