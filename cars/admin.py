from django.contrib import admin
from .models import Car, Mail, Scripty, VygodaRapid, VygodaOctavia, VygodaKodiaq, VygodaYeti, VygodaSuperb, Sta


# Register your models here.
@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ["idauto", "modelcar", "complectation", "oldprice", "newprice"]

@admin.register(Mail)
class AdminMail(admin.ModelAdmin):
    list_display = ["mail"]



@admin.register(VygodaRapid)
class AdminScript(admin.ModelAdmin):
    list_display = ["vygoda"]

@admin.register(VygodaOctavia)
class AdminScript(admin.ModelAdmin):
    list_display = ["vygoda_oct"]

@admin.register(VygodaSuperb)
class AdminScript(admin.ModelAdmin):
    list_display = ["vygoda_sup"]


@admin.register(VygodaYeti)
class AdminScript(admin.ModelAdmin):
    list_display = ["vygoda_yeti"]

@admin.register(VygodaKodiaq)
class AdminScript(admin.ModelAdmin):
    list_display = ["vygoda_kod"]



@admin.register(Sta)
class AdminScript(admin.ModelAdmin):
    list_display = ["sta"]
