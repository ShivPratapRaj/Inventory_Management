from django.contrib import admin
from .models import Item

class AdminItem(admin.ModelAdmin):
    list_display = ['product_name', 'quantity', 'size', 'date']
   

# Register your models here.
admin.site.register(Item, AdminItem)