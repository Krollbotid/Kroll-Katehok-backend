from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class TicketStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SupportTicket(models.Model):
    creator_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status_id = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)


class SupportMessage(models.Model):
    ticket_id = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
    sender_id = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
