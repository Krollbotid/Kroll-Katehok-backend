from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse_lazy
# from django.db.models import Q
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse
# from django.contrib.auth import get_user_model
from .models import SupportTicket, TicketStatus, SupportMessage
from .forms import SupportTicketForm
from django.core.exceptions import PermissionDenied

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
                f"Пользователь {request.user.username} создал новую заявку: {ticket.description}",
                settings.DEFAULT_FROM_EMAIL,
                ['markuskonev@gmail.com'],  # email техподдержки
                fail_silently=False,
            )

            return redirect('support:support_ticket_success')
    else:
        form = SupportTicketForm()
    return render(request, 'support/create_ticket.html', context={
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
    """Просмотр и ответ на конкретную заявку для сотрудников и авторов заявки"""
    ticket = get_object_or_404(SupportTicket, id=ticket_id)
    
    # Проверка доступа: либо сотрудник, либо автор тикета
    if not request.user.is_staff and ticket.creator_id != request.user:
        raise PermissionDenied("Доступ воспрещен")  # Возвращает ошибку 403
    
    # Обработка отправки ответа на тикет
    if request.method == 'POST' and (request.user.is_staff or ticket.creator_id == request.user):
        message = request.POST.get('response')
        SupportMessage.objects.create(ticket_id=ticket, sender_id=request.user, message=message)

        # Отправка email-уведомления автору тикета
        if request.user.is_staff:
            send_mail(
                'Ответ на вашу заявку',
                f"Сотрудник ответил на вашу заявку: {message}",
                settings.DEFAULT_FROM_EMAIL,
                [ticket.creator_id.email],
                fail_silently=False,
            )
        if (ticket.creator_id == request.user):
            ticket.status_id = TicketStatus.objects.get(name="Ожидание")  # Обновляем статус
        else:
            ticket.status_id = TicketStatus.objects.get(name="Отвечено")  # Обновляем статус
        ticket.save()
        return redirect('support:view_ticket_detail', ticket.id)

    # Список сообщений, связанных с тикетом
    messages = ticket.supportmessage_set.all()
    return render(request, 'support/view_ticket_detail.html', {
        'ticket': ticket,
        'messages': messages,
    })
