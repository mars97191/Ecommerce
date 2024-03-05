from django.shortcuts import render, get_object_or_404

from product.models import Product, Category


def index(request):
    parent_categories = Category.objects.filter(parent__isnull=True)
    context = {'parent_categories': parent_categories}
    return render(request, 'product/index.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'product/shop.html', {'products': products})


def products_by_category(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)

    return render(request, 'product/shop.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()

    return render(request, 'product/product-details.html',
                  {'product': product, 'images': images})


def child_categories(request, id):
    category = get_object_or_404(Category, id=id)
    child_categories = category.children.all()
    context = {
        'parent_category': category,
        'child_categories': child_categories,
    }
    return render(request, 'product/categories/cat.html', context)
