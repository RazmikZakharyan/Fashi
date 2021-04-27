from django.shortcuts import render

from .models import Product, ProductImage


from django.views.generic import DetailView, View
from CartApp.mixins import CartMixin




class ProductDetail(DetailView):
    model = Product
    template_name = 'productApp/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = super().get_object()
        slideProducts = Product.objects.filter(collection__title= obj.collection.title)[:4]

        context['images'] = ProductImage.objects.filter(product=obj)
        context['categories'] = [obj.category , obj.departments]
        context['products'] = slideProducts
        return context