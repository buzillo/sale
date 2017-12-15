from django import template

from cars.models import VygodaRapid

register = template.Library()
from services.models import Service


@register.inclusion_tag(
    'cars/vigodas_list.html')  # регистрируем тег и подключаем шаблон lastnews_tpl.html из папки newslist




def vyg():
    rapids = VygodaRapid.objects.all()
    return {
        "rapids": rapids
    }

