# Generated by Django 4.0.4 on 2022-05-29 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_invoice_total_cost_alter_invoice_id_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='id_customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='id_discount',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='id_task',
            new_name='tasks',
        ),
    ]
