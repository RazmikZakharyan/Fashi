from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .mixins import CartMixin

from .models import CartProduct
from productApp.models import Product

class CartView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        context = {
            'cart': self.cart,
        }

        return render(request, 'CartApp/cart.html', context)

class AddToCartView(CartMixin, View):

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            product_slug = kwargs.get('slug')
            product = Product.objects.get(slug=product_slug)
            cart_product, created = CartProduct.objects.get_or_create(
                user=self.cart.owner, cart=self.cart,
                product=product, color=request.POST.get('color'),
                size=request.POST.get('size'),
            )

            if created:
                cart_product.final_price = product.price
                self.cart.products.add(cart_product)

            cart_product.qty = int(request.POST.get('qty'))
            cart_product.save()
            self.cart.save()
            return HttpResponseRedirect('/cart/')
        else:
            return HttpResponseRedirect('/accounts/login')

class UpdateCartView(CartMixin, View):

    def post(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)
        cart_product = CartProduct.objects.get(
            user=self.cart.owner, cart=self.cart,
            product=product
        )
        cart_product.qty = int(request.POST.get('qty'))
        cart_product.save()
        self.cart.save()
        return HttpResponseRedirect('/cart/')

class DeleteFromCartView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        if product_slug != 'all':
            product = Product.objects.get(slug=product_slug)
            cart_product = CartProduct.objects.filter(
                user=self.cart.owner, cart=self.cart,
                product=product
            ).first()
            self.cart.products.remove(cart_product)
            cart_product.delete()
        else:
            cart_product = CartProduct.objects.filter(
                user=self.cart.owner, cart=self.cart
            )
            for item in cart_product:
                self.cart.products.remove(item)
                item.delete()

        self.cart.save()
        return HttpResponseRedirect('/cart/')
