from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import SupportTicket, TicketStatus
from .forms import SupportTicketForm

User = get_user_model()


class SupportTicketModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user', password='password')
        self.status = TicketStatus.objects.create(name="Ожидание")
        self.ticket = SupportTicket.objects.create(
            creator_id=self.user, status_id=self.status, description="Test ticket"
        )

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.creator_id, self.user)


class SupportTicketFormTest(TestCase):
    def test_valid_support_ticket_form(self):
        form = SupportTicketForm(data={'description': 'Test description'})
        self.assertTrue(form.is_valid())


class SupportTicketViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='password', email='user@test.com')
        self.staff = User.objects.create_user(username='staff', password='password', email='staff@test.com', is_staff=True)
        self.status = TicketStatus.objects.create(name="Ожидание")
        self.ticket = SupportTicket.objects.create(
            creator_id=self.user, status_id=self.status, description="Test ticket"
        )

    def test_create_ticket_view(self):
        self.client.login(username='user', password='password')
        response = self.client.post(reverse('support:create_support_ticket'), data={'description': 'New ticket'})
        self.assertRedirects(response, reverse('support:support_ticket_success'))

    def test_view_tickets_for_user(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('support:view_tickets'))
        self.assertContains(response, 'Ticket')
        self.assertContains(response, '(user)')
        self.assertContains(response, 'Create')
        self.assertContains(response, 'new')

    def test_view_ticket_detail_for_author(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse('support:view_ticket_detail', kwargs={'ticket_id': self.ticket.id}))
        self.assertContains(response, 'Test ticket')
        self.assertEqual(response.status_code, 200)

    def test_view_ticket_detail_for_non_author(self):
        self.client.login(username='staff', password='password')
        response = self.client.get(reverse('support:view_ticket_detail', kwargs={'ticket_id': self.ticket.id}))
        self.assertContains(response, 'Test ticket')
        self.assertEqual(response.status_code, 200)
