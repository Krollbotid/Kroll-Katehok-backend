from django.shortcuts import render
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

# TMP
item = {
    'id': 324,
    'seller': 'Ilya',
    'producer': 'Basynya',
    'full_name': 'Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet.',
    'short_name': 'Lorem ipsum dolor sit amet.',
    'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque amet magni quos expedita nemo sequi voluptas facere nihil ullam tempora voluptatem, corrupti exercitationem qui molestias doloremque ipsam minus dolor quis.',
    'created_at': '2024-10-26',
    'quantity': 3,
    'price': 299.99,
}

def index(request):
    # return HttpResponse("<h1>Index</h1>")
    return render(request, 'index.html')

def catalog(request):
    return render(request, 'catalog/catalog.html', context={
        'page_title': 'Catalog',
        'cards': cards, # брать из БД
    })

def product(request, id):
    return render(request, 'catalog/product.html', context={
        'page_title': 'Product',
        'product': item, # брать из БД, найдя по id и склеив с именами производителя и продавца (по fk)
    })
