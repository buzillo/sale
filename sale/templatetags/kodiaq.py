from django import template

from cars.models import VygodaKodiaq

register = template.Library()
from services.models import Service


@register.inclusion_tag(
    'cars/kodiaq_list.html')  # регистрируем тег и подключаем шаблон lastnews_tpl.html из папки newslist




def kodiaq():
    kodiaqs = VygodaKodiaq.objects.all()
    return {
        "kodiaqs": kodiaqs
    }