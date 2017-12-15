from django import template

from cars.models import VygodaYeti

register = template.Library()
from services.models import Service


@register.inclusion_tag(
    'cars/yeti_list.html')  # регистрируем тег и подключаем шаблон lastnews_tpl.html из папки newslist




def yeti():
    yetis = VygodaYeti.objects.all()
    return {
        "yetis": yetis
    }