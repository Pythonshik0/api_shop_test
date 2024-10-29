from .models import Product, Type, Price

from django.contrib import admin
from .models import Product


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля для поиска
    list_filter = ('name',)  # Фильтры в правой части админки

    def description(self, obj):
        return obj.description[:50]  # Обрезаем описание для компактного отображения


class PriceAdmin(admin.ModelAdmin):
    list_display = ('currency', 'amount') # Поля, которые будут отображаться в списке
    search_fields = ('currency',)  # Поля для поиска


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'barcode', 'updated_at', 'product_type')  # Поля, которые будут отображаться в списке
    search_fields = ('name', 'barcode')  # Поля для поиска
    list_filter = ('product_type', 'price')  # Фильтры в правой части админки
    prepopulated_fields = {'barcode': ('name',)}  # Автозаполнение поля barcode на основе name

    def get_queryset(self, request):
        """Переопределяем метод для улучшения производительности при отображении списка."""
        return super().get_queryset(request).select_related('price', 'product_type')



admin.site.register(Type, TypeAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Product, ProductAdmin)