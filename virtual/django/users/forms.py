from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

CHAR_FIELD_CLASSES = 'one-column-form-item one-column-txt-input'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Password'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Password'}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel', 'class': CHAR_FIELD_CLASSES, 'placeholder': 'Phone number'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Password'}))

    class Meta:
        model = get_user_model()
        fields = ['email', 'phone', 'username', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'class': CHAR_FIELD_CLASSES, 'placeholder': 'Phone number'}),
            'username': forms.TextInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': CHAR_FIELD_CLASSES, 'placeholder': 'Password'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already exist")
        return email
