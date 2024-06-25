from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from users.forms import ShippingAddressForm

from .models import OrderItem, Order, ShippingAddress


def complete_order(request):
    # if request.POST.get('action') == 'payment':

    return None


def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            order = form.save
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'cart/checkout/checkout.html',
                          {'order': order})
    else:
        form = ShippingAddressForm()
        return render(request, 'cart/checkout/checkout.html', {'cart': cart, 'form': form})


def payment_success(request):
    return None


def payment_fail(request):
    return render(request, 'cart/newpay/payment/payment-failed.html')
