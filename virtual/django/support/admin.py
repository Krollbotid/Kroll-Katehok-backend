from django.contrib import admin
from .models import TicketStatus, SupportTicket, SupportMessage


@admin.register(SupportMessage)
class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'sender_id', 'created_at', 'message')
    search_fields = ('sender_id__login', 'message')
    list_filter = ('ticket_id',)
    ordering = ('created_at',)


class SupportMessageInline(admin.TabularInline):
    model = SupportMessage
    extra = 1


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('creator_id', 'status_id', 'created_at', 'description')
    search_fields = ('creator_id__login', 'description')
    list_filter = ('status_id',)
    ordering = ('created_at',)
    inlines = [SupportMessageInline]


class SupportTicketInline(admin.TabularInline):
    model = SupportTicket
    extra = 1


@admin.register(TicketStatus)
class TicketStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [SupportTicketInline]
