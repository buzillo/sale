from django import template

from cars.models import VygodaSuperb

register = template.Library()
from services.models import Service


@register.inclusion_tag(
    'cars/superb_list.html')  # регистрируем тег и подключаем шаблон lastnews_tpl.html из папки newslist




def superb():
    superbs = VygodaSuperb.objects.all()
    return {
        "superbs": superbs
    }

