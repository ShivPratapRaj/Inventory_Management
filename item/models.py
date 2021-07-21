from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Item(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    size_choice = (
        ('S', 'Short'),
        ('M','Medium'),
        ('L','Long')
    )
    size = models.CharField(max_length=30, choices=size_choice)
    date = models.DateField()
    sold = models.IntegerField(blank=True, null=True)
    left = models.IntegerField(blank=True, null=True)

    