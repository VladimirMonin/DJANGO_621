from django import template

register = template.Library()


@register.filter
def rating_lable(value):
    # Рейтинги в эмодзи
    if value is None:
        return ""
    elif value == 1:
        return "⭐"
    elif value == 2:
        return "⭐⭐"
    elif value == 3:
        return "⭐⭐⭐"
    elif value == 4:
        return "⭐⭐⭐⭐"
    elif value == 5:
        return "⭐⭐⭐⭐⭐"
    else:
        return ""
