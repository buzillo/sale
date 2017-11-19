# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(u"Название услуги", max_length=200, default='')
    action = models.CharField(u"Действие (отображение на главной странице)", max_length=1000, default='')
    description = models.TextField(u"Описание услуги блок 1", max_length=2000, default='', blank=True)
    description2 = models.TextField(u"Описание услуги блок 2", max_length=2000, default='', blank=True)
    description3 = models.TextField(u"Описание услуги блок 3", max_length=2000, default='', blank=True)
    description4 = models.TextField(u"Описание услуги блок 4", max_length=2000, default='', blank=True)
    description5 = models.TextField(u"Описание услуги блок 5", max_length=2000, default='', blank=True)
    callmy = models.CharField(u"Обращение перед формой обратной связи)", max_length=1000, default='', blank=True)
    photo = models.ImageField(u"Картинка", upload_to="services/photos", default='', blank=True)

    class Meta:
        verbose_name = u"услуга"
        verbose_name_plural = u"услуги"

    def __str__(self):
        return self.name







