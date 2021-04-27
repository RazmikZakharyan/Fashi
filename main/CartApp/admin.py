from django.contrib import admin
from .models import CartProduct, Cart, Customer

admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
