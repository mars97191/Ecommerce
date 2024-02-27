from django.shortcuts import render


def index(request):
    return render(request, 'product/index.html')

def products(request):
    return render(request, 'product/shop.html')