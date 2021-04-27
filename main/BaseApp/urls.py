from django.urls import path, include
from .views import IndexView, ShopView, DepartmentView,\
    CollectiontView, CategoryView, TagView, SearchView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('cart/', include('CartApp.urls'), name='cart'),
    path('Search/', SearchView.as_view(), name='search'),
    path('detail/', include('productApp.urls')),
    path('shop/', ShopView.as_view(), name='shop'),
    path('department/<slug:slug>', DepartmentView.as_view(), name='department'),
    path('collection/<slug:slug>', CollectiontView.as_view(), name='collection'),
    path('category/<slug:slug>', CategoryView.as_view(), name='category'),
    path('tag/<slug:slug>', TagView.as_view(), name='tag'),
    path('accounts/', include('UserApp.urls'), name='login'),
]

