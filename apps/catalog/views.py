# from django.shortcuts import render
# from .models import Product


# def index(request):
#     """Главная страница магазина (в каталоге)"""
#     products = Product.objects.filter(is_active=True)[:6]  # пос-ние 6 тов
#     return render(request, 'catalog/index.html', {'products': products})

from django.http import HttpResponse


def index(request):
    return HttpResponse("Каталог работает! 🎉")
