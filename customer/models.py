from django.db import models
from django_countries.fields import CountryField


class Customer(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    zip_code = models.CharField(max_length=16, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = CountryField(blank_label='(select country)')
    tax_number = models.CharField(max_length=24, null=True, blank=True)
    regon_number = models.CharField(max_length=9, null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name.capitalize()}'
