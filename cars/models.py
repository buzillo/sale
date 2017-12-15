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
    id = models.BigIntegerField(primary_key=True, verbose_name=u'ID страницы')
    idauto = models.CharField(max_length=200, verbose_name=u'ID автомобиля в базе', default='')
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
    bonus = models.CharField(max_length=300, verbose_name=u'Бонус', default='')
    ico = models.ImageField(upload_to='cars/ico',
                              verbose_name=u'Дополнительная иконка',  default='')

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


class VygodaRapid(models.Model):
    vygoda = models.CharField(max_length=1000, verbose_name=u'Выгоды на Rapid', default='')

    class Meta:
        verbose_name = u"Выгода на Rapid"
        verbose_name_plural = u"Выгода на Rapid"

    def __str__(self):
        return  str(self.vygoda)

class VygodaOctavia(models.Model):
    vygoda_oct = models.CharField(max_length=1000, verbose_name=u'Выгоды на Octavia', default='')

    class Meta:
        verbose_name = u"Выгода на Octavia"
        verbose_name_plural = u"Выгода на Octavia"

    def __str__(self):
        return  str(self.vygoda_oct)

class VygodaSuperb(models.Model):
    vygoda_sup = models.CharField(max_length=1000, verbose_name=u'Выгоды на Superb', default='')

    class Meta:
        verbose_name = u"Выгода на Superb"
        verbose_name_plural = u"Выгода на Superb"

    def __str__(self):
        return  str(self.vygoda_sup)

class VygodaYeti(models.Model):
    vygoda_yeti = models.CharField(max_length=1000, verbose_name=u'Выгоды на Yeti', default='')

    class Meta:
        verbose_name = u"Выгода на Yeti"
        verbose_name_plural = u"Выгода на Yeti"

    def __str__(self):
        return  str(self.vygoda_yeti)


class VygodaKodiaq(models.Model):
    vygoda_kod = models.CharField(max_length=1000, verbose_name=u'Выгоды на Kodiaq', default='')

    class Meta:
        verbose_name = u"Выгода на Kodiaq"
        verbose_name_plural = u"Выгода на Kodiaq"

    def __str__(self):
        return  str(self.vygoda_kod)

class OrderCar(models.Model):
    id_email = models.CharField(u"почта", max_length=200)
    id_name = models.CharField(u"Имя", max_length=200, default='')
    id_car = models.CharField(u"ID автомобиля", max_length=200)
    date = models.DateTimeField(u"Дата", auto_now_add=True)


    def __str__(self):
        return str(self.id_name) + ' | ' + str(self.id_email) + ' | ' + str(self.id_car) + ' | ' + str(self.date)


    class Meta:
        verbose_name = u"Заявка"
        verbose_name_plural = u"Заявки"

class Sta(models.Model):
    sta = models.CharField(max_length=2000, verbose_name=u'Выгоды на Rapid', default='')

    class Meta:
        verbose_name = u"СТА"
        verbose_name_plural = u"СТА"

    def __str__(self):
        return  str(self.sta)
