# Generated by Django 4.0.3 on 2022-04-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserprofile',
            name='upload',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
    ]
