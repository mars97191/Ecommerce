import logging

from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from product.forms import ProductReviewForm
from product.models import Product, Category, ProductReview, Wishlist
from product.recommender import Recommender


def calculate_average_rating(products):
    for product in products:
        average_rating_dict = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
        average_rating = average_rating_dict['rating'] if average_rating_dict['rating'] is not None else 0
        empty_stars_count = 5 - int(round(average_rating))
        setattr(product, 'average_rating', average_rating)
        setattr(product, 'empty_stars_count', empty_stars_count)


def index(request):
    # Получаем все категории верхнего уровня
    parent_categories = Category.objects.filter(parent__isnull=True)
    products = Product.objects.all()
    calculate_average_rating(products)
    context = {'parent_categories': parent_categories, 'products': products}
    return render(request, 'product/index.html', context)


def products(request):
    # Получаем все продукты
    products = Product.objects.all()
    calculate_average_rating(products)
    return render(request, 'product/shop.html', {'products': products})


def products_by_category(request, slug=None):
    # Получаем категорию по ее слагу
    category = get_object_or_404(Category, slug=slug)
    # Получаем все продукты, относящиеся к данной категории
    products = Product.objects.filter(category=category)

    calculate_average_rating(products)

    return render(request, 'product/shop.html',
                  {'category': category, 'products': products})


def product_detail(request, slug):
    # Получаем продукт по его слагу
    product = get_object_or_404(Product, slug=slug)
    # Получаем все изображения для данного продукта
    images = product.images.all()
    # Получаем все продукты из той же категории, исключая текущий продукт
    products = Product.objects.filter(category=product.category).exclude(id=product.id)

    # Получаем все отзывы для данного продукта
    review = ProductReview.objects.filter(product=product)

    # Создаем форму для отзыва о продукте
    review_form = ProductReviewForm()

    # Проверяем, можно ли пользователю оставить отзыв
    make_review = True
    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()
        if user_review_count > 0:
            make_review = False

    # Вычисляем средний рейтинг для продукта
    average_rating_dict = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    average_rating = average_rating_dict['rating'] if average_rating_dict['rating'] is not None else 0

    # Вычисляем количество пустых звезд
    empty_stars_count = 5 - int(round(average_rating))

    # r = Recommender()
    # recommended_products = r.suggest_products_for([product], 4)

    return render(request, 'product/product-details.html', {
        'product': product,
        'images': images,
        'products': products,
        'review': review,
        'average_rating': average_rating,
        'review_form': review_form,
        'make_review': make_review,
        'empty_stars_count': empty_stars_count,
        # 'recommended_products': recommended_products,
    })


def child_categories(request, id):
    # Получаем категорию по ее идентификатору
    category = get_object_or_404(Category, id=id)
    # Получаем все дочерние категории для данной категории
    child_categories = category.children.all()
    context = {
        'parent_category': category,
        'child_categories': child_categories,
    }
    # Возвращаем страницу с дочерними категориями
    return render(request, 'product/categories/cat.html', context)


def ajax_add_review(request, id):
    # Получаем продукт по его идентификатору
    product = Product.objects.get(id=id)
    # Получаем пользователя, отправившего отзыв
    user = request.user

    # Создаем новый отзыв для продукта
    review = ProductReview.objects.create(product=product,
                                          user=user,
                                          review=request.POST['review'],
                                          rating=request.POST['rating'])

    # Формируем контекст для JSON-ответа
    context = {
        'user': user.username,
        'product': product.id,
        'review': request.POST['review'],
        'rating': request.POST['rating']
    }

    # Вычисляем средний рейтинг для продукта после добавления отзыва
    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    # Возвращаем JSON-ответ с информацией о добавленном отзыве и новом среднем рейтинге
    return JsonResponse({'bool': True, 'context': context, 'average_reviews': average_reviews})


def search_view(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query).order_by('-created_at')
    calculate_average_rating(products)

    context = {
        "products": products,
        "query": query,
    }
    return render(request, 'product/shop.html', context)


@login_required
def wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {
        "wishlist": wishlist
    }
    return render(request, 'product/wishlist.html', context)


def add_to_wishlist(request, product_id):
    try:
        # Проверяем, существует ли уже запись о продукте в списке желаний пользователя
        Wishlist.objects.get(user=request.user, product_id=product_id)
        return JsonResponse({'success': False, 'error': 'Продукт уже находится в вашем списке желаний'})
    except Wishlist.DoesNotExist:
        # Если запись не существует, создаем новую
        wishlist_item = Wishlist(user=request.user, product_id=product_id)
        wishlist_item.save()

        wishlist_count = Wishlist.objects.filter(user=request.user).count()
        return JsonResponse({'success': True, 'wishlist_count': wishlist_count})


def remove_wishlist(request, product_id):
    # Находим объект Wishlist, который нужно удалить
    try:
        wishlist_item = Wishlist.objects.get(user=request.user, product_id=product_id)
        wishlist_item.delete()  # Удаляем объект из базы данных
        wishlist_count = Wishlist.objects.filter(user=request.user).count()
        return JsonResponse({'success': True, 'wishlist_count': wishlist_count})
    except Wishlist.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Этот продукт не находится в вашем списке желаний'})
