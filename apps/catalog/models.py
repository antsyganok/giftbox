from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категория товаров"""
    name = models.CharField("Название", max_length=200)
    slug = models.SlugField("URL", unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Товар"""
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name="Категория"
    )
    name = models.CharField("Название", max_length=300)
    slug = models.SlugField("URL", unique=True)
    price = models.DecimalField(
        "Цена",
        max_digits=10,
        decimal_places=2
    )
    image = models.ImageField(
        "Изображение",
        upload_to='products/',
        blank=True,
        null=True
    )
    description = models.TextField("Описание", blank=True)
    is_active = models.BooleanField("Активен", default=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'slug': self.slug})
