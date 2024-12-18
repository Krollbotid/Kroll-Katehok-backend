from django import forms
from .models import SupportTicket

CHAR_FIELD_CLASSES = 'one-column-form-item one-column-txt-input'

class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['description']  # Поле для описания проблемы
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Feedback message',
                'class': CHAR_FIELD_CLASSES,
            })}
