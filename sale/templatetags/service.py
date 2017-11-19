from django import template
register = template.Library()
from services.models import Service


@register.inclusion_tag(
    'services/services_list.html')  # регистрируем тег и подключаем шаблон lastnews_tpl.html из папки newslist




def service():
    services = Service.objects.all()
    return {
        "services": services
    }