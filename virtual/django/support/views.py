import requests
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import SupportTicket, TicketStatus, SupportMessage
from .forms import SupportTicketForm
from django.core.exceptions import PermissionDenied


def send_notification(recipient_email, subject, message):
    """Функция для отправки уведомлений через FastAPI"""
    fastapi_url = "http://notification_service:8000/notify/"  # URL FastAPI внутри Docker-сети
    try:
        response = requests.post(
            fastapi_url,
            json={
                "recipient": recipient_email,
                "subject": subject,
                "message": message,
            },
            timeout=5,
        )
        response.raise_for_status()
    except requests.RequestException as e:
        # Логируем ошибку, но не прерываем выполнение
        print(f"Ошибка отправки уведомления: {e}")

# Feedback section


@login_required
def create_support_ticket(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator_id = request.user  # Привязываем заявку к текущему пользователю
            ticket.status_id = TicketStatus.objects.get(name="Ожидание")  # Статус по умолчанию
            ticket.save()

            # Уведомляем техподдержку
            send_notification(
                recipient_email="supportmail@gmail.com",  # Email техподдержки
                subject="Новая заявка в техподдержку",
                message=f"Пользователь {request.user.username} создал заявку: {ticket.description}",
            )

            return redirect('support:support_ticket_success')
    else:
        form = SupportTicketForm()
    return render(request, 'support/create_ticket.html', {
        'page_title': 'Create ticket',
        'form': form,
    })


def support_ticket_success(request):
    return render(request, 'support/support_ticket_success.html')


@login_required
def view_tickets(request):
    """Просмотр тикетов: для сотрудников — все тикеты, для обычных пользователей — только их собственные тикеты"""
    if request.user.is_staff:
        tickets = SupportTicket.objects.all()  # Все тикеты для сотрудников
    else:
        tickets = SupportTicket.objects.filter(creator_id=request.user)  # Только тикеты текущего пользователя
    return render(request, 'support/view_tickets.html', {'tickets': tickets})


@login_required
def view_ticket_detail(request, ticket_id):
    """Просмотр и ответ на конкретную заявку"""
    ticket = get_object_or_404(SupportTicket, id=ticket_id)

    if not request.user.is_staff and ticket.creator_id != request.user:
        raise PermissionDenied("Доступ воспрещен")

    if request.method == 'POST' and (request.user.is_staff or ticket.creator_id == request.user):
        message = request.POST.get('response')
        SupportMessage.objects.create(ticket_id=ticket, sender_id=request.user, message=message)

        # Уведомляем автора тикета
        send_notification(
            recipient_email=ticket.creator_id.email,
            subject="Ответ на вашу заявку",
            message=f"Сотрудник ответил на вашу заявку: {message}",
        )

        if (ticket.creator_id == request.user):
            ticket.status_id = TicketStatus.objects.get(name="Ожидание")
        else:
            ticket.status_id = TicketStatus.objects.get(name="Отвечено")
        ticket.save()
        return redirect('support:view_ticket_detail', ticket.id)

    messages = ticket.supportmessage_set.all()
    return render(request, 'support/view_ticket_detail.html', {
        'ticket': ticket,
        'messages': messages,
    })
