# Generated by Django 4.0.4 on 2022-05-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='tax_number',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
