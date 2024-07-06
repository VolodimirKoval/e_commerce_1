from django.contrib import admin
from .models import Category, Products


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'category', 'description', 'price', 'discount', 'quantity', 'image')
    prepopulated_fields = {'slug': ('product_name',)}
