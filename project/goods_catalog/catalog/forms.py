from django import forms
from .models import SupportTicket

class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['description']  # Поле для описания проблемы
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Введите ваше сообщение'}),
        }
