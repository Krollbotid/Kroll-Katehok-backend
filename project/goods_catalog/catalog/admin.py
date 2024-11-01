from django.contrib import admin
from .models import Producer, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name', 'price', 'quantity', 'producer_id', 'seller_id')
    search_fields = ('full_name', 'short_name', 'description')
    list_filter = ('producer_id', 'seller_id')
    ordering = ('created_at',)


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name', 'email')
    search_fields = ('full_name', 'short_name', 'email')
    list_filter = ('short_name',)
    ordering = ('full_name',)
    inlines = [ProductInline]
