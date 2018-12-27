from django.contrib import admin
from .models import *
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['username', 'date_create', 'date_update', 'email', 'phone']
admin.site.register(Order, OrderAdmin)
