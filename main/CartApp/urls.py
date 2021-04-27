from django.urls import path, include
from .views import CartView, AddToCartView, DeleteFromCartView, UpdateCartView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add-to-cart/<slug:slug>', AddToCartView.as_view(), name='add-to-cart'),
    path('update/<slug:slug>', UpdateCartView.as_view(), name='update'),
    path('remove-from-cart/<slug:slug>', DeleteFromCartView.as_view(), name='delete-from-cart'),
]