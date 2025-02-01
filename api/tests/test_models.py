from django.test import TestCase
from api.models import Menu, Booking


class MenuModelTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(
            title="Pizza",
            price=15.99,
            inventory=10
        )

    def test_menu_item_creation(self):
        self.assertIsInstance(self.menu_item, Menu)
        self.assertEqual(self.menu_item.title, "Pizza")
        self.assertEqual(self.menu_item.price, 15.99)
        self.assertEqual(self.menu_item.inventory, 10)

    def test_menu_item_str_representation(self):
        expected_str = "Pizza : 15.99"
        self.assertEqual(str(self.menu_item), expected_str)


class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=2,
            booking_date="2024-12-31",
            booking_slot=12
        )

    def test_booking_creation(self):
        self.assertIsInstance(self.booking, Booking)
        self.assertEqual(self.booking.name, "John Doe")
        self.assertEqual(self.booking.no_of_guests, 2)
        self.assertEqual(self.booking.booking_date, "2024-12-31")
        self.assertEqual(self.booking.booking_slot, 12)

    def test_booking_str_representation(self):
        expected_str = "John Doe : 2024-12-31 12:00H"
        self.assertEqual(str(self.booking), expected_str)
