from django.urls import path
from support import views

app_name = 'support'

urlpatterns = [
    path('create/', views.create_support_ticket, name='create_support_ticket'),
    path('tickets/', views.view_tickets, name='view_tickets'),
    path('tickets/<int:ticket_id>/', views.view_ticket_detail, name='view_ticket_detail'),
    path('success/', views.support_ticket_success, name='support_ticket_success'),
]
