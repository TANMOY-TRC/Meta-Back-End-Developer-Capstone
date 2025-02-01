from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date
from api.models import Menu, Booking


class MenuItemsViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)
        self.menu_item1 = Menu.objects.create(
            title="Pizza",
            price=15.99,
            inventory=10
        )
        self.menu_item2 = Menu.objects.create(
            title="Pasta",
            price=12.50,
            inventory=8
        )

    def test_get_menu_items_list(self):
        response = self.client.get('/api/menu-items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_menu_item(self):
        data = {
            'title': 'Salad',
            'price': 8.99,
            'inventory': 15
        }
        response = self.client.post('/api/menu-items/', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Salad')

    def test_create_menu_item_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            'title': 'Salad',
            'price': 8.99,
            'inventory': 15
        }
        response = self.client.post('/api/menu-items/', data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_menu_item(self):
        data = {
            'title': 'Updated Pizza',
            'price': 16.99,
            'inventory': 12
        }
        response = self.client.put(f'/api/menu-items/{self.menu_item1.id}/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Pizza')

    def test_delete_menu_item(self):
        response = self.client.delete(f'/api/menu-items/{self.menu_item1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Menu.objects.filter(id=self.menu_item1.id).exists())


class BookingViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)

    def test_create_booking(self):
        """Test that authenticated users can create a booking."""
        data = {
            'name': 'John Doe',
            'no_of_guests': 2,
            'booking_date': '2024-12-31',
            'booking_slot': 12
        }
        response = self.client.post(reverse('booking-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_create_booking_unauthenticated(self):
        """Test that unauthenticated users cannot create a booking."""
        self.client.force_authenticate(user=None)
        data = {
            'name': 'Jane Doe',
            'no_of_guests': 3,
            'booking_date': '2024-12-31',
            'booking_slot': 14
        }
        response = self.client.post(reverse('booking-list'), data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_bookings(self):
        """Test that authenticated users can list bookings."""
        booking1 = Booking.objects.create(
            name='John Doe',
            no_of_guests=2,
            booking_date=date(2024, 12, 31),
            booking_slot=12
        )
        booking2 = Booking.objects.create(
            name='Jane Doe',
            no_of_guests=3,
            booking_date=date(2024, 12, 31),
            booking_slot=14
        )
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_booking(self):
        """Test that authenticated users can retrieve a specific booking."""
        booking = Booking.objects.create(
            name='John Doe',
            no_of_guests=2,
            booking_date=date(2024, 12, 31),
            booking_slot=12
        )
        response = self.client.get(reverse('booking-detail', args=[booking.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_update_booking(self):
        """Test that authenticated users can update a booking."""
        booking = Booking.objects.create(
            name='John Doe',
            no_of_guests=2,
            booking_date=date(2024, 12, 31),
            booking_slot=12
        )
        data = {
            'name': 'Updated Name',
            'no_of_guests': 3,
            'booking_date': '2024-12-31',
            'booking_slot': 14
        }
        response = self.client.put(reverse('booking-detail', args=[booking.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Name')

    def test_delete_booking(self):
        """Test that authenticated users can delete a booking."""
        booking = Booking.objects.create(
            name='John Doe',
            no_of_guests=2,
            booking_date=date(2024, 12, 31),
            booking_slot=12
        )
        response = self.client.delete(reverse('booking-detail', args=[booking.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Booking.objects.filter(id=booking.id).exists())

    def test_filter_bookings_by_date(self):
        """Test that users can filter bookings by date."""
        booking1 = Booking.objects.create(
            name='John Doe',
            no_of_guests=2,
            booking_date=date(2024, 12, 31),
            booking_slot=12
        )
        booking2 = Booking.objects.create(
            name='Jane Doe',
            no_of_guests=3,
            booking_date=date(2025, 1, 1),
            booking_slot=14
        )
        response = self.client.get(reverse('booking-list') + '?booking_date=2024-12-31')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'John Doe')

