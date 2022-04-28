from datetime import datetime

from django.db import models

from task.models import Task
from customer.models import Customer


class Discount(models.Model):
    value = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return str(self.value)


class Invoice(models.Model):
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    id_discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING, null=True, default='0')
    id_task = models.ManyToManyField(Task,
                                     limit_choices_to={'is_active': False,
                                                       'invoiced': False}, )  # moze byc samo TASK, bo to nie dziala
    number = models.IntegerField(default=0, editable=False)  # auto add
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def no_invoice(self):
        if Invoice.objects.count() == 0:
            return True

    def last_invoice_date(self):
        if not Invoice.no_invoice(self):
            last_date = Invoice.objects.all().last().date_created.strftime("%Y")
            return last_date
        else:
            return datetime.now().strftime("%Y")

    def save(self, *args, **kwargs):

        date_now = datetime.now().strftime("%Y")

        if Invoice.no_invoice(self) or Invoice.last_invoice_date(self) != date_now:
            self.number = 1
            super().save(*args, **kwargs)

        else:
            last_obj = Invoice.objects.all().last()
            self.number = last_obj.number + 1
            super().save(*args, **kwargs)

    def __str__(self):
        return f'Invoice nr {str(self.number)}, issued on {self.date_created},for client: {self.id_customer}'
