from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


class Producer(models.Model):
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    seller_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    producer_id = models.ForeignKey(Producer, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse_lazy("product", kwargs={"id": self.pk})
