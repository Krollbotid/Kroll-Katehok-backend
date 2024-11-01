from django.db import models
from django.contrib.auth import get_user_model

class Producer(models.Model):
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)

class Product(models.Model):
    seller_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    producer_id = models.ForeignKey(Producer, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
