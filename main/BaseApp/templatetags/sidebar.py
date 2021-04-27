from django import template
from django.db.models import Count

from productApp.models import Tag, Collection, Brand, Color, Size
register = template.Library()

@register.inclusion_tag('BaseApp/sidebar.html')
def show_sidebar(cnt= 4):
    tags = Tag.objects.annotate(Count('product'))
    tag = []
    for item in tags:
        if item.product__count > 0:
            tag.append(item)
    collection = Collection.objects.all()
    colors = Color.objects.all()
    size = Size.objects.all()
    brands = Brand.objects.all()
    context = {
        "tags": tag[:cnt],
        "collection": collection,
        "brands": brands,
        "colors": colors,
        "size": size,
    }
    return context

