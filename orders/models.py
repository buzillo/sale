# -*- coding: utf-8 -*-
from django.db import models
from cars.models import Car
from services.models import Service


# Create your models here.
class Order(models.Model):
    car = models.ForeignKey(Car, verbose_name="Автомобиль")
    name = models.CharField(u"Имя", max_length=200)
    phone = models.CharField(u"Телефон", max_length=200)
    date = models.DateTimeField(u"Дата", auto_now_add=True)

    class Meta:
        verbose_name = u"Заявка на автомобиль"
        verbose_name_plural = u"Заявки на автомобиль"


class Order_service(models.Model):

    service = models.ForeignKey(Service, verbose_name=u"Услуга")
    name = models.CharField(u"Имя", max_length=200)
    phone = models.CharField(u"Телефон", max_length=200)
    date = models.DateTimeField(u"Дата", auto_now_add=True)

    class Meta:
        verbose_name = u"Заявка на услугу"
        verbose_name_plural = u"Заявки на услугу"




