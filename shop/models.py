from django.db import models
import os
from datetime import datetime

from django.utils.text import slugify


def auto_image_folder(instance, filename):
    current_date = datetime.now()
    category_name = instance.category.slug
    return os.path.join(f'products/{current_date.year}/{category_name}/{filename}')


class Category(models.Model):
    category_name = models.CharField(max_length=120, unique=True, verbose_name='Назва категорії')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='URL категорії')
    
    class Meta:
        db_table = 'Категорії'
        verbose_name = 'категорія'
        verbose_name_plural = 'Категорії'
        ordering = ('category_name', 'id',)
    
    def __str__(self):
        return self.category_name


class Products(models.Model):
    product_name = models.CharField(max_length=160, unique=True, verbose_name='Назва продукту')
    slug = models.SlugField(max_length=160, unique=True, verbose_name='URL продукту')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    description = models.TextField(blank=True, null=True, verbose_name='Опис продукту')
    image = models.ImageField(upload_to=auto_image_folder, blank=True, null=True, verbose_name='Фото')
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Ціна')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Знижка')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість')
    
    class Meta:
        db_table = 'products'
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукти'
        ordering = ['category', 'product_name']
    
    def __str__(self):
        return f"{self.product_name} | {self.quantity}"
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        return super().save(*args, **kwargs)
    