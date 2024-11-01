from django import forms
from .models import Product, Producer
from users .models import User

CHAR_FIELD_CLASSES = 'one-column-form-item one-column-txt-input'

class ProductForm(forms.ModelForm):
    seller_id = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='Select seller', widget=forms.Select(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Seller'}))
    producer_id = forms.ModelChoiceField(queryset=Producer.objects.all(), empty_label='Select producer', widget=forms.Select(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Producer'}))

    class Meta:
        model = Product
        fields = ['seller_id', 'producer_id', 'full_name', 'short_name', 'description', 'quantity', 'price', ]
        widgets = {
            'seller_id': forms.Select(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Producer'}),
            'producer_id': forms.Select(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Producer'}),
            'full_name': forms.TextInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Full name'}),
            'short_name': forms.TextInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Short name'}),
            'description': forms.Textarea(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Description',  'rows': 4}),
            'quantity': forms.TextInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Quantity', 'type': 'number'}),
            'price': forms.TextInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Price', 'type': 'number'}),
        }
