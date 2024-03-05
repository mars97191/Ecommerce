from django.template.loader import render_to_string

from product.models import Product
from .basket import Basket
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'cart/detail.html', {'basket': basket})


def basket_add(request):
    if request.method == 'POST' and request.POST.get('action') == 'post':
        basket = Basket(request)
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()

        response = JsonResponse({'qty': basketqty})

        return response
    else:
        # Обработка некорректных запросов (GET или другие)
        return JsonResponse({'error': 'Invalid request method'})


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
