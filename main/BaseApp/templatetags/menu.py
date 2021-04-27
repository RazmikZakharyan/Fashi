from django import template
from django.db.models import Count

from productApp.models import Departments, Collection
register = template.Library()

@register.inclusion_tag('BaseApp/menu.html')
def show_menu():
    collection = Collection.objects.all()
    d = Departments.objects.annotate(cnt=Count('product'))
    departments = []
    for item in d:
        if item.cnt > 0:
            departments.append(item)

    context = {
        "collection": collection,
        "departments": departments
    }
    return context
