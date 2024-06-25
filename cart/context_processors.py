from .cart import Cart


def cart(request):
    cart = request.session.get('cart', {})

    return {'cart': cart,}
