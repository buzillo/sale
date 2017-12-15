# -*- coding: utf-8 -*-
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField


NOMER = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
)


# Create your models here.
class Service(models.Model):
    pnum = models.CharField(max_length=200, choices=NOMER,
                              default='', verbose_name=u'Порядковый номер')
    name = models.CharField(u"Название услуги", max_length=200, default='')
    ico = models.CharField(u"Иконка ", max_length=1000, default='', help_text='Выбрать иконку http://fontawesome.io/icons/ , кликнуть на нее, скопировать ее название и вставить в это поле')
    action = models.CharField(u"Действие", max_length=1000, default='', help_text='Так будет отображаться ссылка на главной странице')
    description = RichTextUploadingField(u"Описание услуги блок 1", max_length=10000, default='', blank=True)



    callmy = models.CharField(u"Обращение перед формой обратной связи)", max_length=1000, default='', blank=True)
    photo = models.ImageField(u"Картинка", upload_to="services/photos", default='', blank=True)


    class Meta:
        verbose_name = u"услуга"
        verbose_name_plural = u"услуги"
        ordering = ['pnum']

    def __str__(self):
        return str(self.pnum) + ' | ' + str(self.name)







