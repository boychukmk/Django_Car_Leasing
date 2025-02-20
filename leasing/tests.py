from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from leasing.models import LeasingContract, ServicePackage, Service
from cars.models import Car
import datetime

User = get_user_model()


class LeasingContractTestCase(TestCase):
    def setUp(self):
        """ Налаштування тестових даних перед кожним тестом """
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.car = Car.objects.create(
            name='Test Car', code='TST123', price=Decimal('10000.00'), year=2022,
            engine_capacity=Decimal('2.0'), fuel_type='petrol', transmission='manual',
            mileage=5000, drive_type='fwd', color='black'
        )
        self.service = Service.objects.create(name="Test Service", description="Basic test service")
        self.service_package = ServicePackage.objects.create(name="Base Leasing", description="Basic package",
                                                             price=500)
        self.service_package.services.add(self.service)

    def test_create_valid_contract(self):
        """ Перевірка успішного створення лізингового контракту """
        start_date = datetime.date.today() + datetime.timedelta(days=1)
        end_date = start_date + datetime.timedelta(days=60)  # Договір на 2 місяці

        contract = LeasingContract.objects.create(
            user=self.user,
            car=self.car,
            start_date=start_date,
            end_date=end_date,
            service_package=self.service_package,
            total_price=1000,
            monthly_payment=500
        )

        self.assertEqual(contract.user, self.user)
        self.assertEqual(contract.car, self.car)
        self.assertEqual(contract.service_package, self.service_package)
        self.assertEqual(contract.total_price, 1000)
        self.assertEqual(contract.monthly_payment, 500)

    def test_invalid_start_date(self):
        """ Перевірка, що стартова дата не може бути сьогодні або в минулому """
        from leasing.forms import LeasingContractForm

        data = {
            'start_date': datetime.date.today(),  # Невірна дата (має бути не раніше завтра)
            'end_date': datetime.date.today() + datetime.timedelta(days=40),
            'service_package': self.service_package.id
        }
        form = LeasingContractForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("start_date", form.errors)
        self.assertEqual(form.errors["start_date"][0], _("Start date must be from tomorrow onwards."))

    def test_invalid_end_date(self):
        """ Перевірка, що кінцева дата має бути не менше 30 днів після початкової """
        from leasing.forms import LeasingContractForm

        data = {
            'start_date': datetime.date.today() + datetime.timedelta(days=1),
            'end_date': datetime.date.today() + datetime.timedelta(days=15),  # Менше 30 днів
            'service_package': self.service_package.id
        }
        form = LeasingContractForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("end_date", form.errors)
        self.assertEqual(form.errors["end_date"][0], _("End date must be at least 30 days ahead of start date."))

    def test_price_calculation(self):
        """ Перевірка, що ціна та місячний платіж коректно розраховуються """

        start_date = datetime.date.today() + datetime.timedelta(days=1)
        end_date = start_date + datetime.timedelta(days=90)  # 3 місяці

        car_part = (self.car.price / 100) * 2
        expected_total = self.service_package.price * 3 + car_part
        expected_monthly = expected_total / 3

        contract = LeasingContract.objects.create(
            user=self.user,
            car=self.car,
            start_date=start_date,
            end_date=end_date,
            service_package=self.service_package,
            total_price=expected_total,
            monthly_payment=expected_monthly
        )

        self.assertAlmostEqual(contract.total_price, expected_total, places=2)
        self.assertAlmostEqual(contract.monthly_payment, expected_monthly, places=2)
