from django.contrib import admin
from .models import Order_service
from cars.models import OrderCar



@admin.register(Order_service)
class Order_serviceAdmin(admin.ModelAdmin):
    list_display = ["service", "name", "phone", "date"]


@admin.register(OrderCar)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id_name", "id_email", "id_car", "date"]


