from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('catalog/', views.catalog, name = 'catalog'),
    path('product/<int:id>', views.product, name = 'product'),
    path('support/create/', views.create_support_ticket, name='create_support_ticket'),
    path('support/tickets/', views.view_tickets, name='view_tickets'),
    path('support/tickets/<int:ticket_id>/', views.view_ticket_detail, name='view_ticket_detail'),
    path('support/success/', views.support_ticket_success, name='support_ticket_success'),
]
