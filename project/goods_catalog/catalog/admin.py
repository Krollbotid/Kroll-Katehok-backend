from django.contrib import admin
from .models import Producer, UserType, User, Product, TicketStatus, SupportTicket, SupportMessage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name', 'price', 'quantity', 'producer_id', 'seller_id')
    search_fields = ('full_name', 'short_name', 'description')
    list_filter = ('producer_id', 'seller_id')
    ordering = ('created_at',)


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'short_name', 'email')
    search_fields = ('full_name', 'short_name', 'email')
    list_filter = ('short_name',)
    ordering = ('full_name',)
    inlines = [ProductInline]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'email', 'phone', 'type_id')
    search_fields = ('login', 'email', 'phone')
    list_filter = ('type_id',)
    ordering = ('login',)
    inlines = [ProductInline]

class UserInline(admin.TabularInline):
    model = User
    extra = 1

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [UserInline]


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
