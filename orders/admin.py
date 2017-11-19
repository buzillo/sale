from django.contrib import admin
from .models import Order, Order_service

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["car", "name", "phone", "date"]

@admin.register(Order_service)
class Order_serviceAdmin(admin.ModelAdmin):
    list_display = ["service", "name", "phone", "date"]



