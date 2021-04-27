from django.http import Http404
from django.db.models import Count
from django.shortcuts import render
from CartApp.mixins import CartMixin
from productApp.models import Product, Category, Collection
from django.views.generic import ListView


class IndexView(CartMixin, ListView):
    model = Product
    template_name = 'BaseApp/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        productMens = Product.objects.filter(collection__slug='men')
        productWomens = Product.objects.filter(collection__slug='women')
        collectionKids = Collection.objects.filter(slug="kid")[0]
        collection = Collection.objects.all()
        category = Category.objects.all()
        context["Men"] = productMens
        context["Women"] = productWomens
        context["CMen"] = productMens[0]
        context["CWomen"] = productWomens[0]
        context["CKids"] = collectionKids
        context["collection"] = collection
        context["category"] = category
        context["range"] = range(1, 7)

        return context


class ShopView(ListView):
    model = Product
    template_name = 'BaseApp/shop.html'
    context_object_name = 'products'
    paginate_by = 6


class DepartmentView(ListView):
    template_name = 'BaseApp/shop.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(departments__slug= self.kwargs['slug'])

class CollectiontView(ListView):
    template_name = 'BaseApp/shop.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(collection__slug= self.kwargs['slug'])

class TagView(ListView):
    template_name = 'BaseApp/shop.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(tags__slug= self.kwargs['slug'])

class CategoryView(ListView):
    template_name = 'BaseApp/shop.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(category__slug= self.kwargs['slug'])

class SearchView(ListView):
    template_name = 'BaseApp/shop.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        try:
            p = Product.objects.filter(title__icontains=self.request.GET.get('s'))
        except:
            raise Http404()
        return p

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        print(context['s'])
        return context
