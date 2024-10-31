from django.db import models
from django.contrib.auth import get_user_model

class Producer(models.Model):
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)

class Product(models.Model):
    # seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    producer_id = models.ForeignKey(Producer, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class TicketStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

class SupportTicket(models.Model):
    # creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    creator_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status_id = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

class SupportMessage(models.Model):
    ticket_id = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
    # sender_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    sender_id = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
