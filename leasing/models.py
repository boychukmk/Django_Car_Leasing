
# leasing.models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from cars.models import Car
from django.conf import settings
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.name

class ServicePackage(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    services = models.ManyToManyField(Service, related_name='service_packages', verbose_name=_("Services"))

    def base_services_count(self):
        # Логіка для визначення кількості послуг у пакеті "Base Leasing"
        if self.name == "Base Leasing":
            return self.services.count()
        return 0

    def premium_services_count(self):
        # Логіка для визначення кількості преміум послуг
        if self.name != "Base Leasing":
            base_leasing = ServicePackage.objects.filter(name="Base Leasing").first()
            base_services_count = base_leasing.services.count() if base_leasing else 0
            return self.services.count() - base_services_count
        return 0
    def __str__(self):
        return self.name


class LeasingContract(models.Model):
    STATUS_CHOICES = [
        ('Processing', _("В обробці")),
        ('Completed', _("Виконаний")),
        ('In progress', _("Виконується")),
        ('Cancelled', _("Відмінений")),
        ('Сonfirmed', _("Підтверджений")),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("User"))
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name=_("Car"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    service_package = models.ForeignKey(ServicePackage, on_delete=models.CASCADE, verbose_name=_("Service Package"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Price"))
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Monthly Payment"))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing', verbose_name=_("Status"))

    def __str__(self):
        return f"{self.user} - {self.car.name} ({self.car.code})"

    class Meta:
        verbose_name = _("Leasing Contract")
        verbose_name_plural = _("Leasing Contracts")