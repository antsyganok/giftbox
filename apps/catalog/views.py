from django.shortcuts import render
from .models import Product, Category


def index(request):
    """Главная страница магазина (в каталоге)"""
    products = Product.objects.filter(is_active=True)[:6]
    categories = Category.objects.all()[:4]
    return render(request, 'catalog/index.html', {
        'products': products,
        'categories': categories,
    })


def category(request):
    """Страница с категориями товаров"""
    categories = Category.objects.all()
    return render(request, 'catalog/categories.html', {
        'categories': categories,
    })
