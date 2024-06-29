from django.shortcuts import render, redirect
from django.urls import reverse

from cart.cart import Cart
from orders.form import OrderCreateForm
from orders.models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['qty']
                )

            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))

    else:
        form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

