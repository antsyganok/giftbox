from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    # path('category/<slug:slug>/', views.category, name='category'),
    # path('<slug:slug>/', views.product_detail, name='product_detail'),
]
