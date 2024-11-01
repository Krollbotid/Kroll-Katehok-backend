from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin # А этот миксин - для ограничения доступа к классам представления
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from .models import Product, Producer, SupportTicket, TicketStatus, SupportMessage
from .forms import SupportTicketForm

# Feedback section

@login_required
def create_support_ticket(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator_id = request.user  # Привязываем заявку к текущему пользователю
            ticket.status_id = TicketStatus.objects.get(name="Ожидание")  # Устанавливаем статус по умолчанию
            ticket.save()

            # Отправка email-уведомления сотруднику
            send_mail(
                'Новая заявка в техподдержку',
                f"Пользователь {request.user.login} создал новую заявку: {ticket.description}",
                settings.DEFAULT_FROM_EMAIL,
                ['markuskonev@gmail.com'],  # email техподдержки
                fail_silently=False,
            )

            return redirect('support_ticket_success')
    else:
        form = SupportTicketForm()
    return render(request, 'support/create_ticket.html', {'form': form})

def support_ticket_success(request):
    return render(request, 'support/support_ticket_success.html')

@user_passes_test(lambda u: u.is_staff)
def view_tickets(request):
    """Просмотр списка всех заявок для сотрудников"""
    tickets = SupportTicket.objects.all()
    return render(request, 'support/view_tickets.html', {'tickets': tickets})

@user_passes_test(lambda u: u.is_staff)
def view_ticket_detail(request, ticket_id):
    """Просмотр и ответ на конкретную заявку для сотрудников"""
    ticket = get_object_or_404(SupportTicket, id=ticket_id)
    if request.method == 'POST':
        message = request.POST.get('response')
        SupportMessage.objects.create(ticket_id=ticket, sender_id=request.user, message=message)

        # Отправка email-уведомления пользователю
        send_mail(
            'Ответ на вашу заявку',
            f"Сотрудник ответил на вашу заявку: {message}",
            settings.DEFAULT_FROM_EMAIL,
            [ticket.creator_id.email],
            fail_silently=False,
        )

        ticket.status_id = TicketStatus.objects.get(name="Отвечено")  # Обновляем статус
        ticket.save()
        return redirect('view_tickets')

    messages = ticket.supportmessage_set.all()
    return render(request, 'support/view_ticket_detail.html', {
        'ticket': ticket,
        'messages': messages,
    })

# Searcher section

@login_required # Илья, используй этот декоратор для ограничения доступа незареганным пользакам
def index(request):
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
    sellers = get_user_model().objects.all()

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
