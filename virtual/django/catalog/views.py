from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.decorators.cache import cache_page  # Добавлено для кэширования
from django.utils.decorators import method_decorator  # Для декорирования методов классов
from .models import Product, Producer
from .forms import ProductForm

class HomeView(LoginRequiredMixin, ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'cards'
    extra_context = {
        'page_title': 'Home',
    }

    def get_queryset(self):
        return Product.objects.filter(seller_id=self.request.user.id)

class ProductView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'
    extra_context = {
        'page_title': 'Product',
    }

class AddProduct(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'catalog/form_product.html'
    extra_context = {
        'page_title': 'Add product',
        'form_title': 'Add product',
    }

class UpdateProduct(LoginRequiredMixin, UpdateView):
    form_class = ProductForm
    pk_url_kwarg = 'id'
    template_name = 'catalog/form_product.html'
    extra_context = {
        'page_title': 'Update product',
        'form_title': 'Update product',
    }
    
    def get_queryset(self):
        # не автор не может редактировать продукт
        product = Product.objects.filter(Q(pk=self.kwargs[self.pk_url_kwarg]), Q(seller_id=self.request.user.id))
        if not product:
            raise PermissionDenied()
        return product

class DeleteProduct(LoginRequiredMixin, DeleteView):
    pk_url_kwarg = 'id'
    template_name = 'catalog/delete_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('index')
    extra_context = {
        'page_title': 'Delete product',
        'form_title': 'Delete product',
    }
    
    def get_queryset(self):
        # не автор не может удалить продукт
        product = Product.objects.filter(Q(pk=self.kwargs[self.pk_url_kwarg]), Q(seller_id=self.request.user.id))
        if not product:
            raise PermissionDenied()
        return product

# Декорируем функцию для кэширования
@cache_page(300)  # Кэш на 5 минут
def catalog(request):
    query = request.GET.get('query', '')
    producer_id = request.GET.get('producer')
    seller_id = request.GET.get('seller')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_quantity = request.GET.get('min_quantity')

    products = Product.objects.all()

    # Поиск
    if query:
        products = products.filter(
            Q(full_name__icontains=query) | 
            Q(short_name__icontains=query) | 
            Q(description__icontains=query) |
            Q(producer_id__full_name__icontains=query) | 
            Q(seller_id__username__icontains=query)
        )

    # Фильтрация
    if producer_id:
        products = products.filter(producer_id=producer_id)
    if seller_id:
        products = products.filter(seller_id=seller_id)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if min_quantity:
        products = products.filter(quantity__gte=min_quantity)

    # Передаем списки производителей и продавцов в шаблон для фильтрации
    producers = Producer.objects.all()
    sellers = get_user_model().objects.all()

    return render(request, 'catalog/catalog.html', context={
        'page_title': 'Catalog',
        'cards': products,
        'producers': producers,
        'sellers': sellers,
    })
