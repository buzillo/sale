# -*- coding: utf-8 -*-
from django.db import models

MODELCAR = (
    ('Rapid', 'Rapid'),
    ('Octavia', 'Octavia'),
    ('Superb', 'Superb'),
    ('Yeti', 'Yeti'),
    ('Kodiaq', 'Kodiaq')
)

POWER = (
        (u'90 л/с', u'90 л/с'),
        (u'110 л/с', u'110 л/с'),
        (u'120 л/с', u'120 л/с'),
        (u'125 л/с', u'125 л/с'),
        (u'150 л/с', u'150 л/с'),
        (u'220 л/с', u'220 л/с'),
        (u'230 л/с', u'230 л/с'),
        (u'250 л/с', u'250 л/с'),
        (u'280 л/с', u'280 л/с'),

    )

# Create your models here.
class Car(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name=u'ID автомобиля')
    modelcar = models.CharField(max_length=200,
                                choices=MODELCAR,
                                default='RAPID', verbose_name=u'Модель')

    complectation = models.CharField(max_length=60, verbose_name=u'Комплектация', default='Ambition')

    ENGINE = (
        ('1.2', '1.2'),
        ('1.4', '1.4'),
        ('1.6', '1.6'),
        ('1.8', '1.8'),
        ('2.0', '2.0'),
        ('2.2', '2.2')
    )
    engine = models.CharField(max_length=200, choices=ENGINE,
                              default='1,6', verbose_name=u'Объем двигателя')

    power = models.CharField(max_length=200,
                             choices=POWER,
                             default='90', verbose_name=u'Мощность двигателя')
    KPP = (
        (u'МКПП', u'МКПП'),
        (u'5 МКПП', u'5 МКПП'),
        (u'6 МКПП', u'6 МКПП'),
        (u'АКПП', u'АКПП'),
        (u'DSG', u'DSG'),
    )

    kpp = models.CharField(max_length=200,
                           choices=KPP,
                           default=u'5МКПП', verbose_name=u'Коробка передач')
    PRIVOD = (
        (u'Передний', u'Передний'),
        (u'Полный', u'Полный')
    )
    privod = models.CharField(max_length=200,
                           choices=PRIVOD,
                           default=u'Передний', verbose_name=u'Привод')

    TYPEENG = (
        ('uБензиновый', 'uБензиновый'),
        ('Дизельный', 'Дизельный')
    )
    tipeeng = models.CharField(max_length=200,
                              choices=TYPEENG,
                              default=u'Бензиновый', verbose_name=u'Тип двигателя')

    color = models.CharField(max_length=200, verbose_name=u'Цвет', default='')
    dop = models.TextField(max_length=1500, verbose_name=u'Дополнительные опции', default=u'Не установлено')


    oldprice = models.CharField(max_length=60, verbose_name=u'Старая цена', default='')
    newprice = models.CharField(max_length=60, verbose_name=u'Новая цена', default='')

    image =  models.ImageField(upload_to='cars/photos', help_text='250x172px',
                              verbose_name=u'Ссылка картинки')
    class Meta:
        verbose_name = u"Автомобиль"
        verbose_name_plural = u"Автомобили"
        ordering = ["modelcar"]

    def __str__(self):
        return str(self.id) + ' | ' + str(self.modelcar) + ' ' + str(self.complectation) \
               + ' | ' + str(self.engine) + ' | ' + str(self.power) \
               + ' | ' + str(self.kpp) + ' | ' + str(self.oldprice) + u'руб. | ' + str(self.newprice) + u'руб.'


class Mail(models.Model):
    mail = models.CharField(max_length=300, verbose_name=u'e-mail для заявок', default='')
    class Meta:
        verbose_name = u"Почта для заявок"
        verbose_name_plural = u"Почта для заявок"

    def __str__(self):
        return str(self.mail)

class Scripty(models.Model):
    script = models.CharField(max_length=600, verbose_name=u'Скрипт', default='')
    class Meta:
        verbose_name = u"Скрипт"
        verbose_name_plural = u"Скрипты"

    def __str__(self):
        return str(self.script)


