from django import template

from cars.models import VygodaOctavia

register = template.Library()
from services.models import Service


@register.inclusion_tag(
    'cars/octavia_list.html')  # регистрируем тег и подключаем шаблон lastnews_tpl.html из папки newslist




def octavia():
    octavias = VygodaOctavia.objects.all()
    return {
        "octavias": octavias
    }

