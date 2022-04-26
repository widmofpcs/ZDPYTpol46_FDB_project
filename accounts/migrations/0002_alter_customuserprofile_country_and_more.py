# Generated by Django 4.0.3 on 2022-04-14 14:28

import accounts.models
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserprofile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='customuserprofile',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.CustomUserProfile.user_directory_path),
        ),
    ]