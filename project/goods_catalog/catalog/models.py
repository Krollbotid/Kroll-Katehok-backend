from django.db import models

class Producer(models.Model):
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)

class UserType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

class User(models.Model):
    login = models.CharField(max_length=100)
    type_id = models.ForeignKey(UserType, default=1, on_delete=models.SET_DEFAULT)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

class Product(models.Model):
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
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
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status_id = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

class SupportMessage(models.Model):
    ticket_id = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
    sender_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
