from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from cart.cart import Cart
from product.models import Product



def add_to_cart(request):
    if request.method == 'POST' and request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))

            product = get_object_or_404(Product, id=product_id)

            cart = Cart(request)
            cart.add(product=product, quantity=product_qty)

            cart_qty = cart.__len__()

            response = JsonResponse({'qty': cart_qty, 'product': product.name})
            return response
        except ValueError:
            # Handle case where product_id or product_qty cannot be converted to int
            return JsonResponse({'error': 'Invalid data format'}, status=400)
        except Product.DoesNotExist:
            # Handle case where product with given id does not exist
            return JsonResponse({'error': 'Product not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method or action'}, status=400)

def cart_view(request):
    cart = Cart(request)

    context = {
        'cart': cart
    }

    return render(request, "cart/cart/detail.html", context)


@require_POST
def remove_from_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        try:
            product_id = int(request.POST.get('product_id'))
            cart.delete(product=product_id)
            cart_qty = cart.__len__()
            cart_total = cart.get_total_price()
            response_data = {
                'status': 'success',
                'qty': cart_qty,
                'total': cart_total,
            }
            return JsonResponse(response_data)
        except Exception as e:
            # Обработка ошибок, если произошла ошибка при удалении товара
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)




def update_cart_quantity(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        cart = Cart(request)

        action = request.POST.get('action')
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')

        if action == 'post' and product_id is not None and product_qty is not None:
            product_id = int(product_id)
            product_qty = int(product_qty)

            cart.update(product=product_id, quantity=product_qty)

            cart_qty = len(cart)  # Используем функцию __len__() напрямую
            cart_total = cart.get_total_price()

            response = {
                'qty': cart_qty,
                'total': cart_total
            }

            return JsonResponse(response)
        else:
            return JsonResponse({'error': 'Invalid data in POST request'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method or headers'}, status=400)
