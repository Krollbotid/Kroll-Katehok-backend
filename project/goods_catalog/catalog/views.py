from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Producer, User  # предполагается, что эти модели уже подключены
from django.http import HttpResponse

# TMP
cards = [
    {
        'id': 1,
        'short_name': 'Lorem ipsum dolor sit amet.',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque amet magni quos expedita nemo sequi voluptas facere nihil ullam tempora voluptatem, corrupti exercitationem qui molestias doloremque ipsam minus dolor quis.' 
    },
    {
        'id': 2,
        'short_name': 'Lorem ipsum dolor sit amet.',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores minus et ad iusto eveniet ducimus vitae doloribus, accusantium, illum quae ratione eligendi in mollitia voluptates dolorem rerum explicabo eius assumenda. At optio nulla magni dolorum sint unde, provident sit sequi quo beatae reiciendis, aperiam eos molestias totam doloribus facere ipsa!' 
    },
    {
        'id': 3,
        'short_name': 'Lorem ipsum dolor sit amet.',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque amet magni quos expedita nemo sequi voluptas facere nihil ullam tempora voluptatem, corrupti exercitationem qui molestias doloremque ipsam minus dolor quis.' 
    },
    {
        'id': 7,
        'short_name': 'Lorem ipsum dolor sit amet.',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores minus et ad iusto eveniet ducimus vitae doloribus, accusantium, illum quae ratione eligendi in mollitia voluptates dolorem rerum explicabo eius assumenda. At optio nulla magni dolorum sint unde, provident sit sequi quo beatae reiciendis, aperiam eos molestias totam doloribus facere ipsa!' 
    },
    {
        'id': 99,
        'short_name': 'Lorem ipsum dolor sit amet.',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque amet magni quos expedita nemo sequi voluptas facere nihil ullam tempora voluptatem, corrupti exercitationem qui molestias doloremque ipsam minus dolor quis.' 
    },
    {
        'id': 256,
        'short_name': 'Lorem ipsum dolor sit amet.',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores minus et ad iusto eveniet ducimus vitae doloribus, accusantium, illum quae ratione eligendi in mollitia voluptates dolorem rerum explicabo eius assumenda. At optio nulla magni dolorum sint unde, provident sit sequi quo beatae reiciendis, aperiam eos molestias totam doloribus facere ipsa!' 
    },
    {
        'id': 763,
        'short_name': 'Lorem ipsum dolor sit amet.',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores minus et ad iusto eveniet ducimus vitae doloribus, accusantium, illum quae ratione eligendi in mollitia voluptates dolorem rerum explicabo eius assumenda. At optio nulla magni dolorum sint unde, provident sit sequi quo beatae reiciendis, aperiam eos molestias totam doloribus facere ipsa!' 
    },
]

def index(request):
    # return HttpResponse("<h1>Index</h1>")
    return render(request, 'index.html')

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
            Q(seller_id__login__icontains=query)
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
    sellers = User.objects.all()

    return render(request, 'catalog/catalog.html', context={
        'page_title': 'Catalog',
        'cards': products,
        'producers': producers,
        'sellers': sellers,
    })


def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'catalog/product.html', context={
        'page_title': 'Product',
        'product': product,
    })
