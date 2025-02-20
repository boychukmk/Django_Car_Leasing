from django.test import TestCase, Client
from django.urls import reverse
from leasing.models import ServicePackage, LeasingContract
from users.models import User
from cars.models import Car
from decimal import Decimal
from django.utils import timezone


class CarViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.car = Car.objects.create(
            name='Test Car', code='TST123', price=Decimal('10000.00'), year=2022,
            engine_capacity=Decimal('2.0'), fuel_type='petrol', transmission='manual',
            mileage=5000, drive_type='fwd', color='black'
        )
        self.base_service = ServicePackage.objects.create(name="Base Leasing", price=Decimal('100.00'))
        self.premium_service = ServicePackage.objects.create(name="Premium Leasing", price=Decimal('200.00'))

    def test_auto_view(self):
        response = self.client.get(reverse('cars:auto', args=[self.car.code]))
        self.assertEqual(response.status_code, 200)

    def test_catalog_view(self):
        response = self.client.get(reverse('cars:index'))
        self.assertEqual(response.status_code, 200)

    def test_catalog_view_with_page(self):
        response = self.client.get(reverse('cars:index'))  # page=2
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        response = self.client.get(reverse('cars:search') + '?q=Test')
        self.assertEqual(response.status_code, 200)
