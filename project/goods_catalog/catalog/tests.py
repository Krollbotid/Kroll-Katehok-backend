from django.test import TestCase
from django.urls import reverse
from .models import Product, Producer
from .forms import ProductForm
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from users.models import User

class ProductModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.producer = Producer.objects.create(
            full_name='Test Producer', short_name='TP', description='Test producer description', email='producer@test.com'
        )
        self.product = Product.objects.create(
            seller_id=self.user, producer_id=self.producer, full_name='Test Product', short_name='TP', description='A test product', quantity=10, price=100.00
        )

    def test_product_creation(self):
        self.assertEqual(self.product.full_name, 'Test Product')
        self.assertEqual(self.product.seller_id, self.user)

class ProductFormTest(TestCase):
    def setUp(self):
        self.producer = Producer.objects.create(full_name='Producer', short_name='P', email='producer@test.com')
        self.user = User.objects.create(username='seller', password='password')

    def test_product_form_valid_data(self):
        form = ProductForm(data={
            'seller_id': self.user.id, 'producer_id': self.producer.id, 'full_name': 'Valid Product', 'short_name': 'VP',
            'description': 'A valid product description', 'quantity': 10, 'price': 50.00
        })
        self.assertTrue(form.is_valid())

class ProductViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.producer = Producer.objects.create(full_name="Test Producer", short_name="TP", email="producer@test.com")
        self.product = Product.objects.create(
            seller_id=self.user,
            producer_id=self.producer,
            full_name="Test Product",
            short_name="TP",
            description="Test Description",
            quantity=10,
            price=100.00
        )

    def test_index_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_catalog_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('catalog'))
        self.assertEqual(response.status_code, 200)

    def test_product_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('product', kwargs={'id': self.product.id}))
        self.assertEqual(response.status_code, 200)

    def test_add_product_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)

    def test_update_product_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('update', kwargs={'id': self.product.id}))
        self.assertEqual(response.status_code, 200)

    def test_delete_product_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete', kwargs={'id': self.product.id}))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion