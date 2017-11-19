from django.contrib import admin
from .models import Car, Mail, Scripty


# Register your models here.
@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ["id", "modelcar", "complectation", "oldprice", "newprice"]

@admin.register(Mail)
class AdminMail(admin.ModelAdmin):
    list_display = ["mail"]

@admin.register(Scripty)
class AdminScript(admin.ModelAdmin):
    list_display = ["script"]