from django.test import TestCase
from apps.orders.models import Order
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
from apps.events.models import Event
from apps.venues.models import Venue
from django.utils import timezone
from decimal import Decimal

User = get_user_model()

class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = User.objects.create_user(email='testuser@example.com', password='12345', phone_number='+123456789')
        cls.venue = Venue.objects.create(
            name='Test Venue',
            address='123 Test St',
            city='Test City',
            state='TS',
            zip_code='12345',
            capacity=1000
        )
        cls.event = Event.objects.create(
            name='Test Event',
            venue=cls.venue,
            date_time=timezone.now(),
            ticket_price=Decimal('50.00'),
            total_tickets=100,
            available_tickets=100
        )

    def test_order_creation(self):
        order = Order.objects.create(
            user=self.user,
            event=self.event,
            number_of_tickets=2,
            total_amount=Decimal('100.00')
        )
        self.assertTrue(isinstance(order, Order))
        self.assertEqual(order.user.email, 'testuser@example.com')
        self.assertEqual(order.event.name, 'Test Event')
        self.assertEqual(order.number_of_tickets, 2)
        self.assertEqual(order.total_amount, Decimal('100.00'))

    def test_order_str(self):
        order = Order.objects.create(
            user=self.user,
            event=self.event,
            number_of_tickets=1,
            total_amount=Decimal('50.00')
        )
        expected_str = f'Order {order.pk} for event {order.event.name}'
        self.assertEqual(str(order), expected_str)

class OrderViewTests(APITestCase):

    def setUp(self):
        # Create a User instance to be used in the tests
        self.test_user = User.objects.create_user(email='test@example.com', password='Testpass#123', phone_number='+123456789')
        self.client = APIClient()
        self.client.force_authenticate(user=self.test_user)  # Force authentication

        # Create a venue and event
        self.venue = Venue.objects.create(
            name='Venue',
            address='123 Main St',
            city='Anytown',
            state='State',
            zip_code='12345',
            capacity=500
        )
        self.event = Event.objects.create(
            name='Event',
            venue=self.venue,
            date_time=timezone.now(),
            ticket_price=Decimal('20.00'),
            total_tickets=100,
            available_tickets=100
        )

    def test_create_order_success(self):
        # Prepare the URL and data for creating an order
        url = reverse('create_order')
        data = {
            'event_id': self.event.event_id,
            'num_tickets': 2
        }
        # Make a POST request to create an order
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Add assertions for response data as needed