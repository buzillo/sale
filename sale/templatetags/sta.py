from django import template

from cars.models import Sta

register = template.Library()
from services.models import Service


@register.inclusion_tag(
    'cars/sta.html')  # регистрируем тег и подключаем шаблон lastnews_tpl.html из папки newslist




def sta():
    stas = Sta.objects.all()
    return {
        "stas": stas
    }

