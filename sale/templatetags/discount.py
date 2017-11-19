from django import template

from cars.models import Mail


register = template.Library()


@register.inclusion_tag(
    'discount.html')  # регистрируем тег и подключаем шаблон lastnews_tpl.html из папки newslist

def discount():
    spisok = "111111111111"  # можно передавать не только строки, но и сложные объекты типа выборки из базы данных
    return {
        'discount': spisok
    }


