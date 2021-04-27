from django import template
from CartApp.models import Cart, Customer
register = template.Library()

@register.inclusion_tag('BaseApp/cartTag.html')
def cart_menu(request):
    if request.user.is_authenticated:
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(owner=customer).first()
        products = cart.products.all()[:2]
        total = 0
        for item in products:
            total += item.final_price
        context = {
                "cart": cart,
                "products": products,
                "total": total
        }
    else:
        cart = Cart.objects.filter(for_anonymous_user=True).first()
        print(cart)
        if not cart:
            cart = Cart.objects.create(for_anonymous_user=True, pk=5)

        context = {
            "cart": cart,
        }



    return context