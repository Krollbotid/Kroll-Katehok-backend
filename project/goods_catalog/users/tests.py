from django.test import TestCase
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='IhateDjango228', email='user@test.com')
        self.assertEqual(user.username, 'testuser')

class RegisterFormTest(TestCase):
    def test_valid_register_form(self):
        form = RegisterForm(data={
            'username': 'testuser', 'email': 'user@test.com', 'phone': '1234567890',
            'password1': 'IhateDjango228', 'password2': 'IhateDjango228'
        })
        self.assertTrue(form.is_valid())

class LoginFormTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='IhateDjango228', email='user@test.com')
        
    def test_valid_login_form(self):
        form = LoginForm(data={'username': 'testuser', 'password': 'IhateDjango228'})
        self.assertTrue(form.is_valid())

class UserViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='PasswordValidationisShit228')

    def test_login_view(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username='user', password='PasswordValidationisShit228')
        response = self.client.get(reverse('users:logout'))
        self.assertRedirects(response, reverse('users:login'))
