# Generated by Django 4.0.3 on 2022-04-27 11:18

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('address', models.CharField(blank=True, max_length=128, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=6, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('tax_number', models.CharField(blank=True, max_length=10, null=True)),
                ('regon_number', models.CharField(blank=True, max_length=9, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
